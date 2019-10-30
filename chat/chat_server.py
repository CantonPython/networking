#
# Simple chat server.
#
# usage: python3 chat_server.py
#

import sys
import socketserver

class MessageHandler(socketserver.StreamRequestHandler):

    def read(self):
        socket = self.rfile
        line = socket.readline()
        message = line.decode('utf-8')
        return message.rstrip()

    def write(self, message):
        socket = self.wfile
        if not message.endswith('\n'):
            message += '\n'
        line = message.encode('utf-8')
        socket.write(line)

    def handle(self):
        while True:
            message = self.read()
            print(self.request.getpeername(), message)
            self.write('you said: ' + message)


def main():
    ip = 'localhost'
    port = 5005
    address = (ip, port)
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(address, MessageHandler)
    try:
        server.serve_forever()
    finally:
        server.server_close()

if __name__ == '__main__':
    sys.exit(main())
