#!/usr/bin/python2.6

from __future__ import division

import numpy, nltk, random
from nltk.collocations import *
from ngrams import NgramUtils
from stress_and_rhyme import stressesNRhymes

#for foo, bar, baz in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # foo = ('this', 'is'), bar=('a'), baz=('nested', 'tuple')
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # f1='this', f2='is', ...
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple')), (('this', 'is'), ('another'), ('nested', 'tuple'))]

#from nltk.book import *
#import unicodedata
import re

class createLines(object):

    def __init__(self, sourcestring = ['sourcemats/caswinburne.txt']):
        self.ngrams = NgramUtils(sourcestring)
        self.tokens = self.ngrams.tokens
        self.SnR = stressesNRhymes(self.ngrams)

    def appendTokensToList(self, meter, currentword):
        returnline = []

        for i in meter:
            collocations = self.ngrams.findcollocations(currentword)
            stresslist = self.SnR.matchstresswithStress(i)
            possibleList = [w for w in collocations if stresslist.__contains__(w)]
            if len (possibleList) < 1:
                possibleList = [w for w in collocations]
            if len(possibleList) < 1:
                possibleList =[w for w in self.tokens]
            if len(possibleList) < 1:
                possibleList.append('the')
            randomnum = random.randrange(0, len(possibleList))
            returnline.append(possibleList[randomnum])
            currentword = (possibleList[randomnum])

        return returnline

    def appendTokensToListRhymeEdition(self, meter, word_to_rhyme):
        myline = self.appendTokensToList(meter, word_to_rhyme)
        myline = myline[:-1]
        lastword = myline[len(myline)-1:]
        lastmeter = meter[len(meter)-1:]
        meter = meter[:len(meter)-1]
        returnline = []

        for i in lastmeter:
            collocations = self.ngrams.findcollocations(lastword)
            stresslist = self.SnR.matchstresswithStress(i)
            rhymelist = self.SnR.findRhymes(word_to_rhyme)
            possibleList = [w for w in rhymelist if self.tokens.__contains__(w) and stresslist.__contains__(w) and collocations.__contains__(w)]
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist if self.tokens.__contains__(w) and stresslist.__contains__(w)]
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist if self.tokens.__contains__(w)]
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist]

        if len(possibleList) < 1:
            possibleList.append('the')
        randomnum = random.randrange(0, len(possibleList))
        myline.append(possibleList[randomnum])
        return " ".join(myline) + "\n"


    def createMeteredLine(self, chosenmeter):
        meter = self.getMeterList(chosenmeter)
        currentword = str(self.ngrams.pickWord())
        if currentword == '':
            currentword = self.ngrams.pickWord()
        returnline = self.appendTokensToList(meter, currentword)
        return " ".join(returnline)+ "\n"

    def createSubsequentLine(self, line, chosenmeter, isrhyming):
        tokenline = nltk.wordpunct_tokenize(line)
        if len(tokenline) > 0:
            lastword = tokenline[len(tokenline)-1:]
            lastword = str(lastword[0])
        else: lastword = ' '
        meter = self.getMeterList(chosenmeter)
        if isrhyming == False:
            returnline = self.appendTokensToList(meter, lastword)
            return " ".join(returnline)+ "\n"

        if isrhyming == True:
            return self.appendTokensToListRhymeEdition(meter, lastword)

    def getMeterList(self, choosemeter):
        meterdict = {
        'iambic': ['0', '1','0', '1','0', '1','0', '1','0', '1'],
        'dactyl' : ['1', '0', '0','1', '0', '0','1', '0', '0','1', '0', '0','1',],
        'anapest' : ['0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'],
        'somemeter' : ['0','1', '0','1', '0', '1'],
        'singleword' : random.choice((['1'], ['1','0'], ['0'], ['0','1'])),
        'randommeter' : [random.choice([0,1]) for i in range(random.randrange(18))]
        }

        returnmeter = meterdict[choosemeter]
        meter = []
        for i in range (len(returnmeter)):
            rnum = random.choice((1,1,1,2,2,2,3))
            piece = returnmeter[:rnum]
            meter.append(piece)
            del returnmeter[:rnum]

        meter = [m for m in meter if m]
        return meter
