import socket

address = ('localhost', 5005)
message = 'hello world'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(address)
    while True:
        message = input('> ')
        if message == '':
            message = 'quit'
        message += '\n'
        sock.sendall(message.encode('utf-8'))
        print('sent:', message.strip())
        received = sock.recv(1024).decode('utf-8')
        print('received:', received.strip())
        if message == 'quit':
            break
finally:
    sock.close()
