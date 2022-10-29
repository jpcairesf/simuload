from simuload.user_interface.main_window import MainWindow
from PyQt5.QtWidgets import QApplication


import sys


class SimuloadUI:
    def __init__(self, service):
        self.app = QApplication(sys.argv)
        self.service = service
        self.window = MainWindow(self.service)

    def start_ui(self):
        self.window.show()
        self.app.exec()
