from simuload.arch.service import Service
from simuload.user_interface.simuload_ui import SimuloadUI


class Controller:
    def __init__(self):
        self.start_service()
        self.start_ui()

    def start_service(self):
        self.service = Service()

    def start_ui(self):
        self.ui = SimuloadUI(self.service)
        self.ui.start_ui()


if __name__ == "__main__":
    cont = Controller()
