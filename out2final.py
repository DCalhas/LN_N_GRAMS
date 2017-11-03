out = open("fosseIrSer-2.out")
final = open("fosseIrSer-2.final", "w")

lines = out.readlines()

for line in lines:
	divide = line.split("\t")
	if "#" not in divide[0] and "?" not in divide[0]:
		criam = divide[1].split("fosse")
		Criam = divide[1].split("Fosse")
		if len(criam) + len(Criam) < 4:
			criamRemoved = divide[1].replace("fosse", divide[0])
			CriamRemoved = criamRemoved.replace("Fosse", divide[0])
			final.write(CriamRemoved)
			
