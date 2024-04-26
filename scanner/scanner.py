import numpy as np

file = open('Compiler\scanner\mgol_sample.txt','r', encoding='utf-8')

def lexemeTreatment(line: list[str]) -> list[str]:
    charLine: list[str] = np.array(list(line))
    word: str = ''
    _newline: list[str] = []
    
    for char in charLine:
        asciiChar = ord(char)
        if asciiChar in range(65,91) or asciiChar in range(97, 123):
            word += char
        else:
            if(word.isalpha()):
                _newline.append(word)
                word = ''
            _newline.append(char)
            
    return _newline

for line in file.readlines():
    print(lexemeTreatment(line))