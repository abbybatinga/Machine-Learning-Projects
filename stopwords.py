# testing filtering tokenized sentence using stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "Abigail is my name and I live in Seattle"
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)

filterdlist = []

for w in tokens:
    if w not in stop_words:
        filterdlist.append(w)

print(filterdlist) 