from telnetlib import Telnet
tn = Telnet(host='locahost', port=5005)
tn.interact()
