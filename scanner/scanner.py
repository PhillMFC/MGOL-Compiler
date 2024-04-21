import numpy as np
from AFD.q0 import afd

file = open('Compiler\scanner\mgol_sample.txt','r')

def lineTreatment(line: list[str]) -> list[str]:
    _newline: list[str] = np.array(list(line))    
    return _newline

for line in file.readlines():
    afd(lineTreatment(line))