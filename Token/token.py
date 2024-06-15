class Token:
    def __init__(self, lexeme, currentState) -> None:
        self.lexeme: str = lexeme
        self.lexemeClass: str = self.setLexemeClass(currentState)
        self.lexemeType: str = self.setLexemeType(lexeme)

    keyWords: tuple = ("inicio","varinicio","varfim","escreva",
                    "leia","se","entao","fimse","repita",
                    "fimrepita","fim","inteiro","literal",
                    "real")
    
    def setLexemeType(self, lexeme: str):
        return f'{type(lexeme)}'
    
    def setIdTable(self, **kwargs):
        self.idTable = kwargs

    def setLexemeClass(self, currentState: str) -> str:

        if self.lexeme in self.keyWords:
            return self.lexeme
        
        elif currentState == 'q2':
            return 'Comentário'

        elif currentState == 'q3':
            return 'EOF'
              
        elif currentState == 'q5':
            return 'Lit'
                   
        elif currentState == 'q6':
            return 'id'

        elif currentState == 'q7':
            return 'Vir'

        elif currentState == 'q10':
            return 'RCB'

        elif currentState == 'q8' or currentState == 'q9' or currentState == 'q11' or currentState == 'q12' or currentState == 'q13' or currentState == 'q14':
            return 'OPR'

        elif currentState == 'q15':
            return 'PT_V'

        elif currentState == 'q16':
            return 'AB_P'

        elif currentState == 'q17':
            return 'FC_P'

        elif currentState == 'q18':
            return 'OPM'

        elif currentState == 'q19' or currentState == 'q21' or currentState == 'q24':
            return 'Num'
        
        else:
            return 'ERRO'
