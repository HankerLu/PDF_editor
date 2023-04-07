import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtCore import QTimer, Qt

class ImageViewer(QWidget):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.image_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.jpg') or filename.endswith('.png')]
        self.image_index = 0

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.image_label.setGeometry(0, 0, 640, 480)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(2000)

        self.update_image()

    def update_image(self):
        image_path = os.path.join(self.folder_path, self.image_files[self.image_index])
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        print("get key press event")
        if event.key() == Qt.Key_Left:
            self.image_index = (self.image_index - 1) % len(self.image_files)
            self.update_image()
        elif event.key() == Qt.Key_Right:
            self.image_index = (self.image_index + 1) % len(self.image_files)
            self.update_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer('tmp_img_1676863575_amy_final')
    viewer.show()
    sys.exit(app.exec_())