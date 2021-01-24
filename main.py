import sys
import asyncio
from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

# Main Frame
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())