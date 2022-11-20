from simuload.arch.model import Model

import numpy as np


class CargaCalculator:
    def calcular_consumo(Model, carga: dict):
        consumo = np.zeros((24))
        equipamentos = Model().consultar_carga_equipamentos_consumo(carga["Id"])
        for equip in equipamentos:
            consumo += equip["Uso"]*equip["Potencia"]*equip["Qtd"]
        return consumo