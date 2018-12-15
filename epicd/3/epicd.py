
import time
import http.server

HOST = '0.0.0.0' # any
PORT = 8080

class WebHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('got request', self.path)
        uptime = self.server.game.uptime()
        response = 'Uptime is {uptime:.2f} seconds.'.format(uptime=uptime)
        self.respond(response)

    def respond(self, response):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

class GameServer:
    def __init__(self):
        self.players = {}
        self.started = 0
        self.http_server = http.server.HTTPServer((HOST, PORT), WebHandler)
        self.http_server.game = self # context for handlers

    def uptime(self):
        if self.started:
            return time.time() - self.started
        else:
            return 0.0

    def run(self):
        self.started = time.time()
        print('Use control-c to stop...')
        self.http_server.serve_forever()

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

server = GameServer()

# Simulate players joining...
Player(server, 'mike')
Player(server, 'carol')
Player(server, 'jan')

# Start the game server.
server.run()
