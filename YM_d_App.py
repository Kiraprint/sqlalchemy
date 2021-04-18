import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from YM_d_QT import Ui_MainWindow
from get_map import get_map


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('YandexMap')
        self.pushButton.clicked.connect(self.set_map)

    def set_map(self):
        qp = QPixmap()
        qp.loadFromData(get_map(66.6, 66.6, 0.5))
        self.label.setPixmap(qp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
