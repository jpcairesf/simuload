from PyQt5.QtWidgets import QDialog
from simuload.user_interface.components.curva_nova import Ui_NovaCurva
import re


class CurveWindow(QDialog):
    def __init__(self, parent, edit=None):
        super().__init__()
        self.edit = edit
        self.ui = Ui_NovaCurva()
        self.ui.setupUi(self)
        self.parent = parent
        self.service = parent.service
        self.set_connections()
        self.get_cargas()

    def set_connections(self):

        if self.edit:
            self.curve_id = self.edit
            self.get_load_in_curve(self.curve_id)
            self.ui.buttonBox.accepted.connect(self.update_curve)

        else:
            self.ui.buttonBox.accepted.connect(self.create_curve)

        self.ui.buttonBox.rejected.connect(self.close)

        self.ui.addOne.clicked.connect(self.add_one_load)
        self.ui.addMany.clicked.connect(self.add_many_load)
        self.ui.removeLoad.clicked.connect(self.remove_load)

    def input_info(self):
        return {"Nome": self.ui.curva_nome.text()}

    def set_input_info(self, curve):
        self.ui.curva_nome.setText(str(curve[1]))

    def update_curve(self):
        curve_id = self.edit
        try:
            self.service.modificar_curva(curve_id, self.input_info())
            self.service.remover_carga_na_curva(curve_id)
            self.add_load_in_curve()
            self.close()
        except Exception as e:
            print(e)
        self.parent.get_curvas()

    def create_curve(self):

        try:
            self.curve_id = self.service.inserir_curva(self.input_info())
            self.add_load_in_curve()
            self.close()
        except Exception as e:
            print(e)
        self.parent.get_curvas()

    def get_cargas(self):
        self.cargas = self.service.consultar_carga(consulta="")
        self.add_itens()

    def add_itens(self):
        self.ui.loadList.clear()
        for load in self.cargas:
            load_label = str(load[0]) + " - " + load[1]
            self.ui.loadList.insertItem(load[0], load_label)

    def get_selected_loads(self):
        list_items = self.ui.loadList.selectedItems()
        if not list_items:
            return []
        return list_items

    def add_one_load(self):
        for item in self.get_selected_loads():
            load = item.text() + " [1]"
            self.ui.addedLoadList.addItem(load)

    def add_many_load(self):
        for item in self.get_selected_loads():
            qty = self.ui.loadNum.text()
            load = item.text() + f" [{qty}]"
            self.ui.addedLoadList.addItem(load)

    def get_selected_added(self):
        list_items = self.ui.addedLoadList.selectedItems()
        if not list_items:
            return []
        return list_items

    def remove_load(self):
        for item in self.get_selected_added():
            self.ui.addedLoadList.takeItem(self.ui.addedLoadList.row(item))

    def get_added_loads(self):
        return [
            self.ui.addedLoadList.item(row)
            for row in range(self.ui.addedLoadList.count())
        ]

    def add_load_in_curve(self):
        for load in self.get_added_loads():
            text = load.text()
            load_id = int(text.split(" - ")[0])
            qtd = int(re.search(r"(?<=\[).+?(?=\])", text).group())
            self.service.inserir_carga_na_curva(self.curve_id, load_id, qtd)

    def get_load_in_curve(self, curve_id):
        added_load = self.service.consultar_curva_carga(curve_id)
        self.ui.addedLoadList.clear()

        for load in added_load:
            added_load_label = str(load[0]) + " - " + load[1] + f" [{load[2]}]"
            self.ui.addedLoadList.insertItem(load[0], added_load_label)
