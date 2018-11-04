#calculates similarity of words
from nltk.corpus import wordnet
w1 = wordnet.synset('house.n.01')
w2 = wordnet.synset('home.n.01')
print(w1.wup_similarity(w2))

w3 = wordnet.synset('apple.n.01')
w4 = wordnet.synset('dog.n.01')
print(w3.wup_similarity(w4)) 