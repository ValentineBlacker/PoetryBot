import nltk, re, pprint

def importFromLocal(filename):
    f = open(filename)    
    raw = f.read()
    raw.lower()      
    return raw

def buildtext():    
    text = importFromLocal('qualified.txt')
    text.lower()      
    return text
 	
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) 
    sentences = [nltk.word_tokenize(sent) for sent in sentences] 
    sentences = [nltk.pos_tag(sent) for sent in sentences]    
    return sentences

def find_chunks(sentences, chunk):
    returnlist = []
    for sent in sentences:
        cp = nltk.RegexpParser(chunk)
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'CHUNK':
                returnlist.append(subtree)
    return returnlist[0:20]
    
#every sentence is a list in the sentences list
document = buildtext()
sentences = ie_preprocess(document)


 	
grammar = """
    NP:{<NNP>+} # chunk sequences of proper nouns
    {<DT|PP\$>?<JJ>*<NN>}# chunk determiner/possessive, adjectives and nouns
    """
chunk =  "CHUNK: {<V.*> <TO> <V.*>}"
print find_chunks(sentences, chunk)

