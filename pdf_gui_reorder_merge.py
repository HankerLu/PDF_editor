from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class BlockItem(QGraphicsRectItem):
    def __init__(self, parent=None):
        super(BlockItem, self).__init__(parent)
        self.setRect(0, 0, 100, 50)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def mousePressEvent(self, event):
        print("BlockItem mousePressEvent")
        self.setCursor(Qt.ClosedHandCursor)
        self.update()
        super(BlockItem, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        print("BlockItem mouseReleaseEvent")
        self.setCursor(Qt.OpenHandCursor)
        self.update()
        super(BlockItem, self).mouseReleaseEvent(event)


class BlockScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(BlockScene, self).__init__(parent)
        self.setSceneRect(0, 0, 800, 600)

    def dragEnterEvent(self, event):
        print("BlockScene dragEnterEvent")
        if event.mimeData().hasFormat('application/x-block'):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        print("BlockScene dragMoveEvent")
        if event.mimeData().hasFormat('application/x-block'):
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print("BlockScene dropEvent")
        if event.mimeData().hasFormat('application/x-block'):
            itemData = event.mimeData().data('application/x-block')
            dataStream = QDataStream(itemData, QIODevice.ReadOnly)
            pixmap = QPixmap()
            offset = QPoint()
            dataStream >> pixmap >> offset
            newItem = BlockItem()
            newItem.setPos(event.scenePos() - offset)
            self.addItem(newItem)
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()


class BlockView(QGraphicsView):
    def __init__(self, parent=None):
        super(BlockView, self).__init__(parent)
        self.setScene(BlockScene(self))
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setAcceptDrops(True)

        block1 = BlockItem()
        block1.setPos(0, 0)
        self.scene().addItem(block1)

        block2 = BlockItem()
        block2.setPos(0, 0)
        self.scene().addItem(block2)

    def dragEnterEvent(self, event):
        print("BlockView dragEnterEvent")
        self.scene().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        print("BlockView dragMoveEvent")
        self.scene().dragMoveEvent(event)

    def dropEvent(self, event):
        print("BlockView dropEvent")
        self.scene().dropEvent(event)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(0.9, 0.9)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Block Programming')
        self.view = BlockView()
        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())