import nltk
import random
from nltk.collocations import *

def importFromLocal(filename):
    f = open(filename)    
    raw = f.read()
    raw.lower()      
    return raw

def buildtext():
    text = importFromLocal('sourcemats/aeondump.txt') + importFromLocal('sourcemats/curioustaleshort.txt') + importFromLocal('sourcemats/swinburne.txt') + importFromLocal('sourcemats/ninlyrics.txt')   
    #text = importFromLocal('swinburne.txt') + importFromLocal('ninlyrics.txt') + importFromLocal('neruda.txt') + importFromLocal('EAPoe.txt')+ importFromLocal('rossetti.txt') 
    text.lower()      
    return text

def findonecollocation(myword):
    text = buildtext()
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    tokens = nltk.wordpunct_tokenize(text)
    finder = BigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(1)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    scoredbigrams =  sorted(bigram for bigram, score in scored)    
    thinglist = []    
    for a,b in scoredbigrams:
        if a == myword:
            thinglist.append(b)    
    if len(thinglist) > 0:        
        if len(thinglist) > 1:
            half = len(thinglist)/2
        else: half = 1
        
        randomnum = random.randrange(0, len(thinglist))
        collocation = thinglist[randomnum]
    else: collocation = ' '   
    
    return collocation


def findcollocations(myword):
    text = buildtext()
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    #tokens = nltk.wordpunct_tokenize(text)
    finder = BigramCollocationFinder.from_words(tokens)
    #finder.apply_freq_filter(0)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    scoredbigrams =  sorted(bigram for bigram, score in scored)
    thinglist = []
    for a,b in scoredbigrams:
        if a == myword:
            thinglist.append(b)
    return thinglist

def generateresult(myword):
    buildtext()
    result = []    
    result.append(myword)
    for i in range (100):
        randomnext = findonecollocation(myword)
        result.append(randomnext)
        myword = randomnext
        
    resultstring = ''
    for i in result:
        resultstring = resultstring + i + ' '

    return resultstring

### FIND RANDOM WORD
def pickWord():
    text = buildtext()    
    tokens = nltk.wordpunct_tokenize(text)
    randomnum = random.randrange(0, len(tokens))
    word = tokens[randomnum]
    if not word.isalpha():
        randomnum = random.randrange(0, len(tokens))
        word = tokens[randomnum]    
    else:
        return word

def generateTitle(length):
    word1 = 'machine'#pickWord()
    currentword = str(word1)
    returnlist = []
    for i in range(length):
        newword = findonecollocation(str(currentword))
        returnlist.append(newword)
        currentword = newword
        
    resultstring = ''
    for word in returnlist:
        resultstring = resultstring + word + ' '
    return resultstring

for i in range(5):
    print generateTitle((random.randrange(3,9)))


#print findcollocations('the')
#for i in range(3):
#print generateresult('machine')    
#unscoredbigrams = finder.nbest(bigram_measures.pmi, 300)


