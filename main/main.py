from scanner.scanner import Scanner
from SymbolTable.symbolTable import SymbolTable

if __name__ == "__main__":

    try:
        while Scanner.generateToken():
            ()
        

    except:
        SymbolTable.printTable()