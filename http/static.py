from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

address = ('0.0.0.0', 8080)
server = HTTPServer(address, SimpleHTTPRequestHandler)
server.serve_forever()
