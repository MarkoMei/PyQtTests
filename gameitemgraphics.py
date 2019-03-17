from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from gameitem import GameItem

class GameItemGraphics():
    
    def __init__(self, gameitem):
        super().__init__()
        self.gameitem = gameitem

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

        
    def draw(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        coords = self.gameitem.get_coordinates()
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(coords[0], coords[1], 90, 60)
