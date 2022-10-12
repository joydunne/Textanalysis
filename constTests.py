from constClass import *

USFile = constText ("USconst.txt")
CanadaFile = constText ("canadaConst.txt")
NetherlandFile = constText ("netherlandConst.txt")

print ("Number of Lines:", USFile.fileLength()) #() calls the function 
#print ("Number of Lines:", CanadaFile.fileLength()) #() calls the function 
#print ("Number of Lines:", NetherlandFile.fileLength()) #() calls the function 

print ("Number of Stanzas:", USFile.stanzaCount()) #() calls the function 
#print ("Number of Stanzas:", CanadaFile.stanzaCount()) #() calls the function 
#print ("Number of Stanzas:", NetherlandFile.stanzaCount()) #() calls the function 

w = "religion"
print (f"Number of {w}:", USFile.religiousWords(w))
#print (f"Number of {w}:", {CanadaFile.religiousWords(w)})
#print (f"Number of {w}:", {NetherlandFile.religiousWords(w)})

print ("Number of Sentences:", len(USFile.sentences))
#print ("Number of Sentences:", len(CanadaFile.sentences))
#print ("Number of Sentences:", len(NetherlandFile.sentences))