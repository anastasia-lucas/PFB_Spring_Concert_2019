load("PFB_in_Space/Program")

print("Welcome to our concert!")

get_song <- function(title, composer){
	song <- paste(title, composer, sep=" by ")
	return(song)
}

get_song("Also Sprach Zarathustra", "Richard Strauss/ arr. Longfield")
get_song("Selections from ET", "John Williams/ arr. Cacavas")
get_song("We Seven", "Derek M. Jenkins")
get_song("Fly Me to the Moon", "Bart Howard/ arr. Frabizio")
get_song("Star Trek Into Darkness", "Arr. Michael Brown")

Intermission <- function(x){
	break
}

get_song("Twelve Seconds to the Moon", "Robert W. Smith")
get_song("Doctor Who: Through Space and Time", "Murray Gold/ arr. Buckley")
get_song("Through the Rings of Saturn", "Ben Kirby")
get_song("Life on Mars", "David Bowie/ arr. Bernaerts")

for i in c(3,2,1){
	print(i)
}
print("Blast off!")
