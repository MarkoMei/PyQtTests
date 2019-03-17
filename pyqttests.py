import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon, QPainter, QColor, QBrush
from PyQt5 import QtCore

from gameitem import GameItem
from gameitemgraphics import GameItemGraphics

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.gameItem = GameItem()
        self.gameItemGraphics = GameItemGraphics(self.gameItem)
        self.initUI()
        self.statusMessage('Ready to go!')

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def statusMessage(self, message):
        self.statusBar().showMessage(message)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        self.gameItem.move_random()
        self.update()           

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        
        text = "x: {0},  y: {1}".format(x, y)
        self.statusMessage(text)
        self.gameItem.move_random()
        self.update()
    
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.gameItemGraphics.draw(qp)
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
