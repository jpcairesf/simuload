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
        self.model.inserir_equipamento((nome, potencia, fator_potencia, uso_diario))

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