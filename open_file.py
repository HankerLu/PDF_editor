import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QLabel, QPushButton, QVBoxLayout

class FileFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "文件查找和选择"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建文本标签
        self.label = QLabel("请选择要查找的文件：", self)

        # 创建“选择文件”按钮
        self.select_button = QPushButton("选择文件", self)
        self.select_button.clicked.connect(self.get_file)

        # 创建垂直布局，并将标签和按钮添加到其中
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def get_file(self):
        # 打开文件选择对话框
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", os.getenv("HOME"))
        if file_name:
            self.label.setText(f"已选择文件：{file_name}")


if __name__ == "__main__":
    app = QApplication([])
    file_finder = FileFinder()
    file_finder.show()
    app.exec_()