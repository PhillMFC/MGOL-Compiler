import traceback
import pandas as pd
from Token.token import Token
from scanner.scanner import Scanner

class Parser:
    
    def __init__(self):
        self._scanner = Scanner()
        self.slrTable = pd.read_csv("Parser\slr.csv", index_col="state")
        self.grammarRules: dict = self.grammarRulesToDict()
        self.printRulesAndSlr()
        
    @staticmethod
    def grammarRulesToDict():
        pathToFile = 'Parser\\rules.txt'
        grammarRules = {}
        with open(pathToFile, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    ruleNumber, rule = line.strip().split(":", 1)
                    leftSide, rightSide = rule.strip().split("→")
                    grammarRules[int(ruleNumber)] = (
                        leftSide.strip(),
                        [token.strip() for token in rightSide.strip().split()]
                    )
        return grammarRules

    def parse(self):
        stack = [0]  
        symbols = [] 
        currentToken = self._scanner.requestToken()
        
        while (currentToken):
            if not isinstance(currentToken,bool) and currentToken.lexemeClass != 'Comentário':
                state = stack[-1]
                tokenClass = currentToken.lexemeClass
                
                action = self.slrTable.loc[state, tokenClass] if tokenClass in self.slrTable.columns else None

                if pd.isna(action):
                    print(f"Syntax error at token {state, currentToken.toString()}")
                    return False

                if action.startswith("s"):
                    pastState = state
                    nextState = int(action[1:])
                    stack.append(nextState)
                    symbols.append(tokenClass)
                    self.printExecution(currentToken.toString(), 'Shift', pastState, tokenClass, action, stack)
                    currentToken = self._scanner.requestToken()
                    
                elif action.startswith("R"):
                    rule_num = int(action[1:])
                    leftSide, rightSide = self.grammarRules[rule_num]
                    for _ in rightSide:
                        stack.pop()
                        symbols.pop()
                    state = stack[-1]
                    stack.append(int(self.slrTable.loc[state, leftSide]))
                    symbols.append(leftSide)
                    self.printExecution(currentToken.toString(), 'Reduce', pastState, tokenClass, action, stack, leftSide, rightSide)
                    
                elif action == "Acc":
                    print("Input accepted successfully!")
                    return True
                else:
                    print(f"Unknown action: {action}")
                    return False
            else:
                currentToken = self._scanner.requestToken()
            
            
    @staticmethod
    def printExecution(token, context, state, lexemeClass, action, stack, leftSide=None, rightSide=None):
        if context == 'Shift':
            print(f'''{context}: {token}\n\
                State: {state}\n\
                Class: {lexemeClass}\n\
                Action: {action}\n\
                Stack = {stack}\n''')
        elif context == 'Reduce':
            print(f'''{context}: {token}\n\
                State: {state}\n\
                Class: {lexemeClass}\n\
                Action: {action}\n\
                Reduction: {leftSide} → {rightSide}\n\
                Stack = {stack}\n''')
    
    def printRulesAndSlr(self):
        for key, value in self.grammarRules.items():
            print(f'{key}: {value}')
        print(self.slrTable) 
        

if __name__ == '__main__':
    parser = Parser()
    
    try:
        parser.parse()
    except Exception as e:
        print(traceback.print_exc() or '\nÉ isso aí')