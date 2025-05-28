class Error:
    
    mapErrors = []

    @classmethod
    def raiseErrorMessage(self, lineIndex, columnIndex, message):
        errorMessage = f'\n{message}. Linha: {lineIndex} Coluna: {columnIndex+1}\n'
        
        if not errorMessage in self.mapErrors:
            print(f'\n{message}. Linha: {lineIndex} Coluna: {columnIndex+1}\n')
            self.mapErrors.append(errorMessage)

        

