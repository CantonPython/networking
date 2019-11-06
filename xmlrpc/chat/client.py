import time
import sys
import xmlrpc.client

url = 'http://100.115.92.205:8000'
s = xmlrpc.client.ServerProxy(url)

name = sys.argv[1]
token = s.login(name, 'secret')

print('Enter "quit" to quit.')
while True:
    for message in s.get(token):
        print(message)
    message = input('> ')
    if message == 'quit':
        break
    if message:
        s.post(token, message)
    else:
        time.sleep(1)

s.logout(token)
