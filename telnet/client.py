
from telnetlib import Telnet

tn = Telnet('localhost', 5005)

while True:
    request = input('> ')
    if request == '':
        request = 'quit'
    request += '\n'
    tn.write(request.encode('utf-8'))
    response = tn.read_until(b'\n').decode('utf-8')
    print(response.strip())
    if request.strip() == 'quit':
        break

tn.close()

