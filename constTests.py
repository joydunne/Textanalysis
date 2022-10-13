from constClass import *

USFile = constText ("USconst.txt")
CanadaFile = constText ("canadaConst.txt")
NetherlandFile = constText ("netherlandConst.txt")

#print ("Number of Lines in US:", USFile.fileLength()) #() calls the function 
#print ("Number of Lines in Canada:", CanadaFile.fileLength()) #() calls the function 
print ("Number of Lines in Netherlands:", NetherlandFile.fileLength()) #() calls the function 

#print ("Number of Stanzas in US:", USFile.stanzaCount()) #() calls the function 
#print ("Number of Stanzas in Canada:", CanadaFile.stanzaCount()) #() calls the function 
print ("Number of Stanzas in Netherlands:", NetherlandFile.stanzaCount()) #() calls the function 

importantWords  = ["religion", "god", "faith", "church", "secular", "deity", "devout", "saint", "pious", "holy", "sacred"]
for w in importantWords:
    #print (f"Number of {w} in US:", USFile.religiousWords(w))
    #print (f"Number of {w} in Canada:", CanadaFile.religiousWords(w))
    print (f"Number of {w} in Netherlands:", NetherlandFile.religiousWords(w))
#print ("Number of Sentences in US:", len(USFile.sentences))
#print ("Number of Sentences in Canada:", len(CanadaFile.sentences))
print ("Number of Sentences in Netherlands:", len(NetherlandFile.sentences))