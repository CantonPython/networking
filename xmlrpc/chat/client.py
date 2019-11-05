import xmlrpc.client
import time

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# Print list of available methods
print(s.system.listMethods())

print(s.ping())

token = s.login('tycobb', 'secret')
print('login token:', token)

s.post(token, 'hello world')
time.sleep(1)

for message in s.get(token):
    print('>', message)

s.logout(token)
