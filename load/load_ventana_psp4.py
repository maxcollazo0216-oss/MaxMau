import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from psp.ejercicio4.psp4 import PSP4

class VentanaPSP4(QDialog):

    def __init__(self):
        super().__init__()

        ruta = os.path.join(os.path.dirname(__file__), "..", "gui", "ventana_psp4.ui")
        ruta = os.path.abspath(ruta)

        uic.loadUi(ruta, self)

        print(dir(self))  

        self.pushButton_caso1.clicked.connect(self.pushButton_caso1_click)
        self.pushButton_calcular.clicked.connect(self.pushButton_calcular_click)

        self.x = []
        self.y = []

    def pushButton_caso1_click(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]

        QMessageBox.information(self, "OK", "Caso 1 cargado")

    def pushButton_calcular_click(self):
        try:
            if not self.x:
                QMessageBox.warning(self, "Error", "Primero carga el Caso 1")
                return

            xk = float(self.lineEdit.text())
            p = float(self.lineEdit_2.text())

            modelo = PSP4(self.x, self.y)
            sigma, T, Range, UPI, LPI, YK, B0, B1 , R, R2 = modelo.calcular(xk, p)

            self.label_YK.setText(str(round(YK, 4)))
            self.label_T.setText(str(round(T, 4)))
            self.label_Range.setText(str(round(Range, 4)))
            self.label_UPI.setText(str(round(UPI, 4)))
            self.label_LPI.setText(str(round(LPI, 4)))
            self.label_B0.setText(str(round(B0, 4)))
            self.label_B1.setText(str(round(B1, 4)))
            self.label_R.setText(str(round(R, 4)))
            self.label_R2.setText(str(round(R2, 4)))
           

            QMessageBox.information(self, "OK", "Cálculo realizado")

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPSP4()
    ventana.exec_()