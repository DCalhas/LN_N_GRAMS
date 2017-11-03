out = open("criamCrerCriar.out")
final = open("criamCrerCriar.final", "w")

lines = out.readlines()

for line in lines:
	divide = line.split("\t")
	if "#" not in divide[0] and "?" not in divide[0]:
		criam = divide[1].split("criam")
		Criam = divide[1].split("Criam")
		if len(criam) + len(Criam) < 4:
			criamRemoved = divide[1].replace("criam", divide[0])
			CriamRemoved = criamRemoved.replace("Criam", divide[0])
			final.write(CriamRemoved)
			
