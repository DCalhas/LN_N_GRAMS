import sys
import string

#unigrams
#bigrams
#parametrization
#test phrases

def calculateBigram(prob, bigram, V, countSecond):
	return prob * ( (1 + int(bigram[2])) / (countSecond + V) )

def calculateSmoothing(prob, leme, prevWord, word, V):
	if prevWord != "Fosse" and prevWord != "fosse" and word != "Fosse" and word != "fosse":
		return prob

	for unigram in unigrams:
		if word == "fosse" or word == "Fosse":
			listUnigram = unigram.split(" ")
			if leme == listUnigram[0]:
				countSecond = listUnigram[1]
		else:
			listUnigram = unigram.split(" ")
			if word == listUnigram[0]:
				countSecond = listUnigram[1]

	return prob * ( 1 / (int(countSecond) + V) )

fileUnigrams = open(sys.argv[1])
fileBigrams = open(sys.argv[2])
fileParametrization = open(sys.argv[3])
filePhrases = open(sys.argv[4])


unigrams = fileUnigrams.readlines()
bigrams = fileBigrams.readlines()
parametrization = fileParametrization.readlines()
phrases = filePhrases.readlines() 



lemes = parametrization[1].split(" ")

probability1 = 1
probability2 = 1

V = 0

for bigram in bigrams:
	V += int(bigram.split(" ")[2])

for phrase in phrases:
	probability1 = 1
	probability2 = 1

	for c in string.punctuation:
		phrase = phrase.replace(c, " ")

	phraseWords = phrase.split(" ")

	prevWord = "<s>"
	for word in phraseWords:
		if word != " " and word != "" and word!= "\n":
			foundAmbiguity = False
			for bigram in bigrams:
				bigramWords = bigram.split(" ")
				if word == "Fosse" or word == "fosse":
					if prevWord == bigramWords[0] and lemes[0] == bigramWords[1]:
						for unigram in unigrams:
							if lemes[0] in unigram:
								probability1 = calculateBigram(probability1, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
				elif prevWord == "Fosse" or prevWord == "fosse":
					if word == bigramWords[1] and lemes[0] == bigramWords[0]:
						for unigram in unigrams:
							if word in unigram:
								probability1 = calculateBigram(probability1, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
			if not foundAmbiguity:
				probability1 = calculateSmoothing(probability1, lemes[0], prevWord, word, V)
			prevWord = word

	for word in phraseWords:
		if word != " " and word != "" and word!= "\n":
			foundAmbiguity = False
			for bigram in bigrams:
				bigramWords = bigram.split(" ")
				if word == "Fosse" or word == "fosse":
					if prevWord == bigramWords[0] and lemes[1] == bigramWords[1]:
						for unigram in unigrams:
							if lemes[1] in unigram:
								probability2 = calculateBigram(probability2, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
				elif prevWord == "Fosse" or prevWord == "fosse":
					if word == bigramWords[1] and lemes[1] == bigramWords[0]:
						for unigram in unigrams:
							if word in unigram:
								probability2 = calculateBigram(probability2, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
			if not foundAmbiguity:
				probability2 = calculateSmoothing(probability2, lemes[1], prevWord, word, V)

			prevWord = word

	print("\n\n\nFor the phrase: " + phrase)
	print("Probability of being " + lemes[0],probability1)
	print("Probability of being " + lemes[1],probability2)

	if probability2 > probability1:
		print("So the best fit is: " + lemes[1])
	else:
		print("So the best fit is: " + lemes[0])

print("\nThe Smoothing technique used was Laplace Add-One")