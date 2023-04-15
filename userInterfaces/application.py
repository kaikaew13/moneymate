import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginPageModule import Ui_Form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())