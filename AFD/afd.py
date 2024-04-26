from AFD.token import Token


class Afd:
    def __init__(self, lexemeList: list[str]) -> None:
        self.lexemeList: list[str] = lexemeList
        self.currentState: str = 'q0'
        self.currentLexeme: str = ''
        self.tokenLine: list = []
    
    keyWords: tuple = ("inicio","varinicio","varfim","escreva",
                        "leia","se","entao","fimse","repita",
                        "fimrepita","fim","inteiro","literal",
                        "real")
    
    allStates: tuple = ('q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 
                'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
                'q13','q14', 'q15', 'q16', 'q17', 'q18', 
                'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25')

    finalStates: tuple = ('q2', 'q3', 'q5', 'q6', 
                   'q7', 'q9', 'q10', 'q11', 
                   'q12', 'q13', 'q14', 'q15', 
                   'q16', 'q17', 'q18', 'q19', 
                   'q21', 'q24', 'q25')

    def verifyKeyWord(self, lexeme: str) -> bool:
        return lexeme in self.keyWords
            
    def verifyAlpha(self, lexeme: str) -> str:
        if lexeme.isalpha():
            return lexeme
    
    def verifyNumeric(self, lexeme: str) -> str:
        if lexeme.isnumeric():
            return lexeme
        
    def transitionTable(self, lexeme) -> dict :
        return {
        'q0': {' ':'q25', '\n':'q25', '{':'q1', '$':'q3','"':'q4', ',':'q7', '<':'q8', '>':'q13', '=':'q12', '+':'q18', '-':'q18', ';':'q15', '(':'q16',')':'q17', '*':'q18', '/':'q18', f'{self.verifyAlpha(lexeme)}':'q6', f'{self.verifyNumeric(lexeme)}':'q19'},
        'q1': { '}':'q2', ' ':'q25', '\n':'q25'},
        'q4': {'"':'q5', f'{self.verifyAlpha(lexeme)}': 'q4', f'{self.verifyNumeric(lexeme)}':'q4', ' ':'q25', '\n':'q25'}, 
        'q6': {f'{self.verifyAlpha(lexeme)}': 'q6', f'{self.verifyNumeric(lexeme)}':'q6'},
        'q8': {'>':'q11', '=':'q9', '-':'q10', }, 
        'q13': {'=':'q14'},             
        'q19': {f'{self.verifyNumeric(lexeme)}':'q19', 'e':'q22', 'E':'q22', '.':'q20'}, 
        'q20': {f'{self.verifyNumeric(lexeme)}':'q21'}, 
        'q21': {'e':'q22', 'E':'q22'}, 
        'q22': {f'{self.verifyNumeric(lexeme)}':'q24', '+':'q23', '-':'q23'}, 
        'q23': {f'{self.verifyNumeric(lexeme)}':'q24'}, 
        'q24': {f'{self.verifyNumeric(lexeme)}':'q24'},
        'q25:': {' ':'q25', '\n':'q25'}
    }

    def iterateOverLine(self) -> None:
        print(self.lexemeList)
        for lexeme in self.lexemeList:
            if not self.currentState == 'q4' or self.currentState == 'q1':
                _isFinalState: bool = self.verifyLexeme(lexeme)

            if self.currentState == 'q4' or self.currentState == 'q1':
                self.currentLexeme += lexeme
            elif _isFinalState:
                self.generateToken(lexeme)
                self.currentState = 'q0'
            else:
                print('Erro ' + f'{lexeme}' , self.currentState)
                self.currentState = 'q0'
        print(f'tokenLine: {self.tokenLine}')
        print('currentLexeme: ' + self.currentLexeme)
        print('lexeme: ' + lexeme)

    def generateToken(self, lexeme: str) ->Token:
        self.tokenLine.append(lexeme)

    def verifyLexeme(self, lexeme: str) -> bool:
        _transitionTable: dict = self.transitionTable(lexeme)
        self.currentState = _transitionTable[self.currentState][lexeme]
        return self.currentState in self.finalStates

        
