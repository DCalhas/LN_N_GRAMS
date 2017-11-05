import string

final = open("palavra1Anotado.final")

lines = final.readlines()

wordsOnly = {}


for line in lines:
	for c in string.punctuation:
		line = line.replace(c, " ")

	words = line.split(" ")
	if not "<s>" in wordsOnly:
		wordsOnly["<s>"] = 1 
	else:
		wordsOnly["<s>"] = wordsOnly["<s>"] +1

	for word in words:
		if word != " " and word != "" and word!= "\n":
			if not word in wordsOnly:
				wordsOnly[word] = 1
			else:
				wordsOnly[word] = wordsOnly[word] + 1

	if not "</s>" in wordsOnly:
		wordsOnly["</s>"] = 1 
	else:
		wordsOnly["</s>"] = wordsOnly["<s>"] +1
		
	

for word in wordsOnly:
	print(word, wordsOnly[word])
