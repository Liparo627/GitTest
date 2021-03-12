    
class Transition:
    def __init__(self,etatDest=None,label=""):
        self.Destination  = etatDest
        self.Etiquette   = label

    def setDest(self,dest):
        self.Destination = dest
        
    def setLabel(self,lbl):
        self.Etiquette = lbl
        
    def getDest(self):
        return self.Destination
    def getLabel(self):
        return self.Etiquette
