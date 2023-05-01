from PyQt5.QtWidgets import QDialog
from simuload.user_interface.components.novo_transformador import Ui_NovoTransformador


class TransformadorWindow(QDialog):
    def __init__(self, parent, edit=None):
        super().__init__()
        self.edit = edit
        self.ui = Ui_NovoTransformador()
        self.ui.setupUi(self)
        self.parent = parent
        self.service = parent.service
        self.set_connections()

    def set_connections(self):
        if self.edit:
            self.ui.buttonBox.accepted.connect(self.update_transformador)
        else:
            self.ui.buttonBox.accepted.connect(self.create_transformador)

        self.ui.buttonBox.rejected.connect(self.close)

    def input_info(self):
        return {
            "Nome": self.ui.transf_nome.text(),
            "Demanda": self.ui.transf_demanda.text(),
            "Fornecimento": self.ui.transf_fornecimento.text()
        }

    def set_input_info(self, transformador):
        self.ui.transf_nome.setText(str(transformador[1]))
        self.ui.transf_demanda.setText(str(transformador[2]))
        self.ui.transf_fornecimento.setText(str(transformador[3]))

    def update_transformador(self):
        transf_id = self.edit
        try:
            self.service.modificar_transformador(transf_id, self.input_info())
        except Exception as e:
            print(e)
        self.parent.get_transformadores()

    def create_transformador(self):
        try:
            self.service.inserir_transformador(self.input_info())
        except Exception as e:
            print(e)
        self.parent.get_transformadores()
