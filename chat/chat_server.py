#
# Simple chat server with tcp/ip sockets.
#
# usage: python3 chat_server.py
#

import sys
import re
import socketserver

class ChatServer(socketserver.StreamRequestHandler):

    def read_message(self):
        data = self.rfile.readline()
        message = str(data, 'utf-8').rstrip()
        return message

    def write_message(self, message):
        data = bytes(message+'\n', 'utf-8')
        self.wfile.write(data)

    def handle(self):
        sessions = {}
        while True:
            message = self.read_message()
            print(self.request.getpeername(), message)
            if not message:
                continue
            if message.startswith('/join'):
                self.write_message('welcome')
            else:
                sys.stderr.write('ERROR: {0}\n'.format(message))

def main():
    ip = 'localhost'
    port = 5005
    address = (ip, port)
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(address, ChatServer)
    try:
        server.serve_forever()
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
