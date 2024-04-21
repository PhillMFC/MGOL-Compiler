from contextvars import Token
import numpy as np



file = open('MGOL-Compiler\mgol_sample.txt','r')

def lineTreatment(line: list[str]) -> list[str]:
    _newline: list[str] = np.array(list(line))    
    return _newline

for line in file.readlines():
    print(line)