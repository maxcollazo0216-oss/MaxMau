from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from psp.ejercicio1.psp1 import PSP1

class VentanaPSP1(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_1.ui", self)

        self.pushButton.clicked.connect(self.pushButton_click)
        self.pushButton_2.clicked.connect(self.pushButton2_click)
        self.pushButton_3.clicked.connect(self.pushButton3_click)
        self.pushButton_4.clicked.connect(self.pushButton4_click)

        self.pushButton_5.clicked.connect(self.pushButton_5_click)

        self.x = None
        self.y = None

    def pushButton_click(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]

    def pushButton2_click(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    def pushButton3_click(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]

    def pushButton4_click(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    def pushButton_5_click(self):
        try:
            if self.x is None or self.y is None:
                raise Exception("Primero selecciona un caso")

            xk = float(self.lineEdit.text())

            modelo = PSP1(self.x, self.y)
            modelo.calcular_todo()

            yk = modelo.predecir(xk)

            self.label_4.setText(str(round(modelo.B0, 4)))
            self.label_3.setText(str(round(modelo.B1, 4)))
            self.label_6.setText(str(round(modelo.r, 4)))
            self.label_8.setText(str(round(modelo.r2, 4)))
            self.label_10.setText(str(round(yk, 4)))

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))