#chunking similar words
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt") #training sample
sample_text = state_union.raw("2006-GWBush.txt") #testing sample

custom_sent_tokenizer = PunktSentenceTokenizer(train_text) #trains any body of text, passed training sample through Punkt function

tokenized = custom_sent_tokenizer.tokenize(sample_text) #pass testing sample through custom tokenizer that was trained

def content_process(): #this function will tag all parts of speech per sentence
    try:
        for word in tokenized:
            words = nltk.word_tokenize(word) #tokenizes file by word
            tagged = nltk.pos_tag(words) #tags parts of speech
            
            chunkGram = r"""Chunk: {<.*>+} 
                                }<VB.?|IN|DT>{""" #chunks by parts of speech in sentence. Arguments passed through opposite curly braces are the POS's that won't be chunked.
                                       
            
            chunkParser = nltk.RegexpParser(chunkGram) #creates a visualization of chunked data
            chunked = chunkParser.parse(tagged)
            
        print(chunked)
        for subtree in chunked.subtrees(filter= lambda t: t.label() == 'Chunk'):
            print(subtree)
            
        chunked.draw()
        
    except Exception as e:
        print(str(e))
        

print(content_process())
print(chunkGram)