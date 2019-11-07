import time
import sys
import xmlrpc.client

if len(sys.argv) != 3:
    print('usage: python3 client.py <host> <user>')
    sys.exit(1)

host = sys.argv[1]
name = sys.argv[2]
url = 'http://{0}:8000'.format(host)

s = xmlrpc.client.ServerProxy(url)
token = s.login(name, 'secret')
if not token:
    print('unable to login')
    sys.exit(1)

print('Enter "quit" to quit.')
while True:
    for notification in s.get(token):
        name, message = notification
        print('({0}) {1}'.format(name, message))
    message = input('> ')
    if message == 'quit':
        break
    if message:
        s.post(token, message)
    else:
        time.sleep(1)

s.logout(token)
