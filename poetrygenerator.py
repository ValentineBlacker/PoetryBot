#!/usr/bin/python2.6

from __future__ import division  	

import numpy, nltk, random
from nltk.collocations import *

#for foo, bar, baz in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # foo = ('this', 'is'), bar=('a'), baz=('nested', 'tuple')
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple'))]: # f1='this', f2='is', ...
#for (f1, f2), f3, (f4, f5) in [(('this', 'is'), ('a'), ('nested', 'tuple')), (('this', 'is'), ('another'), ('nested', 'tuple'))]



#from nltk.book import *
from nltk.corpus import *
import unicodedata
import re


#### IMPORT TEXT STRING
def importFromLocal(filename):
    f = open(filename)    
    raw = f.read()
    raw.lower()      
    return raw

def buildtext():
    textlist = [importFromLocal('sourcemats/aeondump.txt') , importFromLocal('sourcemats/curioustaleshort.txt') , importFromLocal('sourcemats/swinburne.txt') , importFromLocal('sourcemats/ninlyrics.txt')]
    text = ""
    text = text.join(textlist)
    text = text.decode('latin1')
    #text = importFromLocal('sourcemats/aeondump.txt') + importFromLocal('sourcemats/curioustaleshort.txt') + importFromLocal('sourcemats/swinburne.txt') + importFromLocal('sourcemats/ninlyrics.txt')    
    #text = importFromLocal('swinburne.txt') + importFromLocal('ninlyrics.txt') + importFromLocal('neruda.txt') + importFromLocal('EAPoe.txt')+ importFromLocal('rossetti.txt') + importFromLocal('emotionalpoetry.txt')+ importFromLocal('curioustaleshort.txt')
    #text = text.lower()
    
    return text

usualtext = buildtext()
tokens = nltk.wordpunct_tokenize(usualtext)

entries = nltk.corpus.cmudict.entries()

#### FIND COLLOCATIONS
def findcollocations(myword):    
    bigram_measures = nltk.collocations.BigramAssocMeasures()    
    finder = BigramCollocationFinder.from_words(tokens)
    #finder.apply_freq_filter(0)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    scoredbigrams =  sorted(bigram for bigram, score in scored)
    thinglist = []
    for a,b in scoredbigrams:
        if a == myword:
            thinglist.append(b)
    return thinglist


#MATCH STRESS AND RHYME

    
def findRhymes(findword):
    
    
    mypron = ''
    for word, pron in entries:
        if word == findword:
            mypron = pron
            
    returnlist = []    
        
    for word, pron in entries:
        if len(pron) > 2:                
            if pron[-2:] == mypron[-2:] and pron[-1:] == mypron[-1:]:            
                returnlist.append(word)
        else:                
            if pron[-1:] == mypron[-1:]:           
                returnlist.append(word)
            
    returnlist.append(findword)
      
    return returnlist        
    

def findOneRhyme(findword, collocations):
    usualtext = collocations    
        
    for word, pron in entries:
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

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]    

def matchstresswithStress(mystress):   
   
    returnlist = []    
    
    returnlist = [w for w, pron in entries if stress(pron) == mystress] 
      
    return returnlist

def matchstresswithWord(word):
    findword = word
    mypron = ''
    for word, pron in entries:
        if word == findword:
            mypron = pron
    mystress = [char for phone in mypron for char in phone if char.isdigit()]
    
    returnlist = []    
       
    returnlist = [w for w, pron in entries if stress(pron) == mystress]
    returnlist.append(findword)
    return returnlist
    
def findOneStress(mystress):
    
          
    #mystress = [char for phone in mypron for char in phone if char.isdigit()]
    #print mystress
    returnlist = []    

       
    returnlist = [w for w, pron in entries if stress(pron) == mystress]
    #returnlist.append(findword)
        
    randomnum = random.randrange(0, len(returnlist))
    
    return returnlist[randomnum]

def matchStressandRhyme(findword):
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
def pickLine():
    linelist = usualtext.splitlines()
    randomnum = random.randrange(0, len(linelist))
    return linelist[randomnum]

