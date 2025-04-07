from AFD.afd import Afd
from SymbolTable.symbolTable import SymbolTable
from Token.token import Token
import traceback

class Scanner:

    lineIndex: int = 0
    columnIndex: int = 0
    currentChar = ''
    file: list[str] = ''
    afd: Afd = Afd()
    token = None
    _isPastTokenFaca = False
    _isPastTokenHifen = False
    

    @classmethod
    def setFile(self):
        file = open('scanner\mgol_sample.txt','r', encoding='utf-8')
        self.file = list(file)
        file.close()
        self.file[-1] = self.file[-1] + '\n'
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
        try:
            if self.token.lexemeClass == 'ERRO':
                self.nextChar()
        except:
            ()

    @classmethod
    def requestToken(self):
        self.token = None
        if not self.file:
            self.setFile()
            self.currentChar = self.file[self.lineIndex][self.columnIndex]       
            
        self.generateToken()
        self.afd.resetAfd()

        try:
            self.token = self.facaAteToken(self.token)
            SymbolTable.setIdValue(self.token)
            return self.token
        except Exception as e:
            return True
            

    @classmethod
    def facaAteToken(self, token: Token):
        if not isinstance(token, bool):
            if token.lexeme == 'faca':
                self._isPastTokenFaca = True
                return True
            elif token.lexeme == '-' and self._isPastTokenFaca:
                self._isPastTokenHifen = True
                return True
            elif token.lexeme == 'ate' and self._isPastTokenFaca and self._isPastTokenHifen:
                return Token('faca-ate', 'q6',self.token.lineIndex, self.token.columnIndex)
            else: 
                self._isPastTokenFaca = False
                self._isPastTokenHifen = False
                return token
                