class Exception:

    @classmethod
    def raiseErrorMessage(self, lineIndex, columnIndex, message=None) -> None:
        self.lineIndex = lineIndex
        self.columnIndex = columnIndex
        self.reportMessage = message

        print(message, f'Linha: {self.lineIndex+1} Coluna: {self.columnIndex+1}', end='\n')

