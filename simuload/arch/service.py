from simuload.arch.model import Model


class Service:
    def __init__(self):
        self.start_model()

    def start_model(self):
        self.model = Model()

    def inserir_equipamento(self, equipamento: dict):

        nome = equipamento["Nome"]
        potencia = equipamento["Potencia"]
        fator_potencia = equipamento["FatorPotencia"]
        uso_diario = equipamento["Uso"]
        self.model.inserir_equipamento((nome,
                                        potencia,
                                        fator_potencia,
                                        uso_diario))

    def consultar_equipamentos(self, consulta: str = ""):
        return self.model.consultar_equipamentos_registros_nome(consulta)

    def consultar_equipamento_id(self, equip_id: int):
        return self.model.consultar_equipamento_pela_id(equip_id)

    def modificar_equipamento(self, equip_id, equipamento: dict):

        nome = equipamento["Nome"]
        potencia = equipamento["Potencia"]
        fator_potencia = equipamento["FatorPotencia"]
        uso_diario = equipamento["Uso"]
        self.model.modificar_equipamento(
            equip_id, (nome, potencia, fator_potencia, uso_diario)
        )

    def remover_equipamento(self, equip_id):

        self.model.remover_equipamento(equip_id)

    def inserir_carga(self, carga: dict):

        nome = carga["Nome"]
        self.model.inserir_carga((nome))

    def consultar_carga(self, consulta: str = ""):
        return self.model.consultar_cargas_registros_nome(consulta)

    def consultar_carga_id(self, carga_id: int):
        return self.model.consultar_carga_pela_id(carga_id)

    def modificar_carga(self, carga_id, carga: dict):

        nome = carga["Nome"]
        self.model.modificar_carga(carga_id, (nome))

    def remover_carga(self, carga_id):
        self.model.remover_carga(carga_id)

    def last_id_carga_equipamento(self):
        last_id = (
            1
            if not self.model.last_id_carga_equipamento()
            else self.model.last_id_carga_equipamento()
        )
        return last_id

    def inserir_equip_na_carga(self, carga_id: int, equip_id: int, qtd: int):
        return self.model.inserir_equipamento_na_carga(carga_id, equip_id, qtd)

    def remover_equip_na_carga(self, carga_id):
        self.model.remover_equip_na_carga(carga_id)

    def consultar_equip_na_carga(self, carga_id):
        return self.model.consultar_carga_equipamentos(carga_id)

    def inserir_curva(self, curva: dict):
        nome = curva["Nome"]
        self.model.inserir_curva(nome)
        
    def consultar_curva_pela_id(self, rowid):
        return self.model.consultar_curva_pela_id(rowid)
    
    def consultar_curva(self, consulta: str = ""):
        return self.model.consultar_curvas_registros_nome(consulta)
    
    def modificar_curva(self, rowid, curva: dict):
        nome = curva["Nome"]
        self.model.modificar_curva(rowid, nome)        
        
    def remover_curva(self, rowid):
        self.model.remover_curva(rowid)
    
    def consultar_curva_carga(self, curva_id):
        return self.model.consultar_curva_carga(curva_id)
    
    def inserir_carga_na_curva(self, curva_id, carga_id, qtd):
        self.model.inserir_carga_na_curva(curva_id, carga_id, qtd)
    
    def remover_carga_na_curva(self, curva_id):
        self.model.remover_carga_na_curva(curva_id)
    
    def last_id_curva_carga(self):
        last_id = (
            1
            if not self.model.last_id_curva_carga()
            else self.model.last_id_curva_carga()
        )
        return last_id
        