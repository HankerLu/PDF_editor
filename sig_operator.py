import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SigOperator(QWidget):
    def __init__(self):
        print("Run SigOperator __init__")
        # self.app = QApplication(sys.argv)
        super(SigOperator, self).__init__()
        self.setWindowTitle('绘制矩形，出现重影')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.resize(600, 500)
        self.pix = QPixmap(600, 500)  # 设置画布大小
        self.pix.fill(Qt.white)  # 设置画布背景颜色为白色
        # self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.pix = QPixmap(600, 500)  # 设置画布大小
        self.pix.fill(Qt.white)  # 设置画布背景颜色为白色

    # 绘图
    def paintEvent(self, event):
        p = QPainter(self.pix)
        # painter = QPainter(self)
        # x = self.lastPoint.x()
        # y = self.lastPoint.y()
        # w = self.endPoint.x()-x
        # h = self.endPoint.y()-y
        # p.drawRect(x,y,w,h)
        # painter.drawPixmap(0, 0, self.pix)
        p.drawLine(self.lastPoint, self.endPoint)  # 根据鼠标指针前后两个位置绘制直线
        self.lastPoint = self.endPoint  # 让前一个坐标值等于后一个坐标值，就能画出连续的线
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    #当鼠标左键按下时触发该函数
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    #当鼠标左键移动时触发该函数
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()#调用paintEvent函数，重新绘制

    #当鼠标左键释放时触发该函数
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()  # 调用paintEvent函数，重新绘制
            self.pix.save("D:\Entrepreneurship\HankAmy\SW2304\hr_sheet_manager\sig.png")

    def sig_operator_run(self):
        print("Run sig_operator_run")
        form = SigOperator()
        form.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    print("Run sig_operator_run")
    app = QApplication(sys.argv)
    form = SigOperator()
    form.show()
    sys.exit(app.exec_())