### FIND RANDOM WORD
def pickWord():
    randomnum = random.randrange(0, len(tokens))
    word = tokens[randomnum]
    if not word.isalpha():
        randomnum = random.randrange(0, len(tokens))
        word = tokens[randomnum]    
    else:
        return word
    
### MY DERPLER

def myDerpler(line):
### PRINT OUTPUT
    returnline = []
    rawline = line
    tokenline = tokens = nltk.wordpunct_tokenize(rawline)      
    #currentword = tokenline[0]
    for w in tokenline:
        collocation = bigrams.findonecollocation(w)
        returnline.append(collocation)

    poemstring = ''
    for word in returnline:
        poemstring = poemstring + word + ' '                 
    
    return poemstring

def createSubsequentLine(line, choosemeter, isrhyming):
    tokenline = nltk.wordpunct_tokenize(line)      
    if len(tokenline) > 0:
        lastword = tokenline[len(tokenline)-1:]
        lastword = str(lastword[0])
    else: lastword = ' '
    currentword = lastword    
    returnline = []
    meter = getMeterList(choosemeter)
    if isrhyming == True:
        lastmeter = meter[len(meter)-1:] 
        meter = meter[:len(meter)-1]
    else: pass
    possibleList = []
    for i in meter:
        collocations = findcollocations(currentword)       
        stresslist = matchstresswithStress(i)   
       
        possibleList = [w for w in collocations if stresslist.__contains__(w)]    
                
                   
        if len (possibleList) < 1:
            
            possibleList = [w for w in collocations]

        if len(possibleList) < 1:
            
            possibleList =[w for w in tokens if stresslist.__contains__(w)]

        if len(possibleList) < 1:
            
            possibleList =[w for w in tokens]
            
        
        
        removeList = ['ve', 'an', 's', 'ha', 'th', 'ourselves', 'desecrate', 'overhead', 'engineers', 'overhead', "'", '.', ',','.', ';','Elfonzo','Ambulinia','!']
        for i in removeList:
            if possibleList.__contains__(i):                
                possibleList.remove(i)
        if len(possibleList) < 1:
            possibleList.append('the')
        randomnum = random.randrange(0, len(possibleList))
        returnline.append(possibleList[randomnum])
        
        currentword = (possibleList[randomnum])
       
    if isrhyming == True:    
        for i in lastmeter:
            collocations = findcollocations(currentword)  
            stresslist = matchstresswithStress(i)
                  
            rhymelist = findRhymes(lastword)
            possibleList = [w for w in rhymelist if tokens.__contains__(w) and stresslist.__contains__(w) and collocations.__contains__(w)]
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist if tokens.__contains__(w) and stresslist.__contains__(w)]
                
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist if tokens.__contains__(w)]
            if len(possibleList) < 3:
                possibleList = [w for w in rhymelist]
        
        removeList = ['ve', 'an', 's', 'ha', 'th', 'ourselves', 'desecrate', 'overhead', 'engineers', 'overhead', "'", '.', ',','.', ';','elfonzo','ambulinia','!']
        for i in removeList:
            if possibleList.__contains__(i):                
                possibleList.remove(i)
        
        if len(possibleList) < 1:
            possibleList.append('the')         
        randomnum = random.randrange(0, len(possibleList))
        returnline.append(possibleList[randomnum])        
        
                
    poemstring = ''
    for word in returnline:
        poemstring = poemstring + word + ' '                 
     
    return poemstring


