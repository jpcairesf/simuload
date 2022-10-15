class Carga:
    
    def __init__(self,carga_id):
        self._carga_id = carga_id
        self._nome = None
        self._equipamentos = []
        
    @property
    def id(self):
        return self._carga_id
    
    @property
    def nome(self):
        """Nome do Tipo de Carga"""
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def adicionar_equipamentos(self, equipamento_id, quantidade):
        self._equipamentos.append([equipamento_id,quantidade])
