#using wordnet to find meanings, synonyms, and antonyms
#wordnet is a lexical database
from nltk.corpus import wordnet

synom = wordnet.synsets("exam")
print(synom[0].name()) #index 0 will print first synonym in set
print(synom[0].lemmas()[0].name())#using lemmas will print out just the word
print(synom[0].definition())#.definition will print out meaning
print(synom[0].examples())#word in use