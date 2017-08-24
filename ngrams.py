import nltk
import random
from nltk.collocations import *
from nltk.metrics.association import *

class NgramUtils(object):

    def __init__(self, sourcestring):
        self.text = self.buildtext(sourcestring)
        self.tokens = self.prepareTokens(self.text)

    def importFromLocal(self, filename):
        f = open(filename, encoding="utf-8")
        raw = f.read()
        raw.lower()
        return raw

    def buildtext(self, sourcestring):
        text = ' '.join([self.importFromLocal(s) for s in sourcestring])
        return text

    def removeThingsFromList(self, possibleList):
        list_with_things_removed = possibleList
        removeList = ['"'"", '.', ',','.', ';','!']
        for i in removeList:
            if list_with_things_removed.__contains__(i):
                list_with_things_removed.remove(i)
        return list_with_things_removed

    def prepareTokens(self, text):
        tokens = nltk.wordpunct_tokenize(text)
        return tokens

    def buildCollocationsList(self, myword, scored_ngrams):
        collocationslist = []
        for element in scored_ngrams:
            if element[0] == myword:
                for word in element[1:]:
                    collocationslist.append(word)
        return collocationslist

    def assocMeasuresSwitcher(self, number_of_grams):
        function_list = [BigramAssocMeasures, TrigramAssocMeasures, QuadgramAssocMeasures]
        return function_list[number_of_grams - 2]

    def finderSwitcher(self, number_of_grams):
        function_list = [BigramCollocationFinder.from_words, TrigramCollocationFinder.from_words, QuadgramCollocationFinder.from_words]
        return function_list[number_of_grams -2]

    def buildScoredNgramsList(self, myword, number_of_grams):
        ngram_measures_func = self.assocMeasuresSwitcher(number_of_grams)
        ngram_measures = ngram_measures_func()
        finder_func = self.finderSwitcher(number_of_grams)
        finder = finder_func(self.tokens, window_size=4)
        finder.apply_freq_filter(2)
        scored = finder.score_ngrams(ngram_measures.raw_freq)
        return  sorted(ngram for ngram, score in scored)

    def findcollocations(self, myword, number_of_grams = 2):
        scoredNgrams =  self.buildScoredNgramsList(myword, number_of_grams)
        return self.buildCollocationsList(myword, scoredNgrams)

    def findonecollocation(self, myword):
        thinglist = self.findcollocations(myword)
        if len(thinglist) > 0:
            randomnum = random.randrange(0, len(thinglist))
            collocation = thinglist[randomnum]
        else: collocation = ' '

        return collocation

    def generateresult(self, myword):
        result = []
        result.append(myword)
        for i in range (100):
            randomnext = self.findonecollocation(myword)
            result.append(randomnext)
            myword = randomnext

        resultstring = ''
        for i in result:
            resultstring = resultstring + i + ' '

        return resultstring

    ### FIND RANDOM WORD
    def pickWord(self):
        randomnum = random.randrange(0, len(self.tokens))
        word = self.tokens[randomnum]
        if not word.isalpha():
            randomnum = random.randrange(0, len(self.tokens))
            word = self.tokens[randomnum]
        else:
            return word

    def generateTitle(self, length):
        word1 = self.pickWord()
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

# for i in range(5):
#     print (generateTitle(random.randrange(3,9)))


#print (findcollocations('the'))

# for i in range(0,3):
#     print (generateresult('the'))
#unscoredQuadgrams = finder.nbest(Quadgram_measures.pmi, 300)
