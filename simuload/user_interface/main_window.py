from PyQt5.QtWidgets import QMainWindow

from simuload.user_interface.components.janela_principal import Ui_MainWindow

from simuload.user_interface.equipment_menu import EquipmentMenu
from simuload.user_interface.equipment_window import EquipmentWindow
from simuload.user_interface.load_menu import LoadMenu
from simuload.user_interface.curve_window import CurveWindow
from simuload.processors.calculator import Calculator
import matplotlib.pyplot as plt

from simuload.utils.csv_exporter import csv_save_curve


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
        self.ui.actionNova_Curva.triggered.connect(self.new_curve)
        self.ui.editar_curva.clicked.connect(self.edit_curve)
        self.ui.simular_curva.clicked.connect(self.simulate_curve)
        self.ui.excluir_curva.clicked.connect(self.remove_curve)
        self.ui.actionSalvar_Curva.triggered.connect(self.export_curve)
    
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
            
    def new_curve(self):
        self.widget = CurveWindow(self)
        self.widget.show()
        
    def get_selected_curve(self):
        curve_label = self.ui.curvaList.selectedItems()
        if curve_label:
            return int(curve_label[0].text().split(" - ")[0])
        raise NameError
    
    def edit_curve(self):
        try:
            curve_id = self.get_selected_curve()
            curve = self.service.consultar_curva_pela_id(curve_id)
            self.widget = CurveWindow(self, edit=curve_id)
            self.widget.set_input_info(curve)
            self.widget.show()
        except NameError:
            print("Por favor, selecione uma curva")
            
    def remove_curve(self):
        try:
            curve_id = self.get_selected_curve()
            self.service.remover_curva(curve_id)
            self.service.remover_carga_na_curva(curve_id)
            self.get_curvas()
        except Exception as e:
            print(e)
            
        
    def set_curve_config(self):
        print(self.ui.intervaloGroup.checkedAction())
              
    def simulate_curve(self):
        try:
            curve_id = self.get_selected_curve()
            x, y = Calculator().simulate(curve_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())
            self.show_curve(x, y)
        except Exception as e:
            print(e)
    
    def get_curve_name(self):
        return self.ui.curvaList.selectedItems()[0].text().split('-')[1]
        
    def show_curve(self, x, y):
        plt.plot(x, y)
        plt.grid()
        plt.title(self.get_curve_name())
        plt.xlabel('Horas [h]')
        plt.ylabel('Consumo [kWh/h]')
        plt.fill_between(x, y, alpha=0.4)
        plt.show()
    
    def export_curve(self):
        try:
            curve_id = self.get_selected_curve()
            horas, consumo = Calculator().simulate(curve_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())

            csv_save_curve(horas, consumo, self.get_curve_name())
        except Exception as e:
            print(e)
        
        