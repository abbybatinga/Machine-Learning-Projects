#building a classifier for dataset
import nltk
import random
from nltk.corpus import movie_reviews

infoo = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)] 
#takes the IDs of each review and prints "category of review"(pos or neg) in a list next to review, also this is tokenized version
random.shuffle(infoo) #shuffling data to train both positive and negative

print(infoo[1]) #prints first document

complete = []
for word in movie_reviews.words():
    complete.append(word.lower()) #adds all words in the dataset to a list

complete = nltk.FreqDist(complete)
print(complete.most_common(10)) #prints out 10 most frequent words and their frequency
print(complete["good"]) #prints frequency of one specific word