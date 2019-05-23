#from PFB_in_Space import Program 

print("Welcome to our concert!")

def get_song(title, composer):
	print(title + " by " + composer + "\n")
	return;

get_song("Also Sprach Zarathustra", "Richard Strauss/ arr. Longfield")
get_song("Selections from ET", "John Williams/ arr. Cacavas")
get_song("We Seven", "Derek M. Jenkins")
get_song("Fly Me to the Moon", "Bart Howard/ arr. Frabizio")
get_song("Star Trek Into Darkness", "Arr. Michael Brown")

def Intermission(x=15):
	while x<15:
		break

get_song("Twelve Seconds to the Moon", "Robert W. Smith")
get_song("Doctor Who: Through Space and Time", "Murray Gold/ arr. Buckley")
get_song("Through the Rings of Saturn", "Ben Kirby")
get_song("Life on Mars", "David Bowie/ arr. Bernaerts")

i = 3
while i > 0:
	print i
	i = i - 1
print "Blast off!"
