import socketserver

class EpicRequestHandler(socketserver.StreamRequestHandler):

    def read(self):
        return self.rfile.readline().strip().decode('utf-8')

    def write(self, message):
        message += '\n'
        self.wfile.write(message.encode('utf-8'))

    def handle(self):
        while True:
            message = self.read()
            print(self.request.getpeername(), message)
            if message == 'quit':
                break
            elif message == 'hello':
                self.write('hi')
            else:
                self.write('?')

address = ('localhost', 5005)
socketserver.TCPServer.allow_reuse_address = True
#server = socketserver.TCPServer(address, EpicRequestHandler)
server = socketserver.ThreadingTCPServer(address, EpicRequestHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
