import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginPage import loginPage



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginPage = loginPage()
    loginPage.show()
    sys.exit(app.exec())