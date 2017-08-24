

def print_rhyme_poem(poemy_maker):
    for i in range(1):
        print ('\n'"Poem Number " + str(i + 1) )

        line1= poemy_maker.createMeteredLine('iambic')
        line2 = poemy_maker.createSubsequentLine(line1, 'iambic',False )
        line3= poemy_maker.createSubsequentLine(line2,'iambic', False)
        line4 = poemy_maker.createSubsequentLine(line3, 'dactyl', False)
        line5= poemy_maker.createSubsequentLine(line4,'iambic', True)
        line6 = poemy_maker.createSubsequentLine(line5, 'iambic',False)
        line7= poemy_maker.createSubsequentLine(line6, 'iambic',False)
        line8 = poemy_maker.createSubsequentLine(line7, 'dactyl',True)

        print ("\n" + line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + "\n")

def print_rhyme_poem_pairs(poemy_maker, originalinputstring = "red with the bitter blossom of a kiss"):

    for i in range(1):
        print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
        word = poemy_maker.ngrams.pickWord()

        inputstring =  str(word)

        inputstring = inputstring.lower()
        inputstring = inputstring.strip('.,;?-!')

        line1 = poemy_maker.createSubsequentLine(inputstring, 'iambic',False )
        line2 = poemy_maker.createSubsequentLine(line1, 'iambic',True )
        print(line1)
        print(line2)

        word = poemy_maker.ngrams.pickWord()

        inputstring = originalinputstring + " " + str(word)

        line3 = poemy_maker.createSubsequentLine(line2, 'iambic',False )
        line4 = poemy_maker.createSubsequentLine(line3, 'iambic',True)

        print(line3)
        print(line4)

        word = poemy_maker.ngrams.pickWord()



        inputstring = originalinputstring + " " + str(word)

        line5 = poemy_maker.createSubsequentLine(line4, 'iambic',False )
        line6 = poemy_maker.createSubsequentLine(line5, 'iambic',True)

        print(line5)
        print(line6)

def print_prose(poemy_maker, originalinputstring = "to thee that art a thing of barren hours"):

    for i in range(2):
        print ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
        word = poemy_maker.ngrams.pickWord()

        inputstring = str(word)

        inputstring = inputstring.lower()
        inputstring = inputstring.strip('.,;?-!')

        poem_lines = [inputstring]
        for i in range(0,5):
            poem_lines.append(poemy_maker.createSubsequentLine(poem_lines[i], 'iambic', False))
        print( " ".join(poem_lines))


def create_last_stanza(self, laststring):
    word = str(self.ngrams.pickWord())
    inputstring = word
    currentline = (self.createSubsequentLine(inputstring, 'iambic',False ))
    print (currentline)
    for i in range(5):
        templine =  (self.createSubsequentLine(currentline, 'iambic',False ))
        print (templine)
        currentline = templine
    print ("")

def outputToConsole(sourceText = ['sourcemats/caswinburne.txt']):
    from poetrygenerator import createLines
    poemy_maker = createLines(sourceText)
    originalinputstring = poemy_maker.SnR.pickLine()
    #print(poemy_maker.ngrams.generateresult('red'))
    #print_prose(poemy_maker, originalinputstring)
    print_rhyme_poem(poemy_maker)

def outputToFile(ourceText = ['sourcemats/caswinburne.txt']):
    from poetrygenerator import createLines
    poemy_maker = createLines(sourceText)
    poemoutput = open('poemoutput.txt', 'w')
    for i in range(10):
        poemoutput.write ('\n' +"Poem Number " + str(i + 1) + '\n' + '\n')
        originalinputstring = poemy_maker.SnR.pickLine()
        print_rhyme_poem(poemy_maker)
    poemoutput.close()

#outputToFile['sourcemats/swinburneshort.txt'])
outputToConsole(['sourcemats/swinburneshort.txt'])
