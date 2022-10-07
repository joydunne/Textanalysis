class constText:
    '''Analyze texts using stats and such.'''
    def __init__ (self, filename):
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
    

        