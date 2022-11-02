from PyQt5.QtWidgets import QWidget
from simuload.user_interface.components.equipamento_menu import Ui_MenuEquipamento
from simuload.user_interface.equipment_window import EquipmentWindow


class EquipmentMenu(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.ui = Ui_MenuEquipamento()
        self.ui.setupUi(self)

        self.parent = parent
        self.service = self.parent.service

        self.set_connections()
        self.get_equipamentos()

        self.widget = None

    def set_connections(self):
        self.ui.procurarBotao.clicked.connect(self.get_equipamentos)
        self.ui.NovoEquipamento.clicked.connect(self.create_equip)
        self.ui.procurarBotao.clicked.connect(self.get_equipamentos)
        self.ui.EditarEquipamento.clicked.connect(self.edit_equip)
        self.ui.ExcluirEquipamento.clicked.connect(self.delete_equip)

    def get_equipamentos(self):
        equip = self.ui.procuraEquip.text()
        self.equipamentos = self.service.consultar_equipamentos(equip)
        self.add_itens()

    def add_itens(self):
        self.ui.equipamentoLista.clear()
        for equip in self.equipamentos:
            equip_label = str(equip[0]) + " - " + equip[1]
            self.ui.equipamentoLista.insertItem(equip[0], equip_label)

    def get_selected_equip(self):
        equip_label = self.ui.equipamentoLista.selectedItems()[0].text()
        return int(equip_label.split(" - ")[0])

    def delete_equip(self):
        equip_id = self.get_selected_equip()
        self.service.remover_equipamento(equip_id)
        self.get_equipamentos()

    def edit_equip(self):
        equip_id = self.get_selected_equip()
        equipamento = self.service.consultar_equipamento_id(equip_id)

        self.widget = EquipmentWindow(parent=self, edit=equip_id)
        self.widget.set_input_info(equipamento)
        self.widget.show()

    def create_equip(self):
        self.widget = EquipmentWindow(self)
        self.widget.show()
