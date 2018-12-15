
import time
import http.server
import socketserver
import threading

HOST = '0.0.0.0' # any
PORT = 8080
GAME_PORT = 5005

class WebHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('got request', self.path)
        if self.path == '/':
            self.show_status()
        else:
            self.send_error(404, 'not found')

    def show_status(self):
        game = self.server.game
        response = '<p>Uptime is {game.uptime:.2f} seconds.</p>\n'.format(game=game)
        response += '<ul>\n'
        for p in game.players.values():
            response += '<li>{p.username} joined {p.joined:.2f}</li>\n'.format(p=p)
        response += '</ul>\n'
        self.respond(response)

    def respond(self, response):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

class Player:
    def __init__(self, server, username):
        if username in server.players:
            raise ValueError('player "%s" already joined' % (username))
        self.username = username
        self.realname = None
        self.health = 100
        self.gold = 0
        self.score = 0
        self.joined = time.time()
        server.players[username] = self

class GameHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('connection from', self.request.getpeername())
        while True:
            request = self.rfile.readline().strip().decode('utf-8')
            print('request:', request)
            response = 'you said: ' + request
            self.wfile.write(response.encode('utf-8'))
            self.wfile.write('\n'.encode('utf-8'))
            if request == 'quit':
                print('bye')
                break

class GameServer:
    def __init__(self):
        self.players = {}
        self.started = 0
        self.http_server = http.server.HTTPServer((HOST, PORT), WebHandler)
        self.http_server.game = self # context for handlers
        self.socket_server = socketserver.ThreadingTCPServer((HOST, GAME_PORT), GameHandler)
        self.socket_server.game = self # context for handlers

    @property
    def uptime(self):
        if self.started:
            return time.time() - self.started
        else:
            return 0.0

    def run(self):
        self.started = time.time()
        # Start a thread with the server -- that thread will then start one
        # more thread for each request  Exit the server thread when the main
        # thread terminates
        server_thread = threading.Thread(target=self.socket_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        print('Use control-c to stop...')
        self.http_server.serve_forever()

server = GameServer()

# Simulate players joining...
Player(server, 'mike')
Player(server, 'carol')
Player(server, 'jan')

# Start the game server.
server.run()
