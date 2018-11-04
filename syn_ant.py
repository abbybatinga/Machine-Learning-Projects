#creating a list of synonyms and antonyms
from nltk.corpus import wordnet
synonyms = []
antonyms = []

for word in wordnet.synsets("funny"):
    for w in word.lemmas():
        synonyms.append(w.name())
    if w.antonyms():
        antonyms.append(w.antonyms()[0].name())
        
print(set(synonyms))
print(set(antonyms))