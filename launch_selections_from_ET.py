#!/usr/bin/env python

import sys
import time
from colorama import init, Fore
from tqdm import tqdm

fr = open("lunar_landing_guidance_equations.agc")

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
print("+------------------------------------------------+")
print("| SONG                               |    STATUS |")
print("+------------------------------------------------+")
print("| Also Sprach Zarathustra            | COMPLETED |")
print("| Selections from ET                 |       RUN |")
print("| We Seven                           |   PENDING |")
print("| Fly Me to the Moon                 |   PENDING |")
print("| Star Trek Into Darkness            |   PENDING |")
print("| Twelve Seconds to the Moon         |   PENDING |")
print("| Doctor Who: Through Space and Time |   PENDING |")
print("| Through the Rings of Saturn        |   PENDING |")
print("| Life on Mars                       |   PENDING |")
print("+------------------------------------------------+")
print("| CONCERT PROGRESS                   |       11% |")
print("+------------------------------------------------+\n")

def tprint(words):
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()

message = Fore.CYAN + "Launching song...\n\n" + Fore.RESET
song = Fore.MAGENTA + "Selections from ET by John Williams/ arr. Cacavas\n\n"  + Fore.RESET

tprint(message)
tprint(song)

for i in tqdm(range(10)):
	time.sleep(1.5)


