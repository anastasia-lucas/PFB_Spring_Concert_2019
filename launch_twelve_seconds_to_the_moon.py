#!/usr/bin/env python

import sys
import time
from colorama import init, Fore
from tqdm import tqdm

fr = open("the_lunar_landing.agc")

#def lprint(words):
#    for char in words:
#        time.sleep(0.075)
#        sys.stdout.write(char)
#        sys.stdout.flush()

for line in fr.xreadlines():
	nasa = message = Fore.WHITE + line + Fore.RESET
	#lprint(nasa)
	time.sleep(0.03)
	sys.stdout.write(nasa)
	sys.stdout.flush()


init()

print("\n")
print(" ------------------------------------------------")
print("| SONG                               |    STATUS |")
print(" ------------------------------------------------")
print("| Also Sprach Zarathustra            | COMPLETED |")
print("| Selections from ET                 | COMPLETED |")
print("| We Seven                           | COMPLETED |")
print("| Fly Me to the Moon                 | COMPLETED |")
print("| Star Trek Into Darkness            | COMPLETED |")
print("| Twelve Seconds to the Moon         |       RUN |")
print("| Doctor Who: Through Space and Time |   PENDING |")
print("| Through the Rings of Saturn        |   PENDING |")
print("| Life on Mars                       |   PENDING |")
print(" ------------------------------------------------")
print("| CONCERT PROGRESS                   |       55% |")
print(" ------------------------------------------------\n")

def tprint(words):
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()

message = Fore.CYAN + "Launching song...\n\n" + Fore.RESET
song = Fore.MAGENTA + "Twelve Seconds to the Moon by Robert W. Smith\n\n"  + Fore.RESET

tprint(message)
tprint(song)

for i in tqdm(range(10)):
	time.sleep(1.5)


