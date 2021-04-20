import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from YM_d_QT import Ui_MainWindow
from get_map import get_map


class App(QMainWindow, Ui_MainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('YandexMap')
        self.pushButton.clicked.connect(self.set_map)

        self.keyPressed.connect(self.on_key)

        self.delta = 0.0001
        self.MAX_D, self.MIN_D = 90.0, 0.0001

    def keyPressEvent(self, event):
        super(App, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            self.delta -= 0.0001
            self.delta = min(self.MAX_D, self.delta)
            self.set_map()

        elif event.key() == QtCore.Qt.Key_PageDown:
            self.delta += 0.0001
            self.delta = max(self.MIN_D, self.delta)
            self.set_map()

    def set_map(self):
        qp = QPixmap()
        qp.loadFromData(get_map(66, 66, self.delta))
        self.label.setPixmap(qp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
