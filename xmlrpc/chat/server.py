# Demo chat server with xmlrpc

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ChatServer:
    def __init__(self):
        self.sessions = {}

    def ping(self):
        return 'pong'

    def login(self, name):
        print('login:', name)
        if name in self.sessions:
            return 'already logged in'
        self.sessions[name] = 1
        return 'ok'

def main():
    with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
        server.register_introspection_functions()
        server.register_instance(ChatServer())
        server.serve_forever()

if __name__ == '__main__':
    main()
