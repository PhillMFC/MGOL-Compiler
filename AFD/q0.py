from contextvars import Token
import numpy as np
from AFD.q16 import ver_ab_p
from AFD.q2 import ver_comment
from AFD.q3 import ver_eof
from AFD.q6 import ver_id
from AFD.q5 import ver_lit
from AFD.q19 import ver_num
from AFD.q18 import ver_opm
from AFD.opr_rcb import ver_opr_rcb
from AFD.q15 import ver_pt_v
from AFD.q7 import ver_vir


def afd(line: list[str]) -> str:

    lastChar: str = ''
    i=0
    for index,value in enumerate(line):
        print(value)
            


       
            