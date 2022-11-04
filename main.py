import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.flag)
        self.fl = False

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def flag(self):
        self.fl = True
        self.repaint()
        self.fl = False

    def draw(self, qp):
        x = random.randint(100, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = MyWidget()
    db.show()
    sys.exit(app.exec())