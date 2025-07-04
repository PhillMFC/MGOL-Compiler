from Semantic.SymbolObject import SymbolObject
from Token.token import Token
from SymbolTable.symbolTable import SymbolTable

class Semantic:
    def __init__(self):
        self.semanticStack: list[str] = []
        self.tempVarCount = 0
        self.rules: dict = {
            2:self.rule2,
            5:self.rule5,
            6:self.rule6,
            7:self.rule7,
            8:self.rule8,
            9:self.rule9,
            10:self.rule10,
            11:self.rule11,
            13:self.rule13,
            14:self.rule14,
            15:self.rule15,
            16:self.rule16,
            17:self.rule17,
            19:self.rule19,
            20:self.rule20,
            21:self.rule21,
            22:self.rule22,
            23:self.rule23,
            25:self.rule25,
            26:self.rule26,
            27:self.rule27,
            32:self.rule32,
            33:self.rule33,
            34:self.rule34,
            35:self.rule35,
            36:self.rule36,
            37:self.rule37
        }
        self.fileBuffer: list[str] = ['#include <stdio.h>','typedef char literal[256];','int main(void)','{']
        self.syntaxRule: str = None
        self.poppedSymbols: list[str] = []
        self.leftSide = ''
        self.lineIndex = 0
        self.columnIndex = 0
        self.createFile: bool = True
    
    def createAndFillFile(self):
        for n in range(self.tempVarCount):
            self.fileBuffer.insert(4+n, f'int T{n};')
        
        if self.createFile:    
            with open("program.c", 'w') as file:
                for line in self.fileBuffer:
                    file.write(line + '\n')
    
    def printSymbolTable(self):
        SymbolTable.printTable()
    
    def executeRule(self, ruleNumber: int):
        ruleFunction = self.rules.get(ruleNumber, None)
        if ruleFunction:
            ruleFunction()
    
    def addToStackFromToken(self, token: Token):
        self.lineIndex = token.lineIndex
        self.columnIndex = token.columnIndex
        self.semanticStack.append(SymbolObject(token.lexemeClass, token.lexeme, token.lexemeType))
    
    def addToStack(self, symbolObject):
        self.semanticStack.append(symbolObject)
    
    def reduceAndStack(self, rule_num, leftSide, rightSide):
        self.leftSide = leftSide                
        self.popNSymbolsFromSemanticStack(len(rightSide))
        
        if rule_num in self.rules.keys():
            self.executeRule(rule_num)
        else:
            self.semanticStack.append(SymbolObject(self.leftSide))
            
    def writeToFileBuffer(self, text: str):
        self.fileBuffer.append(text)
    
    def popNSymbolsFromSemanticStack(self, n):
        symbols = []
        for _ in range(n):
            symbols.append(self.semanticStack.pop())
        symbols.reverse()
        self.poppedSymbols = symbols
    
    def variableDeclarationInFileBuffer(self, idLexeme, idType):
        if idType == 'lit':
            self.fileBuffer.append(f'literal {idLexeme};')
        elif idType == 'inteiro':
            self.fileBuffer.append(f'int {idLexeme};')
        elif idType == 'real':
            self.fileBuffer.append(f'double {idLexeme};')        
    
    def variableInputRequest(self, idType, lexeme):
        if idType == 'lit':
            self.fileBuffer.append(f'scanf("%s", {lexeme});')
        elif idType == 'inteiro':
            self.fileBuffer.append(f'scanf("%d", &{lexeme});')
        elif idType == 'real':
            self.fileBuffer.append(f'scanf("%lf", &{lexeme});')  
        else:
            print(f'\nErro: Variável não declarada. linha: {self.lineIndex}, coluna: {self.columnIndex}')
            self.createFile = False
            
    def variablePrinting(self, idType, lexeme):
        if idType == 'lit':
            self.fileBuffer.append(f'printf("%s", {lexeme});')
        elif idType == 'inteiro':
            self.fileBuffer.append(f'printf("%d", {lexeme});')
        elif idType == 'real':
            self.fileBuffer.append(f'printf("%lf", {lexeme});')
        elif idType == 'literal':
            self.fileBuffer.append(f'printf({lexeme});')
        else:
            print(f'\nErro: Variável não declarada. linha: {self.lineIndex}, coluna: {self.columnIndex}')
            self.createFile = False
            
    def rule2(self):
        self.fileBuffer.append('return 0;')
        self.fileBuffer.append('}')
        self.semanticStack.append(self.leftSide)
    
    def rule5(self):
        self.semanticStack.append(SymbolObject(self.leftSide))
    
    def rule6(self):
        idLexeme = self.poppedSymbols[0].attribute
        idType = self.poppedSymbols[1].type
        SymbolTable.setIdType(idLexeme, idType)
        self.semanticStack.append(SymbolObject(self.leftSide, idLexeme, idType, f'{idLexeme} {idType};'))
        self.variableDeclarationInFileBuffer(idLexeme, idType)
            
    def rule7(self):
        ()
        
    def rule8(self):
        obj: SymbolObject = self.poppedSymbols[-1]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type)) 
        
    def rule9(self):
        obj: SymbolObject = self.poppedSymbols[-1]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type)) 
        
    def rule10(self):
        obj: SymbolObject = self.poppedSymbols[-1]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type))
        
    def rule11(self):
        obj: SymbolObject = self.poppedSymbols[-1]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type)) 
    
    def rule13(self):
        idLexeme: SymbolObject = self.poppedSymbols[1].attribute
        idType = ''
        for token in SymbolTable.idTable:
            if token.lexeme == idLexeme:
                idType = token.lexemeType
        self.variableInputRequest(idType, idLexeme)
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule14(self):
        
        obj: SymbolObject = self.poppedSymbols[1]
        self.variablePrinting(obj.type, obj.attribute)
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule15(self):
        obj: SymbolObject = self.poppedSymbols[-1]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type))
        
    def rule16(self):
        ()
        
    def rule17(self):
        idLexeme: SymbolObject = self.poppedSymbols[0].attribute
        for token in SymbolTable.idTable:
            if token.lexeme == idLexeme:
                self.semanticStack.append(SymbolObject(self.leftSide, idLexeme, token.lexemeType))
                break
        else:
            print(f'Erro: Variável não declarada. linha {self.lineIndex}, coluna {self.columnIndex}\n')
            self.createFile = False
        
    def rule19(self):
        idLexeme = self.poppedSymbols[0]
        found = False
        for token in SymbolTable.idTable:
            if token.lexeme == idLexeme.attribute:
                found = True
                if token.lexemeType == self.poppedSymbols[2].type:
                    self.fileBuffer.append(f'{idLexeme.attribute} = {self.poppedSymbols[2].attribute};')
                    self.semanticStack.append(SymbolObject(self.leftSide))
                else:
                    print(f'Erro: Tipos diferentes para atribuição. linha {self.lineIndex}, coluna {self.columnIndex}')
                    self.createFile = False
                    
                break 

        if not found:
            print(f'Erro: Variável não declarada. linha {self.lineIndex}, coluna {self.columnIndex}')
            self.createFile = False

        
    def rule20(self):
        if self.poppedSymbols[0].type != 'lit' and self.poppedSymbols[2].type == self.poppedSymbols[0].type:
            self.semanticStack.append(SymbolObject(self.leftSide, f'T{self.tempVarCount}', self.poppedSymbols[0].type))
            self.fileBuffer.append(f'T{self.tempVarCount} = {self.poppedSymbols[0].attribute} {self.poppedSymbols[1].attribute} {self.poppedSymbols[2].attribute};')
            self.tempVarCount+=1
        else:
            print(f'Erro: Operandos com tipos incompatíveis. linha {self.lineIndex}, coluna {self.columnIndex}')
            self.createFile = False
            
    def rule21(self):
        obj: SymbolObject = self.poppedSymbols[0]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type))
        
    def rule22(self):
        idLexeme: SymbolObject = self.poppedSymbols[0].attribute
        for token in SymbolTable.idTable:
            if token.lexeme == idLexeme:
                self.semanticStack.append(SymbolObject(self.leftSide, idLexeme, token.lexemeType))
                break
        else:
            print(f'Erro: Variável não declarada. linha: {self.lineIndex}, coluna: {self.columnIndex}')
            self.createFile = False
        
    def rule23(self):
        obj: SymbolObject = self.poppedSymbols[0]
        self.semanticStack.append(SymbolObject(self.leftSide, obj.attribute, obj.type))
        
    def rule25(self):
        self.fileBuffer.append('}')
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule26(self):
        self.semanticStack.append(SymbolObject(self.leftSide))
        self.fileBuffer.append(f'if ({self.poppedSymbols[2].attribute}) {{')
        
    def rule27(self):
        if self.poppedSymbols[0].type == self.poppedSymbols[2].type:
            self.fileBuffer.append(f'T{self.tempVarCount} = {self.poppedSymbols[0].attribute} {self.poppedSymbols[1].attribute}{self.poppedSymbols[2].attribute};')
            self.semanticStack.append(SymbolObject(self.leftSide, f'T{self.tempVarCount}'))
            self.tempVarCount+=1
        else:
            print(f'Erro: Operandos com tipos incompatíveis. linha {self.lineIndex}, coluna {self.columnIndex}\n')
            self.createFile = False
            
    def rule32(self):
        self.fileBuffer.append('}')
        self.semanticStack.append(self.leftSide)
    
    def rule33(self):
        self.fileBuffer.append(f'while({self.poppedSymbols[2].attribute}) {{')
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule34(self):
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule35(self):
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule36(self):

        self.semanticStack.append(SymbolObject(self.leftSide))
        
    def rule37(self):
        self.semanticStack.append(SymbolObject(self.leftSide))
        
    