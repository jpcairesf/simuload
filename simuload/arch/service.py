from simuload.arch.model import Model


class Service:
    def __init__(self):
        self.start_model()

    def start_model(self):
        self.model = Model()

    def inserir_equipamento(self, equipamento):
        
        nome = equipamento['Nome']
        potencia = equipamento['Potencia']
        fator_potencia = equipamento['FatorPotencia']
        uso_diario = equipamento['Uso']
        self.model.inserir_equipamento((nome,
                                        potencia,
                                        fator_potencia,
                                        uso_diario))
