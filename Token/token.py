from Error.error import Error

class Token:
    def __init__(self, lexeme, currentState, lineIndex, columnIndex) -> None:
        self.lexeme: str = lexeme
        self.lineIndex = lineIndex
        self.columnIndex = columnIndex
        self.lexemeClass: str = self.setLexemeClass(currentState)
        self.lexemeType: str = self.setLexemeType(lexeme)

    keywords: tuple = ("inicio","varinicio","varfim","escreva",
                    "leia","se","entao","fimse","faca-ate",
                    "fimfaca","fim","inteiro","lit",
                    "real")
    state_map = {
        'q2': 'Comentário',
        'q3': 'EOF',
        'q5': 'Lit',
        'q6': 'id',
        'q7': 'Vir',
        'q10': 'RCB',
        'q8': 'OPR',
        'q9': 'OPR',
        'q11': 'OPR',
        'q12': 'OPR',
        'q13': 'OPR',
        'q15': 'PT_V',
        'q16': 'AB_P',
        'q17': 'FC_P',
        'q18': 'OPM',
        'q19': 'Num',
        'q21': 'Num',
        'q24': 'Num'
        }
    
    def setLexemeClass(self, currentState: str) -> str:
        
        if self.lexeme in self.keywords:
            return self.lexeme
        
        elif self.state_map.get(currentState, 'ERRO'):
            return self.state_map.get(currentState, 'ERRO')
        else:
            return 'ERRO'
        
        
    def setLexemeType(self, lexeme: str):
        if self.lexemeClass == 'Num':
            try:
                if int(lexeme):
                    return 'inteiro'
            except:
                return 'real'
        elif self.lexemeClass == 'Lit':
           return 'literal'
        elif self.lexeme in self.keywords:
            return self.lexeme
        elif self.lexemeClass == 'ERRO':
            return 'ERRO'
        else:
           return 'NULO'

    def toString(self):
        return self.__dict__