from PyQt5.QtWidgets import QMainWindow

from simuload.user_interface.components.janela_principal import Ui_MainWindow

from simuload.user_interface.equipment_menu import EquipmentMenu
from simuload.user_interface.transformador_menu import TransformadorMenu
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
        self.get_transformadores()
        
    def set_connections(self):
        self.ui.transformador_menu.clicked.connect(self.transformer_menu)
        self.ui.equipamento_menu.clicked.connect(self.equipment_menu)
        self.ui.carga_menu.clicked.connect(self.load_menu)
        self.ui.nova_curva.clicked.connect(self.new_curve)
        self.ui.editar_curva.clicked.connect(self.edit_curve)
        self.ui.simular_curva.clicked.connect(self.simulate_curve)
        self.ui.excluir_curva.clicked.connect(self.remove_curve)
        self.ui.exportar_curva.clicked.connect(self.export_curve)
    
    def transformer_menu(self):
        self.widget = TransformadorMenu(self)
        self.widget.show()

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
        self.add_curvas()
    
    def add_curvas(self):
        self.ui.curvaList.clear()
        for curva in self.curvas:
            curva_label = str(curva[0]) + " - " + curva[1]
            self.ui.curvaList.insertItem(curva[0], curva_label)
            
    def get_transformadores(self):
        self.transformadores = self.service.consultar_transformador(consulta="")
        self.add_transformadores()
    
    def add_transformadores(self):
        self.ui.transfList.clear()
        for transf in self.transformadores:
            transf_label = str(transf[0]) + " - " + transf[1]
            self.ui.transfList.insertItem(transf[0], transf_label)

    def new_curve(self):
        self.widget = CurveWindow(self)
        self.widget.show()
        
    def get_selected_curve(self):
        curve_label = self.ui.curvaList.selectedItems()
        if curve_label:
            return int(curve_label[0].text().split(" - ")[0])
        raise NameError

    def get_selected_transf(self):
        transf_label = self.ui.transfList.selectedItems()
        if transf_label:
            return int(transf_label[0].text().split(" - ")[0])
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

    def remove_transf(self):
        try:
            transf_id = self.get_selected_transf()
            self.service.remover_transformador(transf_id)
            self.get_transformadores()
        except Exception as e:
            print(e)
            
        
    def set_curve_config(self):
        print(self.ui.intervaloGroup.checkedAction())
              
    def simulate_curve(self):
        try:
            curve_id = self.get_selected_curve()
            transf_id = self.get_selected_transf()
            x1, y1 = Calculator().simulate_curva(curve_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())
            x2, y2 = Calculator().simulate_transf(transf_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())
            self.show_curve(x1, y1, y2)
        except Exception as e:
            print(e)
    
    def get_curve_name(self):
        return self.ui.curvaList.selectedItems()[0].text().split('-')[1] + " X " + self.ui.transfList.selectedItems()[0].text().split('-')[1]
        
    def show_curve(self, x, y1, y2):
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.grid()
        plt.title(self.get_curve_name())
        plt.xlabel('Horas [h]')
        plt.ylabel('Consumo/Fornecimento [kWh/h]')
        plt.fill_between(x, y1, alpha=0.4)
        plt.show()
    
    def export_curve(self):
        try:
            curve_id = self.get_selected_curve()
            transf_id = self.get_selected_transf()
            horas, consumo = Calculator().simulate_curva(curve_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())
            horas1, fornecimento = Calculator().simulate_transf(transf_id,
                                         curva_config= self.ui.intervaloGroup.checkedAction().text())

            csv_save_curve(horas, consumo, fornecimento, self.get_curve_name())
        except Exception as e:
            print(e)
        
        