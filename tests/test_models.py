import pytest
import sys
import os
import numpy as np

from models.equipamento import Equipamento

equip = None

def setup_module(module):
    global equip
    equip = Equipamento(equipamento_id = 12345)

def test_equipamentos_id():
    assert equip.id == 12345
    
def test_equipamento_propriedades_vazias():
    assert equip.nome == None
    assert equip.potencia == None
    assert equip.fator_potencia == None
    assert equip.uso_diario == None

def test_equipamento_propriedades():
    equip.nome = 'Lampada Incandescente'
    equip.potencia = 60
    equip.fator_potencia = 0.95
    equip.uso_diario = '0:2,7:9,10:15,23'
    
    assert equip.nome == 'Lampada Incandescente'
    assert equip.potencia == 60
    assert equip.fator_potencia == 0.95

    assert np.array_equal(equip.uso_diario, np.array([1,1,1,0,0,0,0,1,
                                                      1,1,1,1,1,1,1,1,
                                                      0,0,0,0,0,0,0,1]).reshape((24)))
