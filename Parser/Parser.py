import pandas as pd
from Token.token import Token
from Error.error import Error
from scanner.scanner import Scanner
from Semantic.semantic import Semantic

class Parser:
    
    def __init__(self):
        self._scanner = Scanner()
        self.slrTable = pd.read_csv("Parser\slr.csv", index_col="state")
        self.grammarRules: dict = self.grammarRulesToDict()
        self.stack = [0]  
        self.symbols = [] 
        self.currentToken: Token
        self.semanticHandler: Semantic = Semantic()
        self.syntaxRuleNumber = '' 

    def grammarRulesToDict(self):
        pathToFile = 'Parser\\rules.txt'
        grammarRules = {}
        with open(pathToFile, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    ruleNumber, rule = line.strip().split(":", 1)
                    self.syntaxRuleNumber = ruleNumber
                    leftSide, rightSide = rule.strip().split("→")
                    grammarRules[int(ruleNumber)] = (
                        leftSide.strip(),
                        [token.strip() for token in rightSide.strip().split()]
                    )
        return grammarRules

    def parse(self):
        _recoveryToken = None
        self.currentToken = _recoveryToken or self._scanner.requestToken()
        
        while (self.currentToken):
            
            if not isinstance(self.currentToken,bool) and self.currentToken.lexemeClass != 'Comentário' and self.currentToken.lexemeClass != 'ERRO':
                state = self.stack[-1]
                tokenClass = self.currentToken.lexemeClass
                action = self.slrTable.loc[state, tokenClass] if tokenClass in self.slrTable.columns else None
                if pd.isna(action):
                    _recoveryToken = self.currentToken
                    missingToken = self.phraseLevelRecovery()
                    
                    if missingToken:
                        Error.raiseErrorMessage(self.currentToken.lineIndex, self.currentToken.columnIndex, f'ERRO SINTÁTICO - PHRASE-LEVEL-RECOVERY: token \'{missingToken}\' esperado \nao invés de \'{self.currentToken.toString()}\'')
                        action = self.slrTable.loc[state, missingToken]
                        tokenClass = missingToken
                        
                    missingToken = self.simulationRecovery(self.stack, tokenClass)
                    
                    if missingToken:
                        Error.raiseErrorMessage(self.currentToken.lineIndex, self.currentToken.columnIndex, f'ERRO SINTÁTICO - Simulação: token \'{missingToken}\' esperado \nao invés de \'{self.currentToken.toString()}\'')
                        action = self.slrTable.loc[state, missingToken]
                        tokenClass = missingToken
                        
                    elif not missingToken:
                        Error.raiseErrorMessage(self.currentToken.lineIndex, self.currentToken.columnIndex, f'ERRO SINTÁTICO - MODO PÂNICO: Ação desconhecida para estado \'{state}\' e token \'{self.currentToken.toString()}\'')
                        self._scanner.requestToken()

                if action.startswith("s"):
                    pastState = state
                    nextState = int(action[1:])
                    self.stack.append(nextState)
                    self.symbols.append(tokenClass)
                    #self.printExecution(tokenClass if _recoveryToken else self.currentToken.toString(), 'Shift', pastState, tokenClass, action, self.stack)
                    self.currentToken = _recoveryToken or self._scanner.requestToken()
                    
                elif action.startswith("R"):
                    pastState = state
                    rule_num = int(action[1:])
                    leftSide, rightSide = self.grammarRules[rule_num]
                    
                    for _ in rightSide:
                        self.stack.pop()
                        self.symbols.pop()
                        
                    state = self.stack[-1]
                    self.stack.append(int(self.slrTable.loc[state, leftSide]))
                    self.symbols.append(leftSide)
                    #self.printExecution(tokenClass if _recoveryToken else self.currentToken.toString(), 'Reduce', pastState, tokenClass, action, self.stack, leftSide, rightSide)
                    
                elif action == "Acc":
                    print("Análise Sintátia concluída. Entrada aceita!")
                    return True
                
            elif not isinstance(self.currentToken,bool) and self.currentToken.lexemeClass == 'ERRO':
                    self.currentToken = self._scanner.requestToken()
            else:
                self.currentToken = self._scanner.requestToken()
            _recoveryToken = None
            

    def phraseLevelRecovery(self):
        _state = self.stack[-1]
        _missingToken = None
        
        for _tokenClass in self.slrTable.columns:
            action = self.slrTable.loc[_state, _tokenClass]
            if not pd.isna(action):
                
                if _tokenClass == 'AB_P':     
                    _missingToken = 'AB_P'
                    
                elif _tokenClass == 'vir':     
                    _missingToken = 'vir'
                    
                elif _tokenClass == 'FC_P':
                    _missingToken = 'FC_P'
                    
                elif _tokenClass == 'lit':
                    _missingToken = 'lit'
                    
                elif _tokenClass == 'real':
                    _missingToken = 'real'
                    
                elif _tokenClass == 'OPR':
                    _missingToken = 'OPR'
                    
                elif _tokenClass == 'PT_V':
                    _missingToken = 'PT_V'
                    
                elif _tokenClass == 'PT_V':
                    _missingToken = 'PT_V'
                    
                elif _tokenClass == 'fimse':
                    _missingToken = 'fimse'
                    
                elif _tokenClass == 'entao':
                    _missingToken = 'entao'
                    
                elif _tokenClass == 'fimfaca':
                    _missingToken = 'fimfaca' 
        
        return _missingToken     
    
    def simulationRecovery(self, stack, tokenClass):

        _state = stack[-1]
        _targetStates = self.slrTable.loc[:,tokenClass]
        
        for _tokenClass in self.slrTable.columns:
            action = self.slrTable.loc[_state, _tokenClass]
            if not pd.isna(action):
                if action.startswith("s"):
                    if int(action[1:]) in _targetStates.index:
                        return _tokenClass
                
    @staticmethod
    def printExecution(token, context, state, lexemeClass, action, stack, leftSide=None, rightSide=None):
        if context == 'Shift':
            print(f'''{context}: {token}\n\
                State: {state}\n\
                Class: {lexemeClass}\n\
                Action: {action}\n\
                stack = {stack}\n''')
            
        elif context == 'Reduce':
            print(f'''{context}: {token}\n\
                State: {state}\n\
                Class: {lexemeClass}\n\
                Action: {action}\n\
                Reduction: {leftSide} → {rightSide}\n\
                stack = {stack}\n''')
    
    def printRulesAndSlr(self):
        for key, value in self.grammarRules.items():
            print(f'{key}: {value}')
        print(self.slrTable) 
        

if __name__ == '__main__':
    parser = Parser()
    
    try:
        parser.parse()
    except Exception as e:
        print(e)
        print('Análise interrompida. Entrada não aceita')