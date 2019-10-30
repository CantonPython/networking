import sys
import socket

def main():
    address = ('localhost', 5005)
    message = 'hello world'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(address)
        while True:
            text = input('> ')
            if not text.endswith('\n'):
                text += '\n'
            message = text.encode('utf-8')
            sock.sendall(message)

            message = sock.recv(1024)
            text = message.decode('utf-8').rstrip()
            print('received:', text)
    finally:
        sock.close()

if __name__ == '__main__':
    sys.exit(main())
