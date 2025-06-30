class Semantic:
    def __init__(self):
        self.semanticStack: list[str]
        self.rules: dict = {
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
            33:self.rule33,
            34:self.rule34,
            35:self.rule35,
            36:self.rule36,
            37:self.rule37
        }
        self.fileBuffer = []
        self.file = self.createFile()
        self.syntaxRule = None
        
    @classmethod
    def createFile(self):
        with open("program.c", 'w') as emptyFile:
            pass
    
    @classmethod
    def executeRule(self, ruleNumber: int):
        if ruleFunction := self.rules.get(ruleNumber, None):
            ruleFunction()
    
    @classmethod    
    def addToStack(self, value):
        self.semanticStack.append(value)
        
    @classmethod
    def writeToFileBuffer(self, text: str):
        self.fileBuffer.append(text)
    
    @classmethod
    def rule5(self):
        ()
    
    @classmethod
    def rule6(self):
        ()
        
    @classmethod
    def rule7(self):
        ()
        
    @classmethod
    def rule8(self):
        ()
        
    @classmethod
    def rule9(self):
        ()
        
    @classmethod
    def rule10(self):
        ()
        
    @classmethod
    def rule11(self):
        ()
    
    @classmethod
    def rule13(self):
        ()
        
    @classmethod
    def rule14(self):
        ()
        
    @classmethod
    def rule15(self):
        ()
        
    @classmethod
    def rule16(self):
        ()
        
    @classmethod
    def rule17(self):
        ()
        
    @classmethod
    def rule19(self):
        ()
        
    @classmethod
    def rule20(self):
        ()
        
    @classmethod
    def rule21(self):
        ()
        
    @classmethod
    def rule22(self):
        ()
        
    @classmethod
    def rule23(self):
        ()
        
    @classmethod
    def rule25(self):
        ()
        
    @classmethod
    def rule26(self):
        ()
        
    @classmethod
    def rule27(self):
        ()
        
    @classmethod
    def rule33(self):
        ()
    @classmethod
    def rule34(self):
        ()
        
    @classmethod
    def rule35(self):
        ()
        
    @classmethod
    def rule36(self):
        ()
        
    @classmethod
    def rule37(self):
        ()
        
    