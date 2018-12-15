import socket

address = ('localhost', 5005)
message = 'hello world'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(address)
    while True:
        message = input()
        if message == "":
            break
        sock.sendall(bytes(message + '\n', 'ascii'))
        print('sent:', message)
        received = str(sock.recv(1024), 'ascii')
        print('received:', received)
finally:
    sock.close()
