import socket

address = ('localhost', 5005)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

while True:
    message = input('> ')
    message += '\n'
    sock.send(message.encode('utf-8'))
    print('sent:', message.strip())
    bytes_ = b''
    while True: 
        b = sock.recv(1)
        if b == b'\n':
            break
        bytes_ += b
    received = bytes_.decode('utf-8')
    print('rec', received)
    if message.strip() == 'quit':
        break

sock.close()
