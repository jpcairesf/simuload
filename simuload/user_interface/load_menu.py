from PyQt5.QtWidgets import QWidget
from simuload.user_interface.components.carga_menu import Ui_MenuCarga
from simuload.user_interface.load_window import LoadWindow


class LoadMenu(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.ui = Ui_MenuCarga()
        self.ui.setupUi(self)

        self.parent = parent
        self.service = self.parent.service

        self.set_connections()
        self.get_load()

        self.widget = None

    def set_connections(self):
        self.ui.procurarBotao.clicked.connect(self.get_load)
        self.ui.NovaCarga.clicked.connect(self.create_load)
        self.ui.EditarCarga.clicked.connect(self.edit_load)
        self.ui.ExcluirCarga.clicked.connect(self.delete_load)

    def get_load(self):
        load = self.ui.procuraCarga.text()
        self.loads = self.service.consultar_carga(load)
        self.add_itens()

    def add_itens(self):
        self.ui.cargaLista.clear()
        for load in self.loads:
            load_label = str(load[0]) + " - " + load[1]
            self.ui.cargaLista.insertItem(load[0], load_label)

    def get_selected_load(self):
        load_label = self.ui.cargaLista.selectedItems()[0].text()
        return int(load_label.split(" - ")[0])

    def delete_load(self):
        load_id = self.get_selected_load()
        self.service.remover_carga(load_id)
        self.service.remover_equip_na_carga(load_id)
        self.get_load()

    def edit_load(self):
        carga_id = self.get_selected_load()
        load = self.service.consultar_carga_id(carga_id)

        self.widget = LoadWindow(parent=self, edit=carga_id)
        self.widget.set_input_info(load)
        self.widget.show()

    def create_load(self):
        self.widget = LoadWindow(self)
        self.widget.show()
