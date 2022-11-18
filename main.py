import random
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene, QApplication
from PyQt5.QtWidgets import QWidget

from ui import Ui_Form


class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.scene = QGraphicsScene()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        self.scene.clear()
        for i in range(4):
            x, y = random.randint(0, 100), random.randint(0, 100)
            self.graphicsView.setScene(self.scene)
            self.scene.addEllipse(x, y, y + 20, y + 20.0, brush=QColor(255, 217, 82))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = App()
    application.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
