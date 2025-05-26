from Parser.Parser import Parser
from scanner.scanner import Scanner
from SymbolTable.symbolTable import SymbolTable
import traceback

if __name__ == "__main__":

    _scanner = Scanner()

    try:
         while (token:= _scanner.requestToken()):
             if not isinstance(token, bool):
                 print(token.toString())
        
    except Exception as e:
       #print( error or "análise léxica concluída")
       print("análise léxica concluída")
    
    SymbolTable.printTable()