from contextvars import Token

class Table:
    _idVariableDict: dict = {}
    _keyWords: tuple = ("inicio","varinicio","varfim","escreva",
                        "leia","se","entao","fimse","repita",
                        "fimrepita","fim","inteiro","literal",
                        "real")

