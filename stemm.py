#tokenized, stopwords filtered, stemmed
from nltk.corpus import stopwords, state_union
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer
text = """Abigail is my name and I live in Seattle and I am living in Seattle.\n
I ride my car to work and I also like riding my car to school."""
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)
filterdlist = []
stem = PorterStemmer()
for w in tokens:
    if w not in stop_words:
        filterdlist.append(w)

print(filterdlist)

for word in tokens:
    print(stem.stem(word))