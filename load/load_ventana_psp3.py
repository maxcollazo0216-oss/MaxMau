from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from psp.ejercicio3.psp3 import SimpsonInverso


class VentanaPSP3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_3.ui", self)
        
        self.pushButton.clicked.connect(self.pushButton_click)

    def pushButton_click(self):
        try:
            dof = float(self.lineEdit.text())
            xi = float(self.lineEdit_2.text())
            p = float(self.lineEdit_3.text())

            modelo = SimpsonInverso(xi, dof)
            x = modelo.encontrar_x(p)

            self.label.setText(str(round(x, 5)))

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))