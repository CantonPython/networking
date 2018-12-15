
from telnetlib import Telnet

tn = Telnet('localhost', 8000)
tn.write(b'GET /\n\n')
doc = tn.read_all().decode('utf-8')
tn.close()

print(doc)
