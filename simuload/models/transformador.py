from simuload.utils.parsers import horario_parse


class Transformador:
    def __init__(self, transformador_id):
        self._transformador_id = transformador_id
        self._nome = None
        self._demanda = None
        self._fornecimento = None

    @property
    def id(self):
        return self._transformador_id

    @property
    def nome(self):
        """Nome do Tipo de Transformador"""
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def demanda(self):
        """Potência Elétrica do Equipamento em Watts"""
        return self._demanda

    @demanda.setter
    def demanda(self, demanda: float):
        self._demanda = demanda

    @property
    def fornecimento(self):
        """Horas em que o equipamento são usados"""
        return self._fornecimento

    @fornecimento.setter
    def fornecimento(self, fornecimento: str):
        self._fornecimento = horario_parse(fornecimento)
