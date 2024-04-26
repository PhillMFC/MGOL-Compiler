class Token:
    def __init__(self, lexeme, lexemeClass, lexemeType) -> None:
        self._lexeme: str = lexeme
        self._lexemeClass: str = lexemeClass
        self._lexemeType: str = lexemeType

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
        