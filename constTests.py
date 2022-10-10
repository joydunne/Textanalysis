from constClass import *

USFile = constText ("USconst.txt")
CanadaFile = constText ("canadaConst.txt")
NetherlandFile = constText ("netherlandConst.txt")

#print ("Number of Lines:", CanadaFile.fileLength()) #() calls the function 

#print ("Number of Stanzas:", CanadaFile.stanzaCount()) #() calls the function 

w = "faith"
print (f"Number of {w}:", {CanadaFile.religiousWords(w)})

for s in CanadaFile.sentences:
    print (s)
print ("Number of Sentences:", len(CanadaFile.sentences))