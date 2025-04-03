class Error:

    @classmethod
    def raiseErrorMessage(self, lineIndex, columnIndex, message):
        print(f'\n{message}. Linha: {lineIndex+1} Coluna: {columnIndex+1}\n')

        

