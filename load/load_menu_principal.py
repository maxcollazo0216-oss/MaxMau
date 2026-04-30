from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from load.load_ventana_psp1 import VentanaPSP1
from load.load_ventana_psp2 import VentanaPSP2
from load.load_ventana_psp3 import VentanaPSP3
from load.load_ventana_psp4 import VentanaPSP4


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu.ui", self)

        self.actionPSP.triggered.connect(self.abrir_psp1)
        self.actionPCP.triggered.connect(self.abrir_psp2)
        self.actionPSP3.triggered.connect(self.abrir_psp3)
        self.actionPSP4.triggered.connect(self.abrir_psp4)
        self.actionSalir.triggered.connect(self.close)

    def abrir_psp1(self):
        self.ventana = VentanaPSP1()
        self.ventana.exec_()

    def abrir_psp2(self):
        self.ventana = VentanaPSP2()
        self.ventana.exec_()

    def abrir_psp3(self):
        self.ventana = VentanaPSP3()
        self.ventana.exec_()
        
    def abrir_psp4(self):
        self.ventana = VentanaPSP4()
        self.ventana.exec_()