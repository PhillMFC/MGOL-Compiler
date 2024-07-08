from Token.token import Token

class Afd:
    lineIndex = ''
    columnIndex = ''
    char: str = ''
    currentState: str = 'q0'
    currentLexeme: str = ''
    token = None

    finalStates: tuple = ('q2', 'q3', 'q5', 'q6', 
                   'q7','q8', 'q9', 'q10', 'q11', 
                   'q12', 'q13', 'q14', 'q15', 
                   'q16', 'q17', 'q18', 'q19', 
                   'q21', 'q24', 'q25')

    @classmethod
    def setChar(self, char: str, lineIndex, columnIndex):
        self.char = char
        self.lineIndex = lineIndex
        self.columnIndex = columnIndex

        if self.char == '$':
            self.generateToken()
    
    @classmethod
    def verifyAlpha(self, lexeme: str) -> str:
        if lexeme.isalpha():
            return lexeme
    
    @classmethod
    def verifyNumeric(self, lexeme: str) -> str:
        if lexeme.isnumeric():
            return lexeme
    
    @classmethod
    def resetAfd(self):
        self.currentState: str = 'q0'
        self.currentLexeme: str = ''
        self.token = None
    
    @classmethod
    def transitionTable(self, lexeme) -> dict :
        return {
            'q0': {' ':'q25', '$':'q3', '\n':'q25', '{':'q1', '$':'q3','"':'q4', ',':'q7', '<':'q8', '>':'q13', '=':'q12', '+':'q18', '-':'q18', ';':'q15', '(':'q16',')':'q17', '*':'q18', '/':'q18', f'{self.verifyAlpha(lexeme)}':'q6', f'{self.verifyNumeric(lexeme)}':'q19'},
            'q1': { '}':'q2', ' ':'q1', '\n':'q1', ':':'q1', f'{self.verifyAlpha(lexeme)}': 'q1', f'{self.verifyNumeric(lexeme)}':'q1', ' ':'q1', '\n':'q1', '{':'q1', '$':'q1', ',':'q1', '<':'q1', '>':'q1', '=':'q1', '+':'q1', '-':'q1', ';':'q1', '(':'q1',')':'q1', '*':'q1', '/':'q1'},
            'q4': {'"':'q5',':':'q4', f'{self.verifyAlpha(lexeme)}': 'q4', f'{self.verifyNumeric(lexeme)}':'q4', ' ':'q4','\\':'q4', '\n':'q4', '{':'q4', '$':'q4', ',':'q4', '<':'q4', '>':'q4', '=':'q4', '+':'q4', '-':'q4', ';':'q4', '(':'q4',')':'q4', '*':'q4', '/':'q4'}, 
            'q6': {f'{self.verifyAlpha(lexeme)}': 'q6', f'{self.verifyNumeric(lexeme)}':'q6', '_':'q6'},
            'q8': {'>':'q11', '=':'q9', '-':'q10'},
            'q13': {'=':'q14'},
            'q19': {'e':'q22', 'E':'q22', '.':'q20', f'{self.verifyNumeric(lexeme)}':'q19'}, 
            'q20': {f'{self.verifyNumeric(lexeme)}':'q21'}, 
            'q21': {'e':'q22', 'E':'q22', f'{self.verifyNumeric(lexeme)}':'q21'}, 
            'q22': {f'{self.verifyNumeric(lexeme)}':'q24', '+':'q23', '-':'q23'}, 
            'q23': {f'{self.verifyNumeric(lexeme)}':'q24'}, 
            'q24': {f'{self.verifyNumeric(lexeme)}':'q24'},
            'q25': {' ':'q25', '\n':'q25'}
            } 

    @classmethod
    def generateToken(self) -> Token:
        if self.currentLexeme == ' ' or self.currentLexeme == '\n':
            return True
        return Token(self.currentLexeme, self.currentState, self.lineIndex, self.columnIndex)

    @classmethod
    def getToken(self) -> Token:
        return self.token or False

    @classmethod
    def verifyChar(self):

        _transitionTable: dict = self.transitionTable(self.char)
        try:
            self.currentState = _transitionTable[self.currentState][self.char]
            self.currentLexeme += self.char
            return True
        except:
            if self.currentState in self.finalStates:
                self.token = self.generateToken()