import socket

BUFFER_SIZE = 1024
address = ('localhost', 5005)

message = 'Hello world'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode('utf-8'), address)
message,address = sock.recvfrom(BUFFER_SIZE)
print('from:', address, 'received:', message.decode('utf-8'))
sock.close()