def createMeteredLine(choosemeter):
    meter = getMeterList(choosemeter)
    returnline = []
    #currentword = 'love'
    currentword = str(pickWord())
    
    if currentword == '':
        currentword = pickWord()
    else: pass
    #print currentword
    possibleList = []
    
    for i in meter:
        
        collocations = findcollocations(currentword)
                           
       
        stresslist = matchstresswithStress(i)
        
       
        possibleList = [w for w in collocations if stresslist.__contains__(w)]
        
        
        
                    
        if len (possibleList) < 1:
            
            possibleList = [w for w in collocations]

        if len(possibleList) < 1:
            
            possibleList =[w for w in tokens if stresslist.__contains__(w)]
        if len(possibleList) < 1:
            
            possibleList =[w for w in tokens]    
        
        removeList = ['ve', 'an', 's', 'ha', 'th', 'ourselves', 'desecrate', 'overhead', 'engineers', 'overhead', "'", '.', ',', ';','elfonzo','ambulinia','!']
        for i in removeList:
            if possibleList.__contains__(i):                
                possibleList.remove(i)
        if len(possibleList) < 1:
            possibleList.append('the')         
        randomnum = random.randrange(0, len(possibleList))
        returnline.append(possibleList[randomnum])
        
        currentword = (possibleList[randomnum])     
       
       
      
    poemstring = ''
    for word in returnline:
        poemstring = poemstring + word + ' '                 
     
    return poemstring



def getMeterList(choosemeter):
    
    iambic = ['0', '1','0', '1','0', '1','0', '1','0', '1']
    dactyl = ['1', '0', '0','1', '0', '0','1', '0', '0','1', '0', '0','1',]
    anapest = ['0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1']
    somemeter = ['0','1', '0','1', '0', '1']
    singleword = random.choice((['1'], ['1','0'], ['0'], ['0','1']))
    randommeter = []     
    for i in range(random.randrange(18)):
        randommeter.append(random.choice((0,1)))
        
    currentmeter = choosemeter
    returnmeter = []
    if currentmeter == 'random':
        returnmeter = randommeter
    elif currentmeter== 'iambic':
        returnmeter = iambic
    elif currentmeter== 'dactyl':
        returnmeter = dactyl
    elif currentmeter== 'anapest':
        returnmeter = anapest
    elif currentmeter== 'custom':
        returnmeter = somemeter
    elif currentmeter== 'singleword':
        returnmeter = singleword
    elif currentmeter== ' ':
        returnmeter = iambic
    else: returnmenter = iambic
    #currentmeter = iambic#random.choice((iambic, dactyl, anapest))
    
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


def print_rhyme_poem():
    for i in range(4):           
        print ('\n'"Poem Number " + str(i + 1) )
        
        line1= createMeteredLine('iambic')
        line2 = createSubsequentLine(line1, 'iambic',False )
        line3= createSubsequentLine(line2,'iambic', False)
        line4 = createSubsequentLine(line3, 'dactyl', True)
        line5= createSubsequentLine(line4,'iambic', False)
        line6 = createSubsequentLine(line5, 'iambic',False)
        line7= createSubsequentLine(line6, 'iambic',False)
        line8 = createSubsequentLine(line7, 'dactyl',True)
        
        print "\n"
        print line1
        print line2
        print line3
        print line4    
        print line5
        print line6
        print line7
        print line8
        print "\n"




def print_rhyme_poem_pairs():

    for i in range(1):
        print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
        originalinputstring = pickLine()
        word = pickWord()
    
        originalinputstring = "red with the bitter blossom of a kiss"
        #originalinputstring = "to thee that art a thing of barren hours"
        #originalinputstring = "i can leave all this flesh behind"
        inputstring =  str(word)
    
        inputstring = inputstring.lower()
        inputstring = inputstring.strip('.,;?-!')
    
        line1 = createSubsequentLine(inputstring, 'iambic',False )
        line2 = createSubsequentLine(line1, 'iambic',True )
        print(line1)
        print(line2 )    
    
        word = pickWord()      
    
        inputstring = originalinputstring + " " + str(word)
    
        line3 = createSubsequentLine(line2, 'iambic',False )
        line4 = createSubsequentLine(line3, 'iambic',True)
    
        print(line3)
        print(line4)
    
        word = pickWord()
    
          
    
        inputstring = originalinputstring + " " + str(word)
    
        line5 = createSubsequentLine(line4, 'iambic',False )
        line6 = createSubsequentLine(line5, 'iambic',True)
    
        print(line5)
        print(line6)

