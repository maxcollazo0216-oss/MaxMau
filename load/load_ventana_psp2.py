from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from psp.ejercicio2.psp2 import Simpson
import matplotlib.pyplot as plt
import numpy as np


class VentanaPSP2(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_2.ui", self)

        self.pushButton.clicked.connect(self.pushButton_click)

    def pushButton_click(self):
        try:
            dof = float(self.lineEdit.text())
            xi = float(self.lineEdit_2.text())
            x = float(self.lineEdit_3.text())

            modelo = Simpson(xi, x, dof)
            p, w, seg = modelo.calcular()

            self.label.setText(str(round(p, 6)))
            self.label_2.setText(str(round(w, 6)))
            self.label_3.setText(str(seg))
            self.graficar(modelo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            
    def graficar(self, modelo):
        x_vals = np.linspace(modelo.xi, modelo.x, 100)
        y_vals = [modelo.f(x) for x in x_vals]

        plt.figure()
        plt.plot(x_vals, y_vals, label="f(x)")
        plt.fill_between(x_vals, y_vals, alpha=0.3)

        plt.title("Regla de Simpson")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.legend()

        plt.show()

