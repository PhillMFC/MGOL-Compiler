from AFD.afd import Afd
from IdTable.idTable import IdTable

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
        self.file = self.file + ['$',' ']

    @classmethod
    def nextChar(self):
        if self.columnIndex + 1 == len(self.file[self.lineIndex]):
            self.columnIndex = 0
            self.lineIndex += 1
        else:
            self.columnIndex += 1

    @classmethod
    def generateToken(self):
        
        if not self.file:
            self.setFile()

        self.afd.setChar(self.file[self.lineIndex][self.columnIndex])

        while self.afd.verifyChar():
            try:
                self.nextChar()
                self.afd.setChar(self.file[self.lineIndex][self.columnIndex])
            except: 
                break

        try:
            self.token = getattr(self.afd, 'token')
            print(getattr(self.afd, 'token').__dict__)
            IdTable.verifyToken(self.token)
        except:
            ()
        self.afd.resetAfd()
        return self.token