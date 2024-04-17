class Token:
    def __init__(self) -> None:
        self._lexeme: str = ''
        self._lexemeClass: str = ''
        self._lexemeType: str = ''

    @property
    def lexeme(self) ->str:
        return self._lexeme
    
    @property
    def lexemeClass(self) ->str:
        return self._lexemeClass
    
    @property
    def lexemeType(self) ->str:
        return self._lexemeType

    @lexeme.setter
    def setLexeme(self, value):
        self._lexeme = value

    @lexemeClass.setter
    def setLexemeClass(self, value):
        self._lexemeClass = value

    @lexemeType.setter
    def setLexemeClass(self, value):
        self._lexemeType = value
        