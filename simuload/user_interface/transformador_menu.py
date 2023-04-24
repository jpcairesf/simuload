from PyQt5.QtWidgets import QWidget
from simuload.user_interface.components.transformador_menu import Ui_MenuTransformador
from simuload.user_interface.transformador_window import TransformadorWindow

class TransformadorMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        self.ui = Ui_MenuTransformador()
        self.ui.setupUi(self)

        self.parent = parent
        self.service = self.parent.service

        self.set_connections()
        self.get_transformadores()

        self.widget = None
    
    def set_connections(self):
        self.ui.procurarBotao.clicked.connect(self.get_transformadores)
        self.ui.NovoTransformador.clicked.connect(self.create_transf)
        self.ui.EditarTransformador.clicked.connect(self.edit_transf)
        self.ui.ExcluirTransformador.clicked.connect(self.delete_transf)

    def get_transformadores(self):
        transf = self.ui.procuraTransf.text()
        self.transformadores = self.service.consultar_transformador(transf)
        self.add_itens()
        self.parent.get_transformadores()

    def add_itens(self):
        self.ui.transformadorLista.clear()
        for transf in self.transformadores:
            transf_label = str(transf[0]) + " - " + transf[1]
            self.ui.transformadorLista.insertItem(transf[0], transf_label)

    def get_selected_transf(self):
        transf_label = self.ui.transformadorLista.selectedItems()[0].text()
        return int(transf_label.split(" - ")[0])

    def delete_transf(self):
        transf_id = self.get_selected_transf()
        self.service.remover_transformador(transf_id)
        self.get_transformadores()

    def create_transf(self):
        self.widget = TransformadorWindow(self)
        self.widget.show()
        self.get_transformadores()


    def edit_transf(self):
        transf_id = self.get_selected_transf()
        transformador = self.service.consultar_transformador_id(transf_id)

        self.widget = TransformadorWindow(parent=self, edit=transf_id)
        self.widget.set_input_info(transformador)
        self.widget.show()
        self.get_transformadores()