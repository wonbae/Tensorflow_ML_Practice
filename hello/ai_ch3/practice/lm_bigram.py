import math, collections


SENTENCE_BEGIN = '-BEGIN-'

corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]
    
# Counting
unigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for word in words:
        unigram_counts[word] += 1

bigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for i in range(len(words)-1):
        bigram_counts[(words[i], words[i+1])] += 1


# Bigram function
def bigram(prev_word, curr_word):
    return float(bigram_counts[(prev_word, curr_word)]) / unigram_counts[prev_word]


# Printing results
print('\n- Bigram probabilities - ')
print(('P(I | -BEGIN- ) = %f'%bigram(SENTENCE_BEGIN, 'I')))
print(('P(Sam | -BEGIN-) = %f'%bigram(SENTENCE_BEGIN, 'Sam')))
print(('P(do | I) = %f'%bigram('I', 'do')))
print(('P(green | like ) = %f'%bigram('like', 'green')))
