import numpy as np
class Equipamento: 
    
    def __init__(self,carga_id:int):
        self._nome = None
        self._carga_id = carga_id
        self._equipamento_id = None
        self._potencia = None
        self._fator_potencia = None
        self._uso_diario = None
        self._quantidade = None    
        
    @property
    def nome(self):
        """Nome do Tipo de Equipamento"""
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def carga_id(self):
        return self._carga_id
    
    @property
    def equipamento_id(self):
        return self._equipamento_id
    @equipamento_id.setter
    def equipamento_id(self,id):
        self._equipamento_id = id
        
    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self,potencia:float):
        self._potencia = potencia
        
    @property
    def fator_potencia(self):
        return self._fator_potencia
    @fator_potencia.setter
    def fator_potencia(self,fator_potencia:float):
        if fator_potencia >= 0:
            self._fator_potencia = fator_potencia
        else:
            print('Fator de Potência inválido')
        
    @property
    def uso_diario(self):
        return self._uso_diario
    @uso_diario.setter
    def uso_diario(self,uso_diario:str):
        
        faixas_horarios = uso_diario.split(',')
        horarios = [faixa.split(':') for faixa in faixas_horarios]
        
        uso_diario = np.zeros((24))
        
        for faixa in horarios:
            start = int(faixa[0])
            end = int(faixa[-1])
            uso_diario[start:end] = 1
        
        self._uso_diario = uso_diario
        
    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self,quantidade: int):
        if quantidade > 0:
            self._quantidade = quantidade
    
    
    
    
if __name__=='__main__':
    lampada = Equipamento(1234)
    print(lampada._carga_id)
    print(lampada._nome)
    lampada.nome = 'Lampada 60W'
    print(lampada.nome)
    

        

    
    
