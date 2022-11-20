import numpy as np
import re


def input_type(text: str):
    in_array = re.search(r"(?<=\[).+?(?=\])", text)
    if not in_array:
        text = horario_parse(text)
    return text
    
def horario_parse(horario: str):
    faixas_horarios = horario.split(",")
    horarios = [faixa.split(":") for faixa in faixas_horarios]
    uso_diario = np.zeros((24))
    for faixa in horarios:
        start = int(faixa[0])
        end = int(faixa[-1])
        uso_diario[start: end + 1] = 1
    uso_diario = np.array_str(uso_diario)
    return uso_diario
