#!/usr/bin/python2.6

from __future__ import division

import numpy, nltk, random
from nltk.collocations import *
from ngrams import NgramUtils

#for foo, bar, baz in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # foo = ('this', 'is'), bar=('a'), baz=('nested', 'tuple')
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # f1='this', f2='is', ...
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple')), (('this', 'is'), ('another'), ('nested', 'tuple'))]

#from nltk.book import *
#import unicodedata
import re

class makeABigHeckinPoem(object):

    def __init__(self):
        self.ngrams = NgramUtils()
        self.tokens = self.ngrams.tokens
        self.entries = nltk.corpus.cmudict.entries()

    def findRhymes(self, findword):
        mypron = ''
        mypron = [pron for pron, word in self.entries if findword == word]
        # for word, pron in self.entries:
        #     if word == findword:
        #         mypron = pron
        returnlist = []

        for word, pron in self.entries:
            if len(pron) > 2:
                if pron[-2:] == mypron[-2:] and pron[-1:] == mypron[-1:]:
                    returnlist.append(word)
            else:
                if pron[-1:] == mypron[-1:]:
                    returnlist.append(word)
        returnlist.append(findword)
        return returnlist


    def findOneRhyme(self, findword, collocations):
        usualtext = collocations

        for word, pron in self.entries:
            if word == findword:
                mypron = pron

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

        returnlist = []

        returnlist = [w for w, pron in self.entries if self.stress(pron) == mystress]

        return returnlist

    def matchstresswithWord(self, word):
        findword = word
        mypron = ''
        for word, pron in self.entries:
            if word == findword:
                mypron = pron
        mystress = [char for phone in mypron for char in phone if char.isdigit()]

        returnlist = []

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

    def removeThingsFromList(possibleList):
        list_with_things_removed = possibleList
        removeList = ['ve', 'an', 's', 'ha', 'th', 'ourselves', 'desecrate', 'overhead', 'engineers', 'overhead', "'", '.', ',','.', ';','Elfonzo','Ambulinia','!']
        for i in removeList:
            if list_with_things_removed.__contains__(i):
                list_with_things_removed.remove(i)
        return list_with_things_removed


    ### PICK INITIAL LINE
    def pickLine():
        linelist = ngrams.text.splitlines()
        randomnum = random.randrange(0, len(linelist))
        return linelist[randomnum]

    def appendTokensToList(self, meter, currentword):
        #possibleList = []
        returnline = []
        for i in meter:
            collocations = self.ngrams.findcollocations(currentword)
            stresslist = self.matchstresswithStress(i)

            possibleList = [w for w in collocations if stresslist.__contains__(w)]

            if len (possibleList) < 1:
                possibleList = [w for w in collocations]

            if len(possibleList) < 1:
                possibleList =[w for w in self.tokens if stresslist.__contains__(w)]

            if len(possibleList) < 1:
                possibleList =[w for w in self.tokens]

            #possibleList = removeThingsFromList(possibleList)

            if len(possibleList) < 1:
                possibleList.append('the')
            randomnum = random.randrange(0, len(possibleList))
            returnline.append(possibleList[randomnum])

            currentword = (possibleList[randomnum])

        return possibleList


    def createMeteredLine(self, choosemeter):
        meter = self.getMeterList(choosemeter)
        returnline = []
        #currentword = 'love'
        currentword = str(self.ngrams.pickWord())

        if currentword == '':
            currentword = self.ngrams.pickWord()
        else: pass
        #print currentword
        possibleList = []

        for i in meter:
            collocations = self.ngrams.findcollocations(currentword)
            stresslist = self.matchstresswithStress(i)
            possibleList = [w for w in collocations if stresslist.__contains__(w)]

            if len (possibleList) < 1:
                possibleList = [w for w in collocations]

            if len(possibleList) < 1:
                possibleList =[w for w in self.tokens if stresslist.__contains__(w)]

            if len(possibleList) < 1:
                possibleList =[w for w in self.tokens]

            #possibleList = removeThingsFromList(possibleList)

            if len(possibleList) < 1:
                possibleList.append('the')
            randomnum = random.randrange(0, len(possibleList))
            returnline.append(possibleList[randomnum])

            currentword = (possibleList[randomnum])

        return " ".join(returnline)
        # poemstring = ''
        # for word in returnline:
        #     poemstring = poemstring + word + ' '
        #
        # return poemstring

    def createSubsequentLine(self, line, choosemeter, isrhyming):
        tokenline = nltk.wordpunct_tokenize(line)
        if len(tokenline) > 0:
            lastword = tokenline[len(tokenline)-1:]
            lastword = str(lastword[0])
        else: lastword = ' '
        currentword = lastword
        #returnline = []
        meter = self.getMeterList(choosemeter)
        if isrhyming == True:
            lastmeter = meter[len(meter)-1:]
            meter = meter[:len(meter)-1]
        else: pass
        possibleList = self.appendTokensToList(meter, currentword)
        # for i in meter:
        #     collocations = self.ngrams.findcollocations(currentword)
        #     stresslist = self.matchstresswithStress(i)
        #
        #     possibleList = [w for w in collocations if stresslist.__contains__(w)]
        #
        #     if len (possibleList) < 1:
        #         possibleList = [w for w in collocations]
        #
        #     if len(possibleList) < 1:
        #         possibleList =[w for w in self.tokens if stresslist.__contains__(w)]
        #
        #     if len(possibleList) < 1:
        #         possibleList =[w for w in self.tokens]
        #
        #     #possibleList = removeThingsFromList(possibleList)
        #
        #     if len(possibleList) < 1:
        #         possibleList.append('the')
        #     randomnum = random.randrange(0, len(possibleList))
        #     returnline.append(possibleList[randomnum])
        #
        #     currentword = (possibleList[randomnum])

        if isrhyming == True:
            for i in lastmeter:
                collocations = self.ngrams.findcollocations(currentword)
                self.stresslist = self.matchstresswithStress(i)

                rhymelist = self.findRhymes(lastword)
                possibleList = [w for w in rhymelist if self.tokens.__contains__(w) and stresslist.__contains__(w) and collocations.__contains__(w)]
                if len(possibleList) < 3:
                    possibleList = [w for w in rhymelist if self.tokens.__contains__(w) and stresslist.__contains__(w)]

                if len(possibleList) < 3:
                    possibleList = [w for w in rhymelist if self.tokens.__contains__(w)]
                if len(possibleList) < 3:
                    possibleList = [w for w in rhymelist]

            #possibleList = removeThingsFromList(possibleList)

            if len(possibleList) < 1:
                possibleList.append('the')
            randomnum = random.randrange(0, len(possibleList))
            returnline.append(possibleList[randomnum])

        return " ".join(returnline) + "\n"
        # poemstring = ''
        # for word in returnline:
        #     poemstring = poemstring + word + ' '
        #
        # return poemstring + "\n"


    def getMeterList(self, choosemeter):

        meterdict = {'iambic': ['0', '1','0', '1','0', '1','0', '1','0', '1'],
        'dactyl' : ['1', '0', '0','1', '0', '0','1', '0', '0','1', '0', '0','1',],
        'anapest' : ['0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'],
        'somemeter' : ['0','1', '0','1', '0', '1'],
        'singleword' : random.choice((['1'], ['1','0'], ['0'], ['0','1'])),
        'randommeter' : [random.choice([0,1]) for i in range(random.randrange(18))]}

        returnmeter = meterdict[choosemeter]
        meter = []
        for i in range (len(returnmeter)):
            rnum = random.choice((1,1,1,2,2,2,3))
            #rnum = random.choice((0,1,2,3))

            piece = returnmeter[:rnum]

            meter.append(piece)
            del returnmeter[:rnum]

        for i in range(10):
            try:
                meter.remove([])
            except: pass

        return meter


    def print_rhyme_poem(self):
        for i in range(4):
            print ('\n'"Poem Number " + str(i + 1) )

            line1= self.createMeteredLine('iambic')
            line2 = self.createSubsequentLine(line1, 'iambic',False )
            line3= self.createSubsequentLine(line2,'iambic', False)
            line4 = self.createSubsequentLine(line3, 'dactyl', True)
            line5= self.createSubsequentLine(line4,'iambic', False)
            line6 = self.createSubsequentLine(line5, 'iambic',False)
            line7= self.createSubsequentLine(line6, 'iambic',False)
            line8 = self.createSubsequentLine(line7, 'dactyl',True)

            print ("\n" + line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + "\n")

    def print_rhyme_poem_pairs():

        for i in range(1):
            print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
            originalinputstring = pickLine()
            word = self.ngrams.pickWord()

            originalinputstring = "red with the bitter blossom of a kiss"
            #originalinputstring = "to thee that art a thing of barren hours"
            #originalinputstring = "i can leave all this flesh behind"
            inputstring =  str(word)

            inputstring = inputstring.lower()
            inputstring = inputstring.strip('.,;?-!')

            line1 = self.createSubsequentLine(inputstring, 'iambic',False )
            line2 = self.createSubsequentLine(line1, 'iambic',True )
            print(line1)
            print(line2 )

            word = self.ngrams.pickWord()

            inputstring = originalinputstring + " " + str(word)

            line3 = self.createSubsequentLine(line2, 'iambic',False )
            line4 = self.createSubsequentLine(line3, 'iambic',True)

            print(line3)
            print(line4)

            word = self.ngrams.pickWord()



            inputstring = originalinputstring + " " + str(word)

            line5 = self.createSubsequentLine(line4, 'iambic',False )
            line6 = self.createSubsequentLine(line5, 'iambic',True)

            print(line5)
            print(line6)

    def print_prose():

        for i in range(2):
            print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
            originalinputstring = pickLine()
            word = self.ngrams.pickWord()

            #originalinputstring = "red with the bitter blossom of a kiss"
            #originalinputstring = "to thee that art a thing of barren hours"
            #originalinputstring = "i can leave all this flesh behind"
            inputstring = str(word)

            inputstring = inputstring.lower()
            inputstring = inputstring.strip('.,;?-!')

            poem_lines = [inputstring]
            for i in range(0,5):
                poem_lines.append(createSubsequentLine(poem_lines[i], 'iambic', False))
            print( " ".join(poem_lines))


    def create_last_stanza(self, laststring):
        word = self.ngrams.pickWord()
        inputstring = word
        currentline = (createSubsequentLine(inputstring, 'iambic',False ))
        print (currentline)
        for i in range(5):
            templine =  (createSubsequentLine(currentline, 'iambic',False ))
            print (templine)
            currentline = templine
        print ("")

