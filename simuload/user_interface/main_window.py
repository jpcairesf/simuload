from PyQt5.QtWidgets import QMainWindow

from simuload.user_interface.components.janela_principal import Ui_MainWindow

from simuload.user_interface.equipment_menu import EquipmentMenu
from simuload.user_interface.equipment_window import EquipmentWindow
from simuload.user_interface.load_menu import LoadMenu


class MainWindow(QMainWindow):
    def __init__(self, service):
        super().__init__()

        self.widget = None

        self.widget = None

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.set_connections()

        self.service = service

    def set_connections(self):

        self.ui.equipamento_menu.clicked.connect(self.equipment_menu)
        self.ui.carga_menu.clicked.connect(self.load_menu)

    def equipment_menu(self):

        self.widget = EquipmentMenu(self)

        self.widget.show()
        
    def load_menu(self):
        
        self.widget = LoadMenu(self)
        self.widget.show()

    def new_equip(self):

        self.widget = EquipmentWindow(self)

        self.widget.show()
