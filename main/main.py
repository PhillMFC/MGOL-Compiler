from scanner.scanner import Scanner
from IdTable.idTable import IdTable

if __name__ == "__main__":

    try:
        while Scanner.generateToken():
            ()
        IdTable.printTable()

    except:
        print(IdTable.idTable)