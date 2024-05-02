import sys
from AFD.token import Token

class Afd:
    def __init__(self, lexemeList: list[str]) -> None:
        self.lexemeList: list[str] = lexemeList
        self.currentState: str = 'q0'
        self.currentLexeme: str = ''
        self.tokenList: list = []
    
    allStates: tuple = ('q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 
                'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
                'q13','q14', 'q15', 'q16', 'q17', 'q18', 
                'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25')

    finalStates: tuple = ('q2', 'q3', 'q5', 'q6', 
                   'q7','q8', 'q9', 'q10', 'q11', 
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
            'q1': { '}':'q2', ' ':'q1', '\n':'q1', ':':'q1', f'{self.verifyAlpha(lexeme)}': 'q1', f'{self.verifyNumeric(lexeme)}':'q1', ' ':'q1', '\n':'q1', '{':'q1', '$':'q1', ',':'q1', '<':'q1', '>':'q1', '=':'q1', '+':'q1', '-':'q1', ';':'q1', '(':'q1',')':'q1', '*':'q1', '/':'q1'},
            'q2': {},
            'q3': {},
            'q4': {'"':'q5',':':'q4', f'{self.verifyAlpha(lexeme)}': 'q4', f'{self.verifyNumeric(lexeme)}':'q4', ' ':'q4','\\':'q4', '\n':'q4', '{':'q4', '$':'q4', ',':'q4', '<':'q4', '>':'q4', '=':'q4', '+':'q4', '-':'q4', ';':'q4', '(':'q4',')':'q4', '*':'q4', '/':'q4'}, 
            'q5': {},
            'q6': {f'{self.verifyAlpha(lexeme)}': 'q6', f'{self.verifyNumeric(lexeme)}':'q6', '_':'q6'},
            'q7': {},
            'q8': {'>':'q11', '=':'q9', '-':'q10'},
            'q9': {},
            'q10': {},
            'q11': {},
            'q12': {},
            'q13': {'=':'q14'},
            'q14': {},
            'q15': {},
            'q16': {},
            'q17': {},
            'q18': {},
            'q19': {'e':'q22', 'E':'q22', '.':'q20', f'{self.verifyNumeric(lexeme)}':'q19'}, 
            'q20': {f'{self.verifyNumeric(lexeme)}':'q21'}, 
            'q21': {'e':'q22', 'E':'q22', f'{self.verifyNumeric(lexeme)}':'q21'}, 
            'q22': {f'{self.verifyNumeric(lexeme)}':'q24', '+':'q23', '-':'q23'}, 
            'q23': {f'{self.verifyNumeric(lexeme)}':'q24'}, 
            'q24': {f'{self.verifyNumeric(lexeme)}':'q24'},
            'q25': {' ':'q25', '\n':'q25'}
            } 
    
    def iterateLexemeList(self) -> None:
        print('LINHA: ' + f'{self.lexemeList}')
        index: int = 0
        print('ta funfando')
        while index + 1 < len(self.lexemeList):
            if self.verifyLexeme(self.lexemeList[index]):
                self.currentLexeme += self.lexemeList[index]

                if self.currentState == 'q8':
                    index = self.verifyNextLexeme(index+1) - 1

                if self.currentState == 'q19':
                    index = self.verifyNextLexeme(index+1) - 1

                if self.currentState in self.finalStates:
                    self.generateToken(self.currentLexeme)
                else:
                    print(f'Current state \'{self.currentState}\' is not a final state. Token generation attempt failed.')
                    sys.exit()
            else:
                self.currentLexeme += self.lexemeList[index]
            index += 1

    def verifyNextLexeme(self, index: int) -> int:
        _index: int = index
        while self.lexemeList[_index] in self.transitionTable(self.lexemeList[_index])[self.currentState]:
            self.currentLexeme += self.lexemeList[_index]
            self.currentState = self.transitionTable(self.lexemeList[_index])[self.currentState][self.lexemeList[_index]]
            _index += 1
        return _index

    def generateToken(self, lexeme: str) -> None:
        token = Token(lexeme, self.currentState)
        self.tokenList.append(token.lexemeClass)
        print(f'TokenList: {self.tokenList}' )
        self.currentLexeme = ''
        self.currentState = 'q0'

    def verifyLexeme(self, lexeme: str) -> bool:
        _transitionTable: dict = self.transitionTable(lexeme)
        self.currentState: str = _transitionTable[self.currentState][lexeme]
        result: bool = self.currentState in self.finalStates
        return result 