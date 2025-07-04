class SymbolObject:
    def __init__(self, symbol, attribute=None, attrType=None, codeSnippet = None):
        self.symbol = symbol
        self.attribute = attribute 
        self.type = attrType
        self.codeSnippet = codeSnippet
    
    def __str__(self):
        return f'{{symbol: \'{self.symbol}\', attribute = \'{self.attribute}\', type = \'{self.type}\', codeSnippet = \'{self.codeSnippet}\'}}'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def setAttribute(self, attr):
        self.attribute = attr
        
    @classmethod
    def setType(self, typeValue):
        self.type = typeValue
        
    @classmethod
    def setCodeSnippet(self, snippet):
        self.setCodeSnippet = snippet