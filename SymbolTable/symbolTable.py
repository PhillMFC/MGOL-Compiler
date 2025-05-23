from Token.token import Token

class SymbolTable:
    idTable: dict = {}
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
            self.addId(token.lexeme)

    @classmethod
    def updateTable(self):
        self._isTokenIdValue: bool = False
        _currentIdValue: str = self.idTable[self._lastIdToken]
        if _currentIdValue:
            self.idTable[self._lastIdToken] = f'{self._idValue}'.replace(f'{self._lastIdToken}',f'({_currentIdValue})')
        else:
            self.idTable[self._lastIdToken] = self._idValue
        self._idValue = ''
    
    @classmethod
    def addId(self, lexeme: str):
        self._lastIdToken = lexeme
        self.idTable.setdefault(lexeme,'')

    @classmethod
    def printTable(self):
        print('\n', self.idTable, '\n', self.keywords)
        
                    

        
