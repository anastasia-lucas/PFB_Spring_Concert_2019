#!/usr/bin/env python

import sys
import time
from colorama import init, Fore
from tqdm import tqdm
from termcolor import colored, cprint

fr = open("planetary_inertial_orientation.agc")

#def lprint(words):
#    for char in words:
#        time.sleep(0.075)
#        sys.stdout.write(char)
#        sys.stdout.flush()

for line in fr.xreadlines():
	nasa = Fore.WHITE + line + Fore.RESET
	#lprint(nasa)
	time.sleep(0.03)
	sys.stdout.write(nasa)
	sys.stdout.flush()


init()

#def blink(char):                       
#    print(char, end = '\r')           
#    time.sleep(0.5)                       
#    print(' ' * 50, end = '\r')       
#    time.sleep(0.5)	

print("\n")
print("+------------------------------------------------+")
print("| SONG                               |    STATUS |")
print("+------------------------------------------------+")
time.sleep(0.03)
print("| Also Sprach Zarathustra            |       RUN |")
time.sleep(0.03)
print("| Selections from ET                 |   PENDING |")
time.sleep(0.03)
print("| We Seven                           |   PENDING |")
time.sleep(0.03)
print("| Fly Me to the Moon                 |   PENDING |")
time.sleep(0.03)
print("| Star Trek Into Darkness            |   PENDING |")
time.sleep(0.03)
print("| Twelve Seconds to the Moon         |   PENDING |")
time.sleep(0.03)
print("| Doctor Who: Through Space and Time |   PENDING |")
time.sleep(0.03)
print("| Through the Rings of Saturn        |   PENDING |")
time.sleep(0.03)
print("| Life on Mars                       |   PENDING |")
time.sleep(0.03)
print("+------------------------------------------------+")
time.sleep(0.03)
print("| CONCERT PROGRESS                   |        0% |")
time.sleep(0.03)
print("+------------------------------------------------+\n")

def tprint(words):
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()

message = Fore.CYAN + "Launching song...\n\n" + Fore.RESET
song = Fore.MAGENTA + "Also Sprach Zarathustra by Richard Strauss/ arr. Longfield \n\n"  + Fore.RESET

tprint(message)
tprint(song)

for i in tqdm(range(10)):
	time.sleep(1.5)


