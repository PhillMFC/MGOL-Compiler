from Token.token import Token

class SymbolTable:
    idValueTable: dict = {}
    idTable: list = []
    keywords: tuple = ("inicio","varinicio","varfim","escreva",
                    "leia","se","entao","fimse","faca-ate",
                    "fimfaca","fim","inteiro","literal",
                    "real")
    _lastIdToken: str = ''
    _isTokenIdValue: bool = False
    _idValue: str = ''

    @classmethod
    def setIdValue(self, token: Token):

        if self._isTokenIdValue and token.lexemeClass != 'PT_V':
            self._idValue = self._idValue + token.lexeme
        
        elif self._isTokenIdValue and token.lexemeClass == 'PT_V':
            self.updateTable()

        elif token.lexemeClass == 'RCB':
            self._isTokenIdValue = True
        
        elif token.lexemeClass == 'id':
            self.addId(token)

    @classmethod
    def setIdType(self,idLexeme, newType):
        for token in self.idTable:
            if idLexeme == token.lexeme:
                token.lexemeType = newType

    @classmethod
    def updateTable(self):
        self._isTokenIdValue: bool = False
        _currentIdValue: str = self.idValueTable[self._lastIdToken]
        if _currentIdValue:
            self.idValueTable[self._lastIdToken] = f'{self._idValue}'.replace(f'{self._lastIdToken}',f'({_currentIdValue})')
        else:
            self.idValueTable[self._lastIdToken] = self._idValue
        self._idValue = ''
    
    @classmethod
    def addId(self, token: str):
        self._lastIdToken = token.lexeme
        self.idValueTable.setdefault(token.lexeme,'')
        
        if not any(tableToken.lexeme == token.lexeme for tableToken in self.idTable):
            self.idTable.append(token)

    @classmethod
    def printTable(self):
        for token in self.idTable:
            print(token.toString())
        print(self.keywords)
        
                    

        
