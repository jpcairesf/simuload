from PyQt5.QtWidgets import QWidget
from simuload.user_interface.components.equipamento_menu import (
    Ui_MenuEquipamento
)


class EquipmentMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_MenuEquipamento()
        self.ui.setupUi(self)
        self.service = parent.service
