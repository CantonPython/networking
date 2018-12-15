
from telnetlib import Telnet

tn = Telnet('localhost', 8000)
tn.write(b'GET /\n\n')
doc = tn.read_all().decode('ascii')
tn.close()

print(doc)
