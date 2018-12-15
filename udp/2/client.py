import socket
import sys

BUFFER_SIZE = 1024
host = 'localhost'
port = 5005
address = (host, port)

try:
    message = sys.argv[1]
except:
    message = 'Hello world'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('sending message:', message)
sock.sendto(message.encode('utf-8'), address)

print('waiting for reply')
message,address = sock.recvfrom(BUFFER_SIZE)
print('from:', address, 'received:', message.decode('utf-8'))

sock.close()
