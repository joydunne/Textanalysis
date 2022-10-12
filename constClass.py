class constText:
    '''Analyze texts using stats and such.'''
    def __init__ (self, filename): #initializing my class 
        self.filename = filename 
        with open(self.filename) as f:
            self.lines = f.readlines()

    def fileLength(self):
        n = 0 
        for line in self.lines:
            line = line.strip()
            print (line, len(line))
            if line != '':   #'' means an empty string 
                n = n + 1 # n is called a counter 
        return (n) 

    def stanzaCount(self): 
        n = 0 
        for line in self.lines:
            line = line.strip()
            if line == '':
                n = n + 1
            c = n + 1 
        return c 
    
    def religiousWords (self, word):
        n = 0 #counter
        r = []
        self.getSentences()
        for s in self.sentences:
            if word  in s:
                n += 1 #saying: n is equal to n + 1 
                #s = s.replace(". ")
                r.append(s)
        return n, r  

    def getSentences (self): #read through the entire text and seperates the sentences
        with open (self.filename) as f:
            fullText = f.read()
        fullText = fullText.replace ('/n', ' ')
        self.sentences = fullText.split(".")     


            