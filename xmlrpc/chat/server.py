# Demo chat server with xmlrpc

import os
import time
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class ChatServer:
    def __init__(self):
        self.sessions = {}

    def ping(self):
        return 'pong'

    def login(self, name, password):
        for token in self.sessions:
            session = self.sessions[token]
            if name == session['name']:
                return session['token']
        token = os.urandom(16).hex()
        self.sessions[token] = {
            'token': token,
            'name': name,
            'start': time.time(),
            'messages': [('server', 'welcome')],
        }
        return token

    def logout(self, token):
        self.sessions.pop(token, None)
        return 0

    def post(self, token, message):
        name = self.sessions[token]['name']
        for session in self.sessions.values():
            session['messages'].append((name, message))
        return 0

    def get(self, token):
        session = self.sessions[token]
        messages = session['messages']
        session['messages'] = []
        return messages

def main():
    addr = ('localhost', 8000)
    server = SimpleXMLRPCServer(addr, requestHandler=SimpleXMLRPCRequestHandler)
    server.register_introspection_functions()
    server.register_instance(ChatServer())
    server.serve_forever()

if __name__ == '__main__':
    main()
