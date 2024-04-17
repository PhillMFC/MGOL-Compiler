from AFD.ab_p import ver_ab_p
from AFD.comment import ver_comment
from AFD.eof import ver_eof
from AFD.id import ver_id
from AFD.lit import ver_lit
from AFD.num import ver_num
from AFD.opm import ver_opm
from AFD.opr_rcb import ver_opr_rcb
from AFD.pt_v import ver_pt_v
from AFD.vir import ver_vir



def afd(line):
    for position in line:
        for char in position:
            if char == range(0,9):
                ver_num(position)
            elif char == '"':
                ver_lit(position)
            elif char == range(65,91) | range(97,123):
                ver_id(position)
            elif char == "{":
                ver_comment(position)
            elif char == '$':
                ver_eof()
            elif char == "<" | '=' | '>':
                ver_opr_rcb(position)
            elif char == "+" | '-' | '*' | '/':
                ver_opm(char)
            elif char == '(':
                ver_ab_p()
            elif char == ')':
                ver_pt_v()
            elif char == ',':
                ver_vir()
            else:
                return "ERRO - afd"
            