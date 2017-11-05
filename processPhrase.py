import sys
import string

#unigrams
#bigrams
#parametrization
#test phrases

def calculateBigram(prob, bigram, V, countSecond):
	return prob * ( (1 + int(bigram[2])) / (countSecond + V) )

def calculateSmoothing(prob, leme, prevWord, word, V):
	if prevWord != wordCaps and prevWord != wordMin and word != wordCaps and word != wordMin:
		return prob

	countSecond = 0
	for unigram in unigrams:
		if prevWord == wordMin or prevWord == wordCaps:
			listUnigram = unigram.split(" ")
			if leme == listUnigram[0]:
				countSecond += int(listUnigram[1])
		else:
			listUnigram = unigram.split(" ")
			if prevWord == listUnigram[0]:
				countSecond += int(listUnigram[1])

	return prob * ( 1 / (countSecond + V) )

fileUnigrams = open(sys.argv[1])
fileBigrams = open(sys.argv[2])
fileParametrization = open(sys.argv[3])
filePhrases = open(sys.argv[4])


unigrams = fileUnigrams.readlines()
bigrams = fileBigrams.readlines()
parametrization = fileParametrization.readlines()
phrases = filePhrases.readlines() 


parameter = parametrization[0]
if parameter == "fosse\n":
	wordMin = "fosse"
	wordCaps = "Fosse"
else:
	wordMin = "criam"
	wordCaps = "Criam"

lemes = parametrization[1].split(" ")

V = 0

for unigram in unigrams:
	V += 1

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
				if word == wordCaps or word == wordMin:
					if prevWord == bigramWords[0] and lemes[0] == bigramWords[1]:
						for unigram in unigrams:
							if prevWord == unigram.split(" ")[0]:
								probability1 = calculateBigram(probability1, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
				elif prevWord == wordCaps or prevWord == wordMin:
					if word == bigramWords[1] and lemes[0] == bigramWords[0]:
						for unigram in unigrams:
							if lemes[0] == unigram.split(" ")[0]:
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
				if word == wordCaps or word == wordMin:
					if prevWord == bigramWords[0] and lemes[1] == bigramWords[1]:
						for unigram in unigrams:
							if prevWord == unigram.split(" ")[0]:
								probability2 = calculateBigram(probability2, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
				elif prevWord == wordCaps or prevWord == wordMin:
					if word == bigramWords[1] and lemes[1] == bigramWords[0]:
						for unigram in unigrams:
							if lemes[1] == unigram.split(" ")[0]:
								probability2 = calculateBigram(probability2, bigramWords, V, int(unigram.split(" ")[1]))
						foundAmbiguity = True
						break
			if not foundAmbiguity:
				probability2 = calculateSmoothing(probability2, lemes[1], prevWord, word, V)

			prevWord = word

	print("The probability " + lemes[0], probability1)
	print("The probability " + lemes[1], probability2)

	
	if probability2 > probability1:
		for word in phraseWords:
			if word != wordMin and word != wordCaps:
				print(word + " ", end = '')
			else:
				print(lemes[1] + " ", end = '')
	else:
		for word in phraseWords:
			if word != wordMin and word != wordCaps:
				print(word + " ", end = '')
			else:
				print(lemes[0] + " ", end = '')
