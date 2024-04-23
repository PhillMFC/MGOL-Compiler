from contextvars import Token
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

def afd(line: list[str]) -> str:
    for lexeme in line:
        if lexeme == range(0,9):
            ver_q19(lexeme, currentState)
        elif lexeme == '"':
            ver_q5(lexeme, currentState)
        elif lexeme.isalpha():
            ver_q6(lexeme, currentState)
        elif lexeme == "{":
            ver_q2(lexeme, currentState)
        elif lexeme == '$':
            ver_q3()
        elif lexeme == ("<" or '=' or '>'):
            ver_q8(lexeme, currentState)
        elif lexeme == ("+" or '-' or '*' or '/'):
            ver_q18(lexeme, currentState)
        elif lexeme == '(':
            ver_q16(lexeme, currentState)
        elif lexeme == ')':
            ver_q15(lexeme, currentState)
        elif lexeme == ',':
            ver_q7(lexeme, currentState)
        else:
            return "ERRO - afd"
       
def ver_q2(lexeme):
    if lexeme == '{':
        comment = '{'
        for word in line:
            comment = comment + ' ' + word
            

        comment = ' ' + '}'

def ver_q3(lexeme):
    return 'EOF'

def ver_q5(lexeme):
    print('no script')

def ver_q6(lexeme):
    print('no script')

def ver_q7(lexeme):
    print(currentState)

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

def ver_q8(lexeme):
    print('no script')