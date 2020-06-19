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

# stopwords from the nltk textbook
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 
				'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
				'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
				'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
				'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
				'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 
				'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
				'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
				'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
				'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
				"should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', 
				"didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 
				'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', 
				"wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

punctuation = [".", ",", ";", ":", "!", "?", '’', '“', '—', '”', "-"]

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
		if word not in common and word not in punctuation and word not in stopwords:
			counter += 1
			informative[word] = frequency_distribution[word]
	return informative

# when I ran the program against a short story I wrote, this was the result for the 50 most common words:
{'g': 36, 'robot': 20, '.”': 19, '?”': 16, 'father': 11, 'mother': 11, 'sister': 9, 'liked': 9, 'robots': 8, 'thought': 8, 
'wanted': 8, 'almost': 7, 'things': 7, 'got': 7, 'question': 7, 'felt': 7, ',”': 7, 'ever': 6, 'really': 6, 'fell': 6, 'asked': 6, 
'ask': 6, 'operation': 6, 'consciousness': 6, 'took': 5, 'around': 5, 'family': 5, 'response': 5, 'never': 5, 'home': 5, 'face': 5, 
'room': 5, 'love': 5, 'update': 4, 'industry': 4, 'knowledge': 4, 'years': 4, 'hand': 4, 'features': 4, 'options': 4, 'selection': 4, 
'systems': 4, 'already': 4, 'many': 4, 'always': 4, 'change': 4, 'stop': 4, 'said': 4, 'exactly': 4, 'hobbies': 4}

print(find_informative(freq_dist, 50))

# main issue above: issues of catching punctuation/program splitting the words based on apostrophes as well--get rid of apostrophes first?
# my short story was only about 3500 words, but the word frequencies are interesting
# need better tokenizing capabilities--possibly overwrite the FreqDist function?
# will add more filtering stopwords

