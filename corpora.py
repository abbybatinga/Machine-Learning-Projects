#accessing datasets from NLTK corpora
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

text = gutenberg.raw("blake-poems")

token = sent_tokenize(text)

for sent in range(8):
    print(token[sent]) #essentially printing first 8 tokenized sentences of text file