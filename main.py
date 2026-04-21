import sys
from PyQt5.QtWidgets import QApplication
from load.load_menu_principal import MenuPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MenuPrincipal()
    ventana.show()

    sys.exit(app.exec_())