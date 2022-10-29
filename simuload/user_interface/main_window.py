from PyQt5.QtWidgets import QMainWindow
from simuload.user_interface.components.janela_principal import Ui_MainWindow
from simuload.user_interface.equipment_menu import EquipmentMenu


class MainWindow(QMainWindow):
    def __init__(self, service):
        super().__init__()
        self.widget = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_connections()
        self.service = service

    def set_connections(self):
        self.ui.equipamento_menu.clicked.connect(self.show_new_equip_window)

    def show_equipment_menu(self):
        self.widget = EquipmentMenu(self)
        self.widget.show()
        
    def show_new_equip_window(self):
        self.widget = EquipmentMenu(self)
        self.widget.show()
