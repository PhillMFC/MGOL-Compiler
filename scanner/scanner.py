from AFD.afd import Afd
from Token.token import Token

class Scanner:

    lineIndex: int = 0
    columnIndex: int = 0
    file: list[str] = ''
    afd: Afd = Afd()
    token = None

    @classmethod
    def setFile(self):
        file = open('scanner\mgol_sample.txt','r', encoding='utf-8')
        self.file = list(file)
        file.close()

    @classmethod
    def nextChar(self):
        if self.columnIndex + 1 == len(self.file[self.lineIndex]):
            self.columnIndex = 0
            self.lineIndex += 1
        elif self.lineIndex + 1 == len(self.file):
            self.afd.setChar('$')
            self.afd.verifyChar()
        else:
            self.columnIndex += 1

    @classmethod
    def generateToken(self):
        if not self.file:
            self.setFile()

        self.afd.setChar(self.file[self.lineIndex][self.columnIndex])

        while self.afd.verifyChar():
            self.nextChar()
            self.afd.setChar(self.file[self.lineIndex][self.columnIndex])

        print(getattr(self.afd, 'token'))
        self.afd.resetAfd()