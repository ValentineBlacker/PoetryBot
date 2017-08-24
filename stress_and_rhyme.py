#!/usr/bin/python2.6
import nltk, random

class stressesNRhymes(object):

    def __init__(self, ngrams):
        self.ngrams = ngrams
        self.entries = nltk.corpus.cmudict.entries()

    def findRhymes(self, findword):
        mypron = [pron for word,pron in self.entries if findword == word]
        returnlist = []
        if len(mypron) >0:
            mypron = mypron[0]
            for word, pron in self.entries:
                if len(pron) > 2:
                    if pron[-2:] == mypron[-2:]:
                        returnlist.append(word)
                else:
                    if pron[-1] == mypron[-1]:
                        returnlist.append(word)
        return returnlist


    def findOneRhyme(self, findword, collocations):
        usualtext = collocations

        mypron = [pron for word,pron in self.entries if findword == word]
        if len(mypron) >0:
            mypron = mypron[0]

        returnlist = []
        for word, pron in entries:
            #if len(pron) > 2:
            if pron[-2:] == mypron[-2:] and usualtext.__contains__(word):
                returnlist.append(word)
            #else:
            if pron[-1:] == mypron[-1:] and usualtext.__contains__(word):
                returnlist.append(word)

        returnlist.append(findword)
        randomnum = random.randrange(0, len(returnlist))

        return returnlist[randomnum]

    def stress(self, pron):
        return [char for phone in pron for char in phone if char.isdigit()]

    def matchstresswithStress(self, mystress):
        returnlist = [w for w, pron in self.entries if self.stress(pron) == mystress]
        return returnlist

    def matchstresswithWord(self, word):
        findword = word
        mypron = ''
        for word, pron in self.entries:
            if word == findword:
                mypron = pron
        mystress = [char for phone in mypron for char in phone if char.isdigit()]
        returnlist = [w for w, pron in self.entries if stress(pron) == mystress]
        returnlist.append(findword)
        return returnlist

    def findOneStress(self, mystress):

        #mystress = [char for phone in mypron for char in phone if char.isdigit()]
        #print mystress
        returnlist = []
        returnlist = [w for w, pron in self.entries if stress(pron) == mystress]
        #returnlist.append(findword)
        randomnum = random.randrange(0, len(returnlist))

        return returnlist[randomnum]

    def matchStressandRhyme(self, findword):
        rhymelist = findRhymes(findword)
        stresslist = matchStress(findword)
        returnlist = []
        for x in rhymelist:
            if stresslist.__contains__(x):
                returnlist.append(x)
        randomnum = random.randrange(0, len(returnlist))
        returnlist.append(findword)
        return returnlist[randomnum]

    ### PICK INITIAL LINE
    def pickLine(self):
        linelist = self.ngrams.text.splitlines()
        randomnum = random.randrange(0, len(linelist))
        return linelist[randomnum]
