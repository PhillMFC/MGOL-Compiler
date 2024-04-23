from symbol_table.token import Token
import numpy as np
from AFD.q16 import ver_ab_p
from AFD.q3 import ver_eof
from AFD.q6 import ver_id
from AFD.q5 import ver_lit
from AFD.q19 import ver_num
from AFD.q18 import ver_opm
from AFD.opr_rcb import ver_opr_rcb
from AFD.q15 import ver_pt_v
from AFD.q7 import ver_vir

currentState: str = 'q0'
concatLexeme: str = ''

def afd(line: list[str]) -> str:
    for lexeme in line:
        if currentState == 'q0':
            q0(lexeme)
        if currentState == 'q1':
            concatLexeme += lexeme
            if lexeme == '}':
                currentState ='q2'
                ver_q2(concatLexeme)
                concatLexeme = ''
        if currentState == 'q4':
            concatLexeme += lexeme
            if lexeme == '"':
                currentState ='q5'
                ver_q5(concatLexeme)
                concatLexeme = ''
        if currentState == 'q6':
            if lexeme == range(0,9):
                concatLexeme += lexeme
            elif lexeme.isalpha():
                concatLexeme += lexeme
            elif lexeme == '_':
                concatLexeme += lexeme
            else:
                ver_q6(concatLexeme)
                concatLexeme = ''
                q0(lexeme)
        if currentState == 'q8':
            if lexeme == '=' and concatLexeme == '<':
                concatLexeme += lexeme
                ver_q8(concatLexeme)
            elif lexeme == '-' and concatLexeme == '<':
                concatLexeme += lexeme
                ver_q10(concatLexeme)
            elif lexeme == '>' and concatLexeme == '<':
                concatLexeme += lexeme
                ver_q8(concatLexeme)
            elif lexeme == '=' and concatLexeme == '>':
                concatLexeme += lexeme
                ver_q8(concatLexeme)
            else:
                ver_q8(concatLexeme)
        if currentState == 'q19':
            if int(lexeme) == range(0,9):
                concatLexeme += lexeme
            if lexeme == '.':
                currentState = 'q20'
                concatLexeme += lexeme
            else:
                ver_num()
        if currentState == 'q20':
            if int(lexeme) == range(0,9):
                concatLexeme += lexeme
            if lexeme == 'E' or 'e':
                concatLexeme += lexeme
                currentState = 'q21'
            else:
                ver_num()
        if currentState == 'q21':
            if lexeme == '+' or '-':
                concatLexeme += lexeme
                currentState == 'q22'
            if int(lexeme) == range(0,9):
                concatLexeme += lexeme
                currentState = 'q22'
            else:
                ver_num()
        if currentState == 'q22':
            if int(lexeme) == range(0,9):
                concatLexeme += lexeme
            else:
                ver_num()

def q0(lexeme:str):
    if int(lexeme) == range(0,9):
        currentState = 'q19'
        concatLexeme += lexeme
    elif lexeme == '"':
        currentState = 'q4'
        concatLexeme += lexeme
    elif lexeme.isalpha():
        currentState = 'q6'
        concatLexeme += lexeme
    elif lexeme == "{":
        currentState = 'q1'
        concatLexeme += lexeme
    elif lexeme == '$':
        ver_q3()
    elif lexeme == ("<" or '>'):
        currentState = 'q8'
        concatLexeme += lexeme
    elif lexeme == '=':
        ver_q12()
    elif lexeme == ("+" or '-' or '*' or '/'):
        ver_q18(lexeme)
    elif lexeme == '(':
        ver_q16()
    elif lexeme == ')':
        ver_q17()
    elif lexeme == ';':
        ver_q15()
    elif lexeme == ',':
        ver_q7()
    else:
        return "ERRO - afd"

def ver_q2(concatLexeme):
    if lexeme == '{':
        comment:str = '{'
        for word in line:
            comment = comment + ' ' + word
            

        comment = ' ' + '}'

def ver_q3(lexeme):
    return 'EOF'
    currentState = 'q0'

def ver_q5(concatLexeme):
    print('no script')
    currentState = 'q0'

def ver_q6(lexeme):
    print('no script')
    currentState = 'q0'

def ver_q7(lexeme):
    print(currentState)
    currentState = 'q0'

def ver_q15(lexeme):
    return ('pt_v', ';')

def ver_q16(lexeme):
    return ('ab_p', '(')

def ver_q17(lexeme):
    return ('fc_p', ')')

def ver_q18(lexeme):
    return ('opm', char)

def ver_q19(lexeme):
    return

def ver_q8(lexeme:str):
    currentState = 'q8'
    if lexeme == '<':

        ver_q9()
        
def ver_q9(lexeme:str):
    currentState = 'q9'
