import socket

def main():
    address = ('localhost', 5005)
    message = 'hello world'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(address)
        while True:
            message = input('> ')
            data = bytes(message+'\n', 'utf-8')
            sock.sendall(data)
            data = sock.recv(1024)
            message = str(data, 'utf-8').rstrip()
            print('received:', message)
    finally:
        sock.close()

if __name__ == '__main__':
    main()
