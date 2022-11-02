from PyQt5.QtWidgets import QDialog
from simuload.user_interface.components.equipamento_novo import Ui_NovoEquipamento


class EquipmentWindow(QDialog):
    def __init__(self, parent, edit=None):
        super().__init__()
        self.edit = edit
        self.ui = Ui_NovoEquipamento()
        self.ui.setupUi(self)
        self.parent = parent
        self.service = parent.service
        self.set_connections()

    def set_connections(self):
        if self.edit:
            self.ui.buttonBox.accepted.connect(self.update_equipment)
        else:
            self.ui.buttonBox.accepted.connect(self.create_equipment)

        self.ui.buttonBox.rejected.connect(self.close)

    def input_info(self):
        return {
            "Nome": self.ui.equip_nome.text(),
            "Potencia": self.ui.equip_potencia.text(),
            "FatorPotencia": self.ui.equip_fp.text(),
            "Uso": self.ui.equip_uso.text(),
        }

    def set_input_info(self, equipamento):
        self.ui.equip_nome.setText(str(equipamento[1]))
        self.ui.equip_potencia.setText(str(equipamento[2]))
        self.ui.equip_fp.setText(str(equipamento[3]))
        self.ui.equip_uso.setText(str(equipamento[4]))

    def update_equipment(self):
        equip_id = self.edit
        try:
            self.service.modificar_equipamento(equip_id, self.input_info())
        except Exception as e:
            print(e)
        self.parent.get_equipamentos()

    def create_equipment(self):

        try:
            self.service.inserir_equipamento(self.input_info())
        except Exception as e:
            print(e)
        self.parent.get_equipamentos()
