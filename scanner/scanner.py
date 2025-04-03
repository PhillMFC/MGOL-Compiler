from AFD.afd import Afd
from SymbolTable.symbolTable import SymbolTable
from Token.token import Token

class Scanner:

    lineIndex: int = 0
    columnIndex: int = 0
    currentChar = ''
    file: list[str] = ''
    afd: Afd = Afd()
    token = None

    @classmethod
    def setFile(self):
        file = open('scanner\mgol_sample.txt','r', encoding='utf-8')
        self.file = list(file)
        file.close()
        self.file = self.file + ['$\n']
        print(self.file)

    @classmethod
    def nextChar(self):
        if self.columnIndex + 1 == len(self.file[self.lineIndex]):
            self.columnIndex = 0
            self.lineIndex += 1
        else:
            self.columnIndex += 1
        
        self.currentChar = self.file[self.lineIndex][self.columnIndex]
    
    @classmethod
    def generateToken(self):
        while not self.token:
            self.afd.setChar(self.currentChar, self.lineIndex, self.columnIndex)    
            self.afd.verifyChar()
            self.token = self.afd.getToken()
            if not self.token:
                self.nextChar()
    
    @classmethod
    def requestToken(self):
        self.token = None
        if not self.file:
            self.setFile()
            self.currentChar = self.file[self.lineIndex][self.columnIndex]       
            
        self.generateToken()
        self.afd.resetAfd()

        try:
            SymbolTable.setIdValue(self.token)
            return self.token
        except:
            return True
            

