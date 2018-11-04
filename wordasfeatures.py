#turning words into features
import nltk
import random
import pickle
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC 

infoo = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)] 

random.shuffle(infoo)

complete = []

for word in movie_reviews.words():
    complete.append(word.lower()) #appends words in reviews in lowercase

complete = nltk.FreqDist(complete)

wordfeatures = list(complete.keys())[:2000] #this list will store top 2000 most common words

#function will find top 2000 most common words in pos and neg and label them as pos or neg
def find_features(text):
    wordz = set(text)
    features = {} #dictionary to store key as word and value as pos or neg 
    for w in wordz: #accessing elements of list of words in text document
        features[w] = (w in wordz) #defining keys in dictionary as the words in the document text
    
    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt')))) #prints all the words in that review are associated with the negative future

featuresets = [(find_features(rev), category) for (rev, category) in infoo]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

#posterior = prior occurences x likelihood / current evidence = naive bayes

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Naive Bayes Algorithm accuracy:", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(20)

save_classifier = open("naivebayes.pickle", "wb") #writes a new file to store the classifier as an object
pickle.dump(classifier, save_classifier)
save_classifier.close()

classifier_f = open("naivebayes.pickle", "rb") #opens file and reads in bytes
classifier = pickle.load(classifier_f) #loads data and saves it in classifier file
classifier_f.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

bern_classifier = SklearnClassifier(BernoulliNB())
bern_classifier.train(training_set)
print("Bern_classifier Algorithm Accuracy:", (nltk.classify.accuracy(bern_classifier, testing_set))*100)