def print_prose():
    
    for i in range(2):
        print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
        originalinputstring = pickLine()
        word = pickWord()
    
        #originalinputstring = "red with the bitter blossom of a kiss"
        #originalinputstring = "to thee that art a thing of barren hours"
        #originalinputstring = "i can leave all this flesh behind"
        inputstring = str(word)
    
        inputstring = inputstring.lower()
        inputstring = inputstring.strip('.,;?-!')
    
        line1 = createSubsequentLine(inputstring, 'iambic',False )
        line2 = createSubsequentLine(line1, 'iambic',False )
        line3 = createSubsequentLine(line2, 'iambic',False )
        line4 = createSubsequentLine(line3, 'iambic',False )
        line5 = createSubsequentLine(line4, 'iambic',False )
        line6 = createSubsequentLine(line5, 'iambic',False )
        line7 = createSubsequentLine(line6, 'iambic',False )
        line8 = createSubsequentLine(line7, 'iambic',False )
        print(line1)
        print(line2 )  
        print(line3 )
        print(line4 )
        print(line5 )
        print(line6 )
        print(line7)
        print(line8)
        

print_rhyme_poem() 
    
laststring = ''

def create_paradelle(inputstring, laststring):
    
    lineA = createSubsequentLine(inputstring, 'iambic',False )
    lineB = createSubsequentLine(lineA, 'iambic',False )
    
    linetemp = lineA + lineB
    tokenz = nltk.wordpunct_tokenize(linetemp)
    
            
    tokenline = tokenz
    random.shuffle(tokenline)
       
    
    halfway = int(len(tokenline)/2)
    
    tokenline1 = tokenline[0:halfway]
    tokenline2 = tokenline[halfway:]
    
    
    lineC = ''
    for word in tokenline1:
        lineC = lineC + word + ' ' 
        
    lineD = ''
    for word in tokenline2:
        lineD = lineD + word + ' ' 
    inputstring = lineD
    
    laststring =  lineA + lineB + lineC + lineD
   
    
    print (lineA)
    print (lineA)    
    print (lineB)
    print (lineB)
    print (lineC)
    print (lineD)
    print ""
     
    return laststring    
        


"""laststring = ''
for i in range(3):
    word = pickWord()
    inputstring = word
    templaststring = create_paradelle(inputstring, laststring)
    laststring = laststring + templaststring + ""
    
    
usualtext = laststring
tokens = nltk.wordpunct_tokenize(usualtext)

    
def create_last_stanza(laststring)   :
    word = pickWord()
    inputstring = word 
    currentline = (createSubsequentLine(inputstring, 'iambic',False ))
    print currentline
    for i in range(5):        
        templine =  (createSubsequentLine(currentline, 'iambic',False ))
        print templine
        currentline = templine
    print ""
   



create_last_stanza(laststring)
        



poemoutput = open('poemoutput.txt', 'w')

for i in range(10):
    poemoutput.write ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
    originalinputstring = pickLine()


    word = pickWord()


    #originalinputstring = "red with the bitter blossom of a kiss"
    #originalinputstring = "to thee that art a thing of barren hours"
    #originalinputstring = "i can leave all this flesh behind"

    inputstring = originalinputstring + " " + str(word)



    inputstring = inputstring.lower()
    inputstring = inputstring.strip('.,;?-!')



    line1 = poemOutput(inputstring)
    line2 = poemOutput(line1)

    poemoutput.write(line1 + '\n')
    poemoutput.write(line2 + '\n')
    

    word = pickWord()

      

    inputstring = originalinputstring + " " + str(word)

    line3 = poemOutput(line2)
    line4 = poemOutput(line3)

    poemoutput.write(line3 + '\n')
    poemoutput.write(line4 + '\n')

    word = pickWord()

      

    inputstring = originalinputstring + " " + str(word)

    line5 = poemOutput(line4)
    line6 = poemOutput(line5)

    poemoutput.write(line5 + '\n')
    poemoutput.write(line6 + '\n')

poemoutput.close()"""
