
import time

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

class GameServer:
    def __init__(self):
        self.players = {}

server = GameServer()

# Simulate players joining...
Player(server, 'mike')
Player(server, 'carol')
Player(server, 'jan')

