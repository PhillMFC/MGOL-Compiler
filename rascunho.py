def lexemeIsAlpha():
    return '212121'

def transitionTable() -> dict :
    return {
    'q0': {'\n':'q0', '{':'q1', '$':'q3','"':'q4', ',':'q7', '<':'q8', '>':'q13', '=':'q12', '+':'q18', '-':'q18', ';':'q15', '(':'q16', '*':'q18', '/':'q18'},
    'q1': { '}':'q2', },
    'q4': {'"':'q5'}, 
    'q6': {f'{lexemeIsAlpha()}': 'q6'},
    'q8': {'>':'q11', '=':'q9', '-':'q10', }, 
    'q13': {'=':'q14'},             
    'q19': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA', 'e':'q22', 'E':'q22', '.':'q20'}, 
    'q20': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}, 
    'q21': {'e':'q22', 'E':'q22'}, 
    'q22': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA', '+':'q23', '-':'q23'}, 
    'q23': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}, 
    'q24': {"TEM QUE ARRUMAR ESSA TRETA AQUI": 'ESTADO DE TRETA'}
}

def verifyLexeme():
    print(transitionTable())


verifyLexeme()