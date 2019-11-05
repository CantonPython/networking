import xmlrpc.client
import time

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# Print list of available methods
print(s.system.listMethods())

print(s.ping())

print(s.login('tycobb'))
time.sleep(5)

print(s.login('tycobb'))

