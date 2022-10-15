from simuload.utils.parsers import horario_parse

class Equipamento: 
    
    def __init__(self,equipamento_id):
        self._equipamento_id = equipamento_id
        self._nome = None
        self._potencia = None
        self._fator_potencia = None
        self._uso_diario = None
    
    @property
    def id(self):
        return self._equipamento_id
    
    @property
    def nome(self):
        """Nome do Tipo de Equipamento"""
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def potencia(self):
        """Potência Elétrica do Equipamento em Watts"""
        return self._potencia
    @potencia.setter
    def potencia(self,potencia:float):
        self._potencia = potencia
        
    @property
    def fator_potencia(self):
        """Fator de Potência Elétrica do Equipamento"""
        return self._fator_potencia
    @fator_potencia.setter
    def fator_potencia(self,fator_potencia:float):
        if fator_potencia >= 0:
            self._fator_potencia = fator_potencia
        else:
            print('Fator de Potência inválido')
        
    @property
    def uso_diario(self):
        """Horas em que o equipamento são usados"""
        return self._uso_diario
    @uso_diario.setter
    def uso_diario(self,uso_diario:str):
        self._uso_diario = horario_parse(uso_diario)
        
    

        

    
    
