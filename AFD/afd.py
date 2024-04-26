class Afd:
    def __init__(self, lexemeList: list[str]) -> None:
        self.lexemeList: list[str] = lexemeList
        self.currentState: str = 'q0'

    def iterateOverLine(self):
        for lexeme in self.lexemeList:
            print(self.verifyLexeme(lexeme))
            print(self.currentState)

    def intLexeme(self, lexeme):
        try:
            if int(lexeme) in range(0,10):
                self.currentState = 'q19'
                return
        except:
            print('Not a number')

    def verifyLexeme(self, lexeme):
        print('entrou aqui')
        if lexeme.isalpha():
            self.currentState = 'q6'
            print('deu bom')
            return
        print('entrou aqui também')
        self.currentState = self.transitionTable[self.currentState][lexeme]
        return self.currentState in self.finalStates

    allStates = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 
                'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
                'q13','q14', 'q15', 'q16', 'q17', 'q18', 
                'q19', 'q20', 'q21', 'q22', 'q23', 'q24'}

    finalStates = {'q2', 'q3', 'q5', 'q6', 
                   'q7', 'q9', 'q10', 'q11', 
                   'q12', 'q13', 'q14', 'q15', 
                   'q16', 'q17', 'q18', 'q19', 
                   'q21', 'q24'}

    transitionTable = {
        'q0': {'\n':'q0', '{':'q1', '$':'q3','"':'q4', ',':'q7', '<':'q8', '>':'q13', '=':'q12', '+':'q18', '-':'q18', ';':'q15', '(':'q16', '*':'q18', '/':'q18'},
        'q1': { '}':'q2', },
        'q4': {'"':'q5'}, 
        'q6': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'},
        'q8': {'>':'q11', '=':'q9', '-':'q10', }, 
        'q13': {'=':'q14'},             
        'q19': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA', 'e':'q22', 'E':'q22', '.':'q20'}, 
        'q20': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}, 
        'q21': {'e':'q22', 'E':'q22'}, 
        'q22': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA', '+':'q23', '-':'q23'}, 
        'q23': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}, 
        'q24': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}
    }


afd = Afd(['"', '\n', '<', '>', '-', ',', ';', ':', '.', '!', '?'])

afd.iterateOverLine()