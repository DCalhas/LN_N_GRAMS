import string

final = open("fosseIrSer-2.final")

lines = final.readlines()


bigrams = {}
for line in lines:
	for c in string.punctuation:
		line = line.replace(c, " ")

	words = line.split(" ")

	prevWord = "<s>"


	for word in words:
		if word != " " and word != "" and word != "\n":
			if not prevWord + " " + word in bigrams:
				bigrams[prevWord + " " + word] = 1
				prevWord = word
			else:
				bigrams[prevWord + " " + word] = bigrams[prevWord + " " + word] + 1
				prevWord = word

	if prevWord != " " and prevWord != "" and prevWord != "\n":
		if not prevWord + " </s>" in bigrams:
			bigrams[prevWord + " </s>"] = 1
		else:
			bigrams[prevWord + " </s>"] = bigrams[prevWord + " </s>"] + 1


	

for word in bigrams:
	print(word, bigrams[word])