from __future__ import division  	

import matplotlib, numpy, nltk, random

from nltk.book import *
from nltk.corpus import *
import unicodedata
import re


def getFileIdList(source):
    idList = []
    for fileid in source.fileids():
        idList.append(fileid)
    return idList

def plotTargetWords(source, wordlist):
    cfd = nltk.ConditionalFreqDist((target, fileid[:4])for fileid in source.fileids()for w in source.words(fileid) for target in wordlist if w.lower().startswith(target)) 
    return cfd.plot()

def generateConditionalFreqDist(source, modals):
    cfd = nltk.ConditionalFreqDist( (genre, word)for genre in source.categories()for word in source.words(categories=genre))
    genres = source.categories()
    return cfd.tabulate(conditions = genres, samples = modals)

def importFromGutenberg(url):
    raw = urlopen(url).read()
    raw = nltk.clean_html(html)
    beginning = raw.find("PART I")
    end = raw.rfind("End of Project Gutenberg")
    raw = raw[beginning:end]
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    return text

def importFromLocal(filename):
    f = open(filename)    
    raw = f.read()
    raw = raw.strip(',. ')
    raw = raw.lower()
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    return text

def importCorpus(mydir):    
    wordlists = PlaintextCorpusReader(mydir, '.*')    
    return wordlists

def importParsedCorpus(mydir, filePattern):
    corpus_root = r(mydir)
    file_pattern = r(filePattern)
    ptb = BracketParseCorpusReader(corpus_root, file_pattern)
    return ptb

def unusualWords(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)
   
def contentFraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

def concordance (text, word):
    return text.concordance(word)

def similar (text, word):
    return text.similar(word)

def commonContexts(text, word1, word2):
    return text.common_contexts([word1, word2])

def dispersionPlot(text, list):
    return text.disperson_plot(list)

def generate(text):
    return text.generate()

def length(text):
    return len(text)

def sortedSet(text):
    return sorted(set(text))

def lexicalDiversity(text): 
    return len(text)/len(set(text))

def wordCount(text, word):
    return text.count(word)

def percentage(count, total):
    return 100 * count / total

def mostCommon(text, number):
    fdist = FreqDist(text)
    vocabulary = fdist.keys()
    return vocabulary [:number]

def whatFrequency(text, word):
    fdist = FreqDist(text)
    fdist[word]

def plotMostFrequent(text, number, iscumulative):
    fdist = FreqDist(text)
    return fdist.plot(number, cumulative=iscumulative)

def viewHapaxes(text, number):
    fdist = FreqDist(text)
    hapaxes = fdist.hapaxes()
    if number == all:
        return hapaxes
    else: return hapaxes[:number]

def findLongWords(text, length):
    V = set(text)
    long_words = [w for w in V if len(w)>length]
    return sorted(long_words)

def findCommonLongWords(text, length, howCommon):
    V = set(text)
    fdist = FreqDist(text)
    long_words = [w for w in V if len(w) > length and fdist[w] > howCommon]
    return sorted(long_words)

def listCollocations(text):
    return text.collocations()

def wordLengths(text):
    fdist = FreqDist([len(w) for w in text])
    return fdist.keys()

def howManyWordsOfLength(text,length):
    fdist = FreqDist([len(w) for w in text])
    return fdist[3]

def percentageWordsOfLength(text,length):
    fdist = FreqDist([len(w) for w in text])
    frequency = fdist.freq(length)
    return frequency * 100

def searchForWordsContaining(text, containing):
    return sorted([w for w in set(text) if containing in w])

def runChatBot():
    nltk.chat.chatbots()

def generateModel(word, num, text):
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams) # [_bigram-condition]    
    for i in range(num):
        print word,
        word = cfd[word].max()
    return word

def makeAWord(letters, minimum_length):
    available_letters = nltk.FreqDist(letters)
    wordlist = nltk.corpus.words.words()
    available_words =[w for w in wordlist if len(w) >= minimum_length and nltk.FreqDist(w) <= available_letters] 
    return available_words
    
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def translate(word, lang1, lang2):
    if lang1 != 'english':
        fr2en = swadesh.entries(['fr', 'en'])
        de2en = swadesh.entries(['de', 'en'])
        es2en = swadesh.entries(['es', 'en'])
        translate = dict(fr2en)
        translate.update(dict(de2en))
        translate.update(dict(es2en))
    if lang1 == 'english':
        if lang2 == 'french':
            en2fr = swadesh.entries(['en', 'fr'])
            translate = (dict(en2fr))
        if lang2 == 'german':    
            en2de = swadesh.entries(['en', 'de'])
            translate = (dict(en2de))
        if lang2 == 'spanish':    
            en2es = swadesh.entries(['en', 'es'])
            translate = (dict(en2es))   

    return translate[word]

def findRhymes(findword):
    entries = nltk.corpus.cmudict.entries()    
    for word, pron in entries:
        if word == findword:
            mypron = pron
    returnlist = []
    for word, pron in entries:
        if pron[-2:] == mypron[-2:]:            
            returnlist.append(word)
    return returnlist        
    
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]    

def matchStress(findword):
    entries = nltk.corpus.cmudict.entries()    
    for word, pron in entries:
        if word == findword:
            mypron = pron    
    mystress = [char for phone in mypron for char in phone if char.isdigit()]
    
    returnlist = [w for w, pron in entries if stress(pron) == mystress]
    return returnlist    

def matchStressandRhyme(findword):
    rhymelist = findRhymes(findword)
    stresslist = matchStress(findword)
    returnlist = []
    for x in rhymelist:
        if stresslist.__contains__(x):
            returnlist.append(x)
    #return returnlist
    randomnum = random.randrange(0, len(returnlist))         
    return returnlist[randomnum]
    
def findSynset(word):
    synsetlist = wordnet.synsets(word)
    return str(synsetlist[0].name)

def findDefinition(word):
    synsetlist = wordnet.synsets(word)
    definitionlist = []
    for s in synsetlist:
        definitionlist.append(s.definition)
    return definitionlist

def findSynonyms(word):
    synsetlist = wordnet.synsets(word)
    synonymlist = []
    for s in synsetlist:
        synonymlist.append(s.lemma_names)
    return synonymlist

def findExamples(word):
    synsetlist = wordnet.synsets(word)
    examplelist = []
    for s in synsetlist:
        examplelist.append(s.examples)
    return examplelist

def findHyponyms(word):
    synsetlist = wordnet.synsets(word)
    thishyponym = synsetlist[0].hyponyms()
    return sorted([lemma.name for synset in thishyponym for lemma in synset.lemmas]) 

def findWordSimilarity(word1, word2):
    a = findSynset (word1)
    b = findSynset (word2)
    wordone = wordnet.synset(a)
    wordtwo = wordnet.synset(b)
    similarity = (wordone.path_similarity(wordtwo)) * 100
    return similarity

def createWordList():                   
    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
    return wordlist


#print matchStressandRhyme('nantucket')

print makeAWord('eocpf', 3)  	

"""from nltk.corpus import brown
def process(sentence):
    mylist = []
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence): 
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')): 
            mylist.append (w1 + w2 + w3)
        return mylist[:10]    
for tagged_sent in brown.tagged_sents():
    print process(tagged_sent)"""
