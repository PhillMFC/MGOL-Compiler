from scanner.scanner import Scanner
from SymbolTable.symbolTable import SymbolTable
import traceback

if __name__ == "__main__":

    _scanner = Scanner()
    try:
        while (token := _scanner.requestToken()):
            if not isinstance(token, bool):
                print('main-scope', token.toString())
            
                
    
        SymbolTable.printTable()

    except Exception as e:
       print("código compilado")