from PyQt5.QtWidgets import QDialog
from simuload.user_interface.components.carga_nova import Ui_NovaCarga


class LoadWindow(QDialog):
    def __init__(self, parent, edit=None):
        super().__init__()
        self.edit = edit
        self.ui = Ui_NovaCarga()
        self.ui.setupUi(self)
        self.parent = parent
        self.service = parent.service
        self.set_connections()
        self.get_equipamentos()

    def set_connections(self):

        if self.edit:
            self.ui.buttonBox.accepted.connect(self.update_load)
        else:
            self.ui.buttonBox.accepted.connect(self.create_load)

        self.ui.buttonBox.rejected.connect(self.close)

        self.ui.addOne.clicked.connect(self.add_one_equip)
        self.ui.addMany.clicked.connect(self.add_many_equip)
        self.ui.removeEquip.clicked.connect(self.remove_equip)

    def input_info(self):
        return {"Nome": self.ui.carga_nome.text()}

    def set_input_info(self, load):
        self.ui.carga_nome.setText(str(load[1]))

    def update_load(self):
        load_id = self.edit
        try:
            self.service.modificar_carga(load_id, self.input_info())
            self.close()
        except Exception as e:
            print(e)
        self.parent.get_load()

    def create_load(self):

        try:
            self.service.inserir_carga(self.input_info())
            self.close()
        except Exception as e:
            print(e)
        self.parent.get_load()

    def get_equipamentos(self):
        self.equipamentos = self.service.consultar_equipamentos(consulta="")
        self.add_itens()

    def add_itens(self):
        self.ui.equipList.clear()
        for equip in self.equipamentos:
            equip_label = str(equip[0]) + " - " + equip[1]
            self.ui.equipList.insertItem(equip[0], equip_label)

    def add_one_equip(self):
        list_items = self.ui.equipList.selectedItems()
        if not list_items:
            return
        for item in list_items:
            equip = item.text() + " (1)"
            self.ui.addedEquipList.addItem(equip)

    def add_many_equip(self):
        list_items = self.ui.equipList.selectedItems()
        if not list_items:
            return
        for item in list_items:
            qty = self.ui.equipNum.text()
            equip = item.text() + f" ({qty})"
            self.ui.addedEquipList.addItem(equip)

    def remove_equip(self):
        list_items = self.ui.addedEquipList.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.ui.addedEquipList.takeItem(self.ui.addedEquipList.row(item))