#print_prose()
if __name__ == "__main__":
    poemy_maker = makeABigHeckinPoem()
    poemy_maker.print_rhyme_poem()
    laststring = ''
    poemy_maker.create_last_stanza(laststring)


# poemoutput = open('poemoutput2.txt', 'w')

# for i in range(10):
#     poemoutput.write ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
#     originalinputstring = pickLine()
#
#
#     word = ngrams.pickWord()
#
#
#     originalinputstring = "red with the bitter blossom of a kiss"
#     #originalinputstring = "to thee that art a thing of barren hours"
#     #originalinputstring = "i can leave all this flesh behind"
#
#     inputstring = originalinputstring + " " + str(word)
#
#
#
#     inputstring = inputstring.lower()
#     inputstring = inputstring.strip('.,;?-!')
#
#
#
#     line1 = poemOutput(inputstring)
#     line2 = poemOutput(line1)
#
#     poemoutput.write(line1 + '\n')
#     poemoutput.write(line2 + '\n')
#
#
#     word = ngrams.pickWord()
#
#
#
#     inputstring = originalinputstring + " " + str(word)
#
#     line3 = poemOutput(line2)
#     line4 = poemOutput(line3)
#
#     poemoutput.write(line3 + '\n')
#     poemoutput.write(line4 + '\n')
#
#     word = ngrams.pickWord()
#
#
#
#     inputstring = originalinputstring + " " + str(word)
#
#     line5 = poemOutput(line4)
#     line6 = poemOutput(line5)
#
#     poemoutput.write(line5 + '\n')
#     poemoutput.write(line6 + '\n')
#
# poemoutput.close()
