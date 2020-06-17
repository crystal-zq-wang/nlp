### TRYING TO SET UP OWN CORPUS, FILTERING OUT COMMON UNINFORMATIVE WORDS

from nltk.corpus import PlaintextCorpusReader
import nltk

# 100 most common English words, from Wikipedia

common = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", 
			"he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", 
			"or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", 
			"about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", 
			"know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", 
			"than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", 
			"two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", 
			"give", "day", "most", "us"]

punctuation = [".", ",", ";", ":", "!", "?", '’', '“', '-']

corpus_root = # the location of the text for me
robot = PlaintextCorpusReader(corpus_root, 'robo.txt') # important: the txt file shouldn't have any weird characters for formatting!
														# possibly write a program to clean this up?

all_words = robot.words()
freq_dist = nltk.FreqDist([w.lower() for w in all_words])

def find_informative(frequency_distribution, n):
	# currently does not account for running out of words...will update this later?
	""" Returns a dictionary of the n most common words from the frequency distribution. """
	informative = {}
	counter = 0
	for word in frequency_distribution:
		if counter >= n:
			break
		if word not in common and word not in punctuation:
			counter += 1
			informative[word] = frequency_distribution[word]
	return informative

# when I ran the program against a short story I wrote, this was the result:
{'i': 133, 'was': 49, 's': 46, 'g': 36, 'had': 28, 't': 22, 'robot': 20, '.”': 19, '?”': 16, 'were': 15, 'before': 11, 'father': 11, 
'd': 11, 'mother': 11, '”': 10, 'did': 9, 'sister': 9, 'liked': 9, 'robots': 8, 'thought': 8, 'wanted': 8, 'didn': 8, 'almost': 7, 
'things': 7, '—': 7, 'got': 7, 'question': 7, 'felt': 7, ',”': 7, 'been': 6, 'ever': 6, 'really': 6, 'fell': 6, 'asked': 6, 'ask': 6, 
'off': 6, 'operation': 6, 'consciousness': 6, 'are': 5, 'down': 5, 'too': 5, 'took': 5, 'around': 5, 'family': 5, 'response': 5, 'never': 5, 
'home': 5, 'face': 5, 'room': 5, 'love': 5}

# main issue above: issues of catching punctuation/program splitting the words based on apostrophes as well--get rid of apostrophes first?
# my short story was only about 3500 words, so not super great at seeing trends.
# need better tokenizing capabilities--possibly overwrite the FreqDist function?

