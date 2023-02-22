# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImageReader,QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QGridLayout
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter, QIcon
from PyQt5.QtCore import QSize

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)

import cv2
from PIL import Image
import img_background_add
import pdf_merger
import math
import os
import time
import fitz
import os
import img2pdf

path_img = ''

global img, point1, point2

class ImageBox(QWidget):
    def __init__(self):
        super(ImageBox, self).__init__()
        self.img = None
        self.scaled_img = None
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.wheel_flag = False

        self.scale = 1
        self.old_scale = 1
        self.point = QPoint(0, 0)
        self.x = -1
        self.y = -1
        self.new_height = -1
        self.new_width = -1

        self.image_index = 0
        self.combine_image_files = []
        self.origin_image_files = []
        self.img_file_root_path = ''
        self.img_file_base_name = ''

        self.pdf_combine_file = "pdf_with_signature/"
        self.pdf_origin_file = "pdf_origin/"

        if os.path.exists(self.pdf_combine_file) == False:
            print("Folder pdf_with_signature is not exist. Create pdf_with_signature.")
            os.mkdir(self.pdf_combine_file)

        if os.path.exists(self.pdf_origin_file) == False:
            print("Folder pdf_origin is not exist. Create pdf_origin_file.")
            os.mkdir(self.pdf_origin_file)

        self.label_image_index = QLabel('PDF page:   ', self)
        layout = QGridLayout(self)
        layout.addWidget(self.label_image_index, -10, 0)

        self.setFocusPolicy(Qt.StrongFocus)

    def pdf_recover_from_imgs(self, sig_name):
        if len(self.combine_image_files) == 0:
            print("[pdf_recover_from_imgs]File list is empty.")
            return
        file_name, file_extension = os.path.splitext(self.combine_image_files[0])
        base_name = os.path.basename(file_name)
        for i in range(len(self.combine_image_files)):
            img_path = os.path.join(self.img_file_root_path, self.combine_image_files[i])
            bg_sg_combine_pdf_bytes = img2pdf.convert(img_path)
            # file_single_out_pdf = self.pdf_combine_file + base_name + '_' + str(i) +'.pdf'
            file_single_out_pdf = self.img_file_root_path + base_name + '_' + str(i) +'.pdf'
            print(file_single_out_pdf)
            file = open(file_single_out_pdf, "wb")
            file.write(bg_sg_combine_pdf_bytes)
            file.close()
        file_final_out_pdf =  self.pdf_combine_file + sig_name + '_' + self.img_file_base_name + '.pdf'
        print(file_final_out_pdf)
        pdf_merger.pdf_multi_files_merge(self.img_file_root_path, file_final_out_pdf)

        

    def pdf2image_tranfer(self, pdf_name, img_path):
        pdf_file = fitz.open(pdf_name)
        os.mkdir(img_path)
        # 遍历PDF的所有页面
        for page_index in range(len(pdf_file)):
            # 获取页面对象
            page = pdf_file[page_index]

            # 将页面转换为图像对象
            pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))

            # 保存图像文件
            # img_path = 'tmp_img_page{}.png'.format(page_index)
            # total_img_name = os.path.join(img_name, new_name)
            total_img_name = img_path + 'tmp_img_{}_ori.png'.format(page_index)
            combine_img_name = img_path + 'tmp_img_{}_com.png'.format(page_index)
            pix._writeIMG(total_img_name, 0)
            pix._writeIMG(combine_img_name, 0)

        # 关闭PDF文件
        pdf_file.close()

    def set_image_index(self, index):
        self.image_index = index

    def get_image_index(self):
        return self.image_index

    def get_combine_files(self):
        return self.combine_image_files

    def get_combine_image_name(self):
        ret_img_name = os.path.join(self.img_file_root_path, self.combine_image_files[self.image_index])
        return ret_img_name

    def get_origin_image_name(self):
        img_file_name = os.path.join(self.img_file_root_path, self.origin_image_files[self.image_index])
        return img_file_name

    def left_switch_image(self):
        self.image_index = (self.image_index - 1) % len(self.combine_image_files)
        # img_file_name = os.path.join(self.img_file_root_path, self.combine_image_files[self.image_index])
        img_file_name = self.get_combine_image_name()
        print("left_switch_image. Index: %s ." %(img_file_name))
        self.set_image(img_file_name)

    def right_switch_image(self):
        self.image_index = (self.image_index + 1) % len(self.combine_image_files)
        img_file_name = self.get_combine_image_name()
        print("right_switch_image. Index: %s ." %(img_file_name))
        self.set_image(img_file_name)

    def display_img(self):
        pdf_name, _ = QFileDialog.getOpenFileName(None, "Open PDF File", self.pdf_origin_file, "*.pdf")
        if pdf_name == '':
            print("No PDF Opened.")
            return
        file_name, file_extension = os.path.splitext(pdf_name)
        img_file_base_name = os.path.basename(file_name)
        self.img_file_base_name = img_file_base_name
        print(img_file_base_name)
        timestamp = time.time()
        self.img_file_root_path = 'tmp_img_' + str(int(timestamp)) + '_' + img_file_base_name + '/'
        print(self.img_file_root_path)
        self.pdf2image_tranfer(pdf_name, self.img_file_root_path)
        # img_file_name = self.img_file_root_path + 'tmp_img_0.png'
        # self.box.set_image(img_file_name)

        self.image_index = 0
        self.combine_image_files = [filename for filename in os.listdir(self.img_file_root_path) if
                            filename.endswith('com.jpg') or filename.endswith('com.png')]
        self.origin_image_files = [filename for filename in os.listdir(self.img_file_root_path) if
                            filename.endswith('ori.jpg') or filename.endswith('ori.png')]
        img_file_name = self.get_combine_image_name()
        self.set_image(img_file_name)
    
    def get_img_file_root_path(self):
        return os.path(self.img_file_root_path)

    # def init_ui(self):
    #     self.setWindowTitle("ImageBox")
    def update_new_img(self):
        img_file_name = self.get_combine_image_name()
        print("update_new_img. New img_file_name: %s ." %(img_file_name))
        self.set_image(img_file_name)
        self.update()

    def set_image(self, img_path):
        self.img = QPixmap(img_path)
        print(type(img_path))
        global path_img
        path_img = img_path
        width, height = self.img.width(), self.img.height()
        if height / width > 990 / 660:
            new_height = 990
            new_width = width * 990 / height
        else:
            new_height = height * 660 / width
            new_width = 660
        new_height = int(new_height)
        new_width = int(new_width)
        print("Run box.set_image. width: %d  height: %d" %(new_width, new_height))
        self.point = QPoint(int((660 - new_width) * 0.5), int((990 - new_height) * 0.5))
        self.img = self.img.scaled(new_width, new_height, Qt.KeepAspectRatio)
        self.scaled_img = self.img

        self.new_height = new_height
        self.new_width = new_width
        self.scale = 1

    def paintEvent(self, e):
        print("Run paintEvent.")
        if self.scaled_img:
            painter = QPainter()
            painter.begin(self)
            painter.scale(self.scale, self.scale)
            painter.setPen(QColor(255, 0, 0))
            if self.wheel_flag:  # 定点缩放
                self.wheel_flag = False
                # 判断当前鼠标pos在不在图上
                this_left_x = self.point.x() * self.old_scale
                this_left_y = self.point.y() * self.old_scale
                this_scale_width = self.new_width * self.old_scale
                this_scale_height = self.new_height * self.old_scale

                # 鼠标点在图上，以鼠标点为中心动作
                gap_x = self.x - this_left_x
                gap_y = self.y - this_left_y
                if 0 < gap_x < this_scale_width and 0 < gap_y < this_scale_height:
                    new_left_x = int(self.x / self.scale - gap_x / self.old_scale)
                    new_left_y = int(self.y / self.scale - gap_y / self.old_scale)
                    self.point = QPoint(new_left_x, new_left_y)
                # 鼠标点不在图上，固定左上角进行缩放
                else:
                    true_left_x = int(self.point.x() * self.old_scale / self.scale)
                    true_left_y = int(self.point.y() * self.old_scale / self.scale)
                    self.point = QPoint(true_left_x, true_left_y)
            painter.drawPixmap(self.point, self.scaled_img)  # 此函数中还会用scale对point进行处理
            painter.end()

    def wheelEvent(self, event):
        print("Run wheelEvent.")

    def mouseMoveEvent(self, e):
        print("Run mouseMoveEvent.")
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos  # 当前位置-起始位置=差值
            self.point = self.point + self.end_pos / self.scale  # 左上角的距离变化
            self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        print("Run mousePressEvent.")
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        print("Run mouseReleaseEvent.")
        if e.button() == Qt.LeftButton:
            self.left_click = False

    def keyPressEvent(self, e):
        if len(self.combine_image_files) == 0:
            print("--keyPressEvent. combine_image_files is empty.")
            return
        if e.key() == Qt.Key_Left:
            self.left_switch_image()
        elif e.key() == Qt.Key_Right:
            self.right_switch_image()
        img_label_str = 'PDF page: ' + str(self.image_index) + '.'
        print(img_label_str)
        self.label_image_index.setText(img_label_str)
        self.update()


if __name__ == "__main__":
    print("Main: img_edit_crop")
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_Form()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
