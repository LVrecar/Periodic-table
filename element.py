
#vrstno število
#masno število
#oznaka
#ime
#skupina
#perioda

class Element:
    def __init__(self, name, symbol, atomicNumber, mass, period, group):
        self.name = name
        self.symbol = symbol
        self.atomicNumber = atomicNumber
        self.mass = mass
        self.group = group
        self.period = period
    
    def getSymbol(self):
        return self.symbol
    
    def getName(self):
        return self.name
    
    def getAtomicNumber(self):
        return self.atomicNumber
    
    def getMass(self):
        return self.mass
    
    def getGroup(self):
        return self.group
    
    def getPeriod(self):
        return self.period