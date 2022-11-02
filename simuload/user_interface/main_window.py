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
        self.service = service
        self.set_connections()
        self.get_curvas()
        
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
    
    def get_curvas(self):
        self.curvas = self.service.consultar_curva(consulta="")
        self.add_itens()
    
    def add_itens(self):
        self.ui.curvaList.clear()
        for curva in self.curvas:
            curva_label = str(curva[0]) + " - " + curva[1]
            self.ui.curvaList.insertItem(curva[0], curva_label)