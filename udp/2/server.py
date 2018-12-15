import socket

BUFFER_SIZE = 1024
address = ('localhost', 5005)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(address)
print('listening on address', address)

try:
    print('press control-c to quit')
    while True:
        message,client = sock.recvfrom(BUFFER_SIZE)
        print('from:', client, 'received:', message.decode('utf-8'))
        reply = 'you said: ' + message.decode('utf-8')
        sock.sendto(reply.encode('utf-8'), client)
except KeyboardInterrupt:
    pass
finally:
    sock.close()
