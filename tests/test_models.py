import pytest
import sys
import os
import numpy as np

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from src.models.equipamento import Equipamento

equip = None

def setup_module(module):
    global equip
    equip = Equipamento(carga_id = 12345)

def test_equipamentos_id():
    assert equip.carga_id == 12345
    
def test_equipamento_propriedades_vazias():
    assert equip.nome == None
    assert equip.potencia == None
    assert equip.fator_potencia == None
    assert equip.uso_diario == None
    assert equip.quantidade == None

def test_equipamento_propriedades():
    equip.nome = 'Lampada Incandescente'
    equip.potencia = 60
    equip.fator_potencia = 0.95
    equip.uso_diario = '0:2,7:9,10:15,23'
    equip.quantidade = 5
    
    assert equip.nome == 'Lampada Incandescente'
    assert equip.potencia == 60
    assert equip.fator_potencia == 0.95

    assert np.array_equal(equip.uso_diario, np.array([1,1,1,0,0,0,0,1,
                                                      1,1,1,1,1,1,1,1,
                                                      0,0,0,0,0,0,0,1]).reshape((24)))
    assert equip.quantidade == 5