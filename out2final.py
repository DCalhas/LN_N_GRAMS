out = open("fosseIrSer-2.out")
final = open("fosseIrSer-2.final", "w")

lines = out.readlines()

for line in lines:
	divide = line.split("\t")
	if "#" not in divide[0] and "?" not in divide[0]:
		fosse = divide[1].split("fosse")
		Fosse = divide[1].split("Fosse")
		if len(fosse) + len(Fosse) < 4:
			fosseRemoved = divide[1].replace("fosse", divide[0])
			FosseRemoved = fosseRemoved.replace("Fosse", divide[0])
			final.write(FosseRemoved)
			