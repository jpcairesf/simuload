from PyQt5.QtWidgets import QDialog
from simuload.user_interface.components.carga_nova import Ui_NovaCarga
import re


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
            self.carga_id = self.edit
            self.get_equip_in_load(self.carga_id)
            
        else:
            self.ui.buttonBox.accepted.connect(self.create_load)
            self.carga_id = self.service.last_id_table("carga_equipamento")

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
            self.add_equip_in_load()
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

    def get_selected_equips(self):
        list_items = self.ui.equipList.selectedItems()
        if not list_items:
            return []
        return list_items

    def add_one_equip(self):
        for item in self.get_selected_equips():
            equip = item.text() + " [1]"
            self.ui.addedEquipList.addItem(equip)

    def add_many_equip(self):
        for item in self.get_selected_equips():
            qty = self.ui.equipNum.text()
            equip = item.text() + f" [{qty}]"
            self.ui.addedEquipList.addItem(equip)

    def get_selected_added(self):
        list_items = self.ui.addedEquipList.selectedItems()
        if not list_items:
            return []
        return list_items

    def remove_equip(self):
        for item in self.get_selected_added():
            self.ui.addedEquipList.takeItem(self.ui.addedEquipList.row(item))

    def get_added_equips(self):
        return [
            self.ui.addedEquipList.item(row)
            for row in range(self.ui.addedEquipList.count())
        ]

    def add_equip_in_load(self):
        for equip in self.get_added_equips():
            text = equip.text()
            equip_id = int(text.split(" - ")[0])
            qtd = int(re.search(r"(?<=\[).+?(?=\])", text).group())
            self.service.inserir_equip_na_carga(self.carga_id, equip_id, qtd)

    def get_equip_in_load(self,carga_id):
        print(self.service.consultar_equip_na_carga(carga_id))
        return self.service.consultar_equip_na_carga(carga_id)