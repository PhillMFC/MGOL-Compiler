class Token:
    def __init__(self, lexeme, currentState) -> None:
        self.token: str = self.setToken(currentState)
        self.lexeme: str = lexeme
        self.lexemeClass: str = self.setLexemeClass(lexeme)
        self.lexemeType: str = self.setLexemeType(lexeme)
        self.idTable: dict = {}

    @property
    def token(self) -> str:
        return self.token
    
    @property
    def lexeme(self) -> str:
        return self.lexeme
    
    @property
    def lexemeClass(self) -> str:
        return self.lexemeClass
    
    @property
    def lexemeType(self) -> str:
        return self.lexemeType
    
    @property
    def idTable(self) -> str:
        return self.idTable
    
    @token.setter
    def token(self, token) -> None:
        self.token = token

    @lexeme.setter
    def lexeme(self, lexeme) -> None:
        self.lexeme = lexeme
    
    @lexemeClass.setter
    def lexemeClass(self, lexemeClass) -> None:
        self.lexemeClass = lexemeClass
    
    @lexemeType.setter
    def lexemeType(self, lexemeType) -> None:
        self.lexemeType = lexemeType
    
    @token.setter
    def idTable(self, **kwargs) -> None:
        self.token = kwargs

    keyWords: tuple = ("inicio","varinicio","varfim","escreva",
                    "leia","se","entao","fimse","repita",
                    "fimrepita","fim","inteiro","literal",
                    "real")

    def setLexemeClass(self, lexeme):
        return lexeme
    
    def setLexemeType(self, lexeme):
        return lexeme

    def setToken(self, currentState: str) -> str:
        
        if currentState == 'q2':
            self.token('Comentário')

        elif currentState == 'q3':
            self.token('EOF')
              
        elif currentState == 'q5':
            self.token('Lit')
                   
        elif currentState == 'q6':
            self.token('id')

        elif currentState == 'q7':
            self.token('Vir')

        elif currentState == 'q10':
            self.token('RCB')

        elif currentState == 'q8' or currentState == 'q9' or currentState == 'q11' or currentState == 'q12' or currentState == 'q13' or currentState == 'q14':
            self.token('OPR')

        elif currentState == 'q15':
            self.token('PT_V')

        elif currentState == 'q16':
            self.token('AB_P')

        elif currentState == 'q17':
            self.token('FC_P')

        elif currentState == 'q18':
            self.token('OPM')

        elif currentState == 'q19' or currentState == 'q21' or currentState == 'q24':
            self.token('Num')
        
        else:
            self.token('ERRO')



        


