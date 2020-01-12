from a.w import *
from a.o import *
from os import system
import sys
from time import sleep
import os

def logo():
 print ("      __ _                               _             _")
 print ("     / _| |__      _ __   ___ _ __   ___| |_ _ __ __ _| |_ ___ _ __")
 print ("    | |_|'_ \    | '_ \ / _ \ '_ \ / _ \ __| '__/ _` | __/ _ \ '__|")
 print ('    |  _| |_) |   | |_) |  __/ | | |  __/ |_| | | (_| | ||  __/ |')
 print ('    |_| |_.__/____| .__/ \___|_| |_|\___|\__|_|  \__,_|\__\___|_|')
 print ('            |_____|_|')
 print ('''
\033[31m   Author:..... CyberWarrior
  App_type:.... Brute force attack
  Version:..... 1.0\033[0m
''')

def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def main():
 system('clear')
 logo()
 print ('''
choose the type of brute force attack

a) Fb brute force attack.
b) my version fb brute force attack.

x) Exit/quit
''')
 msg = input('choose[#]~ ')
 if msg == 'a':
  system('clear')
  p()
 elif msg == 'b':
  system('clear')
  q()
 elif msg == 'x':
  print ('Exiting...')
  sys.exit()
 else:
  print ('\033[31m[!]\033[0m \033[32m invalid input\033[0m')
  sleep(1)
  system('clear')
  restart_program()

if __name__ == "__main__":
        main()

