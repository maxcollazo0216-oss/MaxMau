from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from psp.ejercicio3.psp3 import SimpsonInverso


class VentanaPSP3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_3.ui", self)

        self.btn_calcular.clicked.connect(self.calcular_click)

    def calcular_click(self):
        try:
            dof = float(self.dof_line.text())
            xi = float(self.xi_line.text())
            p = float(self.P_line.text())

            modelo = SimpsonInverso(xi, dof)
            x = modelo.encontrar_x(p)

            self.label.setText(str(round(x, 5)))

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))