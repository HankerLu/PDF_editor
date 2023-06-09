import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

import img_crop_edit
import sig_operator
import cv2
from PIL import Image
import img_background_add
import office_2_pdf
import math
import os
import numpy as np
import pdf_merger

class Ui_MainWindow(object):
	def __init__(self):
		# 主界面初始化
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		# 一级菜单栏初始化
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menu_pdf_tran = QtWidgets.QMenu(self.menubar)
		self.menu_pdf_edit = QtWidgets.QMenu(self.menubar)
		self.menu_pdf_merge = QtWidgets.QMenu(self.menubar)
		self.menu_pdf_help = QtWidgets.QMenu(self.menubar)
		# 二级菜单栏初始化
		self.actionoffice2pdf = QtWidgets.QAction(MainWindow)
		self.action_sign_generate = QtWidgets.QAction(MainWindow)
		self.action_sign_select = QtWidgets.QAction(MainWindow)
		self.action_sign_single_page = QtWidgets.QAction(MainWindow)
		self.action_sign_confirm = QtWidgets.QAction(MainWindow)
		self.action_pdf_multi_merge = QtWidgets.QAction(MainWindow)
		self.action_about_us = QtWidgets.QAction(MainWindow)
		# 界面布局
		self.Layout = QVBoxLayout(self.centralwidget)  # 垂直布局
		# stackedWidget初始化
		self.stackedWidget = QStackedWidget()

		self.app_root_path = os.path.abspath(os.path.dirname(sys.argv[0]))
		print("Init Current path:%s"%(self.app_root_path))
		self.img_signature_file = 'img_signature/'
		self.img_signature_list = [f for f in os.listdir(self.img_signature_file) if f.endswith('.png')]
		
		if len(self.img_signature_list) != 0:		
			self.img_signature_select = self.img_signature_list[0]
			self.sig_img_whole_name = self.img_signature_file + self.img_signature_select
		else:
			self.img_signature_select = ''
			self.sig_img_whole_name = ''
		print("Init self.img_signature_select:%s"%(self.img_signature_select))

		self.pdf_ref_combine_file = "pdf_with_signature/"
		self.pdf_ref_origin_file = "pdf_origin/"
		self.pdf_abs_origin_file = os.path.abspath(self.pdf_ref_origin_file)

		self.pdf_final_merge_file = "pdf_final_merge/"

		self.pdf_merge_list = []

		self.box = img_crop_edit.ImageBox(self.pdf_ref_origin_file, self.pdf_ref_combine_file)
		self.sig_op_form = sig_operator.SigOperator()
		self.pdf_generator = office_2_pdf.PdfGenerator(self.pdf_abs_origin_file)

	def setupUi(self, MainWindow):
		# 创建界面
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(900, 1080)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)

		# 一级菜单栏布置
		self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
		self.menubar.setObjectName("menubar")
		self.menu_pdf_tran.setObjectName("menu_pdf_tran")
		self.menu_pdf_edit.setObjectName("menu_pdf_edit")
		self.menu_pdf_merge.setObjectName("menu_pdf_merge")
		self.menu_pdf_help.setObjectName("menu_pdf_help")
		MainWindow.setMenuBar(self.menubar)
		# 二级菜单栏布置
		self.actionoffice2pdf.setObjectName("actionoffice2pdf")

		self.action_sign_generate.setObjectName("action_sign_generate")
		self.action_sign_select.setObjectName("action_sign_select")
		self.action_sign_single_page.setObjectName("action_sign_single_page")

		# self.action_sign_confirm.setObjectName("action_sign_confirm")
		self.action_pdf_multi_merge.setObjectName("action_pdf_multi_merge")

		self.action_about_us.setObjectName("action_about_us")

		self.menu_pdf_tran.addAction(self.actionoffice2pdf)

		self.menu_pdf_edit.addAction(self.action_sign_generate)
		self.menu_pdf_edit.addAction(self.action_sign_select)
		self.menu_pdf_edit.addAction(self.action_sign_single_page)
		# self.menu_pdf_edit.addAction(self.action_sign_confirm)

		self.menu_pdf_merge.addAction(self.action_pdf_multi_merge)

		self.menu_pdf_help.addAction(self.action_about_us)

		self.menubar.addAction(self.menu_pdf_tran.menuAction())
		self.menubar.addAction(self.menu_pdf_edit.menuAction())
		self.menubar.addAction(self.menu_pdf_merge.menuAction())
		self.menubar.addAction(self.menu_pdf_help.menuAction())

		# 布局添加stackedWidget控件
		self.Layout.addWidget(self.stackedWidget)

		# 设置主界面面板：
		self.form_main_windoow = QWidget()
		self.formLayout = QHBoxLayout(self.form_main_windoow)  # 水平布局
		# self.label0 = QLabel()
		# self.label0.setText("Amy HR Assistant")
		# self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		# self.label0.setAlignment(Qt.AlignAbsolute)
		# self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
		# self.formLayout.addWidget(self.label0)  # 添加控件

		self.label = QLabel()
		pixmap = QPixmap()
		pixmap = pixmap.transformed(QTransform().rotate(90))
		pixmap = pixmap.scaled(700, 950)
		self.label.setPixmap(pixmap)
		self.label.setAlignment(Qt.AlignCenter)
		# self.label.setMaximumSize(900, 1000)
		# 设置 QLabel 的大小和位置
		self.label.setGeometry(QtCore.QRect(0, 0, pixmap.width(), pixmap.height()))
		self.formLayout.addWidget(self.label)

		# 设置第1个面板：
		self.form_office2pdf = QWidget()
		self.formLayoutOffice2PDF = QHBoxLayout(self.form_office2pdf)  # 水平布局

		self.button_office_2_pdf = QtWidgets.QPushButton(self.form_office2pdf)
		self.button_office_2_pdf.setGeometry(QtCore.QRect(30, 500, 180, 50))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_office_2_pdf.setFont(font)
		self.button_office_2_pdf.setObjectName("office_2_pdf")
		self.button_office_2_pdf.clicked.connect(self.office_2_pdf_exec)

		# 设置第2个面板：
		self.form_sign_create = QWidget()
		self.formLayoutSignCreate = QHBoxLayout(self.form_sign_create)
		# self.label_sign_create = QLabel()
		# self.label_sign_create.setText("签名制作")
		# self.label_sign_create.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		# self.label_sign_create.setAlignment(Qt.AlignCenter)
		# self.label_sign_create.setFont(QFont("Roman times", 50, QFont.Bold))
		# self.formLayoutSignCreate.addWidget(self.label_sign_create)

		self.button_sign_create = QtWidgets.QPushButton(self.form_sign_create)
		self.button_sign_create.setGeometry(QtCore.QRect(30, 300, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_sign_create.setFont(font)
		self.button_sign_create.setObjectName("create_sign")
		self.button_sign_create.clicked.connect(self.sign_create_exec)

		self.button_sign_reset = QtWidgets.QPushButton(self.form_sign_create)
		self.button_sign_reset.setGeometry(QtCore.QRect(30, 400, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_sign_reset.setFont(font)
		self.button_sign_reset.setObjectName("save_sign")
		self.button_sign_reset.clicked.connect(self.sign_create_reset)

		self.button_sign_save = QtWidgets.QPushButton(self.form_sign_create)
		self.button_sign_save.setGeometry(QtCore.QRect(30, 500, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_sign_save.setFont(font)
		self.button_sign_save.setObjectName("save_sign")
		self.button_sign_save.clicked.connect(self.sign_create_save)

		# self.form_sign_create_painter = sig_operator.SigOperator()

		# 设置第3个面板：
		self.form_sign_manage = QWidget()
		self.formSignManage = QHBoxLayout(self.form_sign_manage)
		self.label_sign_manage = QLabel()
		self.label_sign_manage.setText("当前签名文件： %s"%self.img_signature_select)
		self.label_sign_manage.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_sign_manage.setAlignment(Qt.AlignCenter)
		self.label_sign_manage.setFont(QFont("Roman times", 30, QFont.Bold))
		self.formSignManage.addWidget(self.label_sign_manage)

		# 设置第4个面板：
		self.form_sign_single_page = QWidget()
		self.formLayoutSignSinglePage = QVBoxLayout(self.form_sign_single_page)
		self.label_sign_single_page = QLabel()
		self.label_sign_single_page.setText("签名单页")
		self.label_sign_single_page.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_sign_single_page.setAlignment(Qt.AlignCenter)
		self.label_sign_single_page.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayoutSignSinglePage.addWidget(self.label_sign_single_page)

		self.scrollArea = QtWidgets.QScrollArea(self.form_sign_single_page)
		self.scrollArea.setGeometry(QtCore.QRect(150, 10, 680, 990))
		self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		# self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")

		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 990))
		self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(100, 100))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout.setObjectName("gridLayout")

		# self.formLayoutSignSinglePage.addWidget(self.box)
		self.gridLayout.addWidget(self.box)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.button_open_pdf = QtWidgets.QPushButton(self.form_sign_single_page)
		self.button_open_pdf.setGeometry(QtCore.QRect(30, 100, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_open_pdf.setFont(font)
		self.button_open_pdf.setObjectName("button_open_pdf")
		self.button_open_pdf.clicked.connect(self.open_pdf_exec)

		self.button_sign_page = QtWidgets.QPushButton(self.form_sign_single_page)
		self.button_sign_page.setGeometry(QtCore.QRect(30, 200, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_sign_page.setFont(font)
		self.button_sign_page.setObjectName("button_sign_page")
		self.button_sign_page.clicked.connect(self.sign_page_exec)

		self.button_confirm_edit = QtWidgets.QPushButton(self.form_sign_single_page)
		self.button_confirm_edit.setGeometry(QtCore.QRect(30, 300, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_confirm_edit.setFont(font)
		self.button_confirm_edit.setObjectName("button_confirm_edit")
		self.button_confirm_edit.clicked.connect(self.confirm_edit_exec)

		self.form_merge_pdf = QWidget()
		self.formMergePDF = QHBoxLayout(self.form_merge_pdf)

		self.label_merge_pdf_for_one = QLabel()
		self.label_merge_pdf_for_one.setText("PDF文件列表: ")
		self.label_merge_pdf_for_one.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_merge_pdf_for_one.setAlignment(Qt.AlignCenter)
		self.label_merge_pdf_for_one.setFont(QFont("Roman times", 15, QFont.Bold))
		self.formMergePDF.addWidget(self.label_merge_pdf_for_one)

		self.button_add_pdf_to_merge = QtWidgets.QPushButton(self.form_merge_pdf)
		self.button_add_pdf_to_merge.setGeometry(QtCore.QRect(30, 300, 180, 50))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_add_pdf_to_merge.setFont(font)
		self.button_add_pdf_to_merge.setObjectName("add_pdf_to_merge")
		self.button_add_pdf_to_merge.clicked.connect(self.add_pdf_to_merge_exec)

		self.button_remove_top_pdf = QtWidgets.QPushButton(self.form_merge_pdf)
		self.button_remove_top_pdf.setGeometry(QtCore.QRect(30, 400, 180, 50))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_remove_top_pdf.setFont(font)
		self.button_remove_top_pdf.setObjectName("remove_top_pdf")
		self.button_remove_top_pdf.clicked.connect(self.remove_top_pdf_exec)

		self.button_merge_select_pdf = QtWidgets.QPushButton(self.form_merge_pdf)
		self.button_merge_select_pdf.setGeometry(QtCore.QRect(30, 500, 180, 50))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_merge_select_pdf.setFont(font)
		self.button_merge_select_pdf.setObjectName("merge_select_pdf")
		self.button_merge_select_pdf.clicked.connect(self.merge_select_pdf_exec)
		
		self.button_reset_merge_pdf = QtWidgets.QPushButton(self.form_merge_pdf)
		self.button_reset_merge_pdf.setGeometry(QtCore.QRect(30, 600, 180, 50))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.button_reset_merge_pdf.setFont(font)
		self.button_reset_merge_pdf.setObjectName("reset_merge_pdf")
		self.button_reset_merge_pdf.clicked.connect(self.reset_pdf_merge_exec)

		self.form_about_us = QWidget()
		self.formAboutUs = QHBoxLayout(self.form_about_us)
		# self.label_about_us = QLabel()
		# self.label_about_us.setText("就不告诉你，略略略")
		# self.label_about_us.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		# self.label_about_us.setAlignment(Qt.AlignCenter)
		# self.label_about_us.setFont(QFont("微软雅黑", 40, QFont.Bold))
		# self.formAboutUs.addWidget(self.label_about_us)
		self.label2 = QLabel()
		# pixmap = pixmap.transformed(QTransform().rotate(90))
		pixmap = pixmap.scaled(700, 900)
		self.label2.setPixmap(pixmap)
		self.label2.setAlignment(Qt.AlignCenter)
		self.label2.setGeometry(QtCore.QRect(0, 0, pixmap.width(), pixmap.height()))
		self.formAboutUs.addWidget(self.label2)

		# stackedWidget添加各种界面用于菜单切换
		self.stackedWidget.addWidget(self.form_main_windoow)
		self.stackedWidget.addWidget(self.form_office2pdf)
		self.stackedWidget.addWidget(self.form_sign_create)
		self.stackedWidget.addWidget(self.form_sign_manage)
		self.stackedWidget.addWidget(self.form_sign_single_page)
		self.stackedWidget.addWidget(self.form_merge_pdf)
		self.stackedWidget.addWidget(self.form_about_us)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		# 窗口名称
		MainWindow.setWindowTitle(_translate("MainWindow", "Amy HR Assistant.V2.0"))
		# 一级目录
		self.menu_pdf_tran.setTitle(_translate("MainWindow", "PDF转换"))
		self.menu_pdf_edit.setTitle(_translate("MainWindow", "PDF编辑"))
		self.menu_pdf_merge.setTitle(_translate("MainWindow", "PDF合并"))
		self.menu_pdf_help.setTitle(_translate("MainWindow", "帮助"))
		# 二级目录
		# PDF转换功能1：office文件转换
		self.actionoffice2pdf.setText(_translate("MainWindow", "office文件转换"))
		self.actionoffice2pdf.triggered.connect(self.goto_office_2_pdf)
		# PDF编辑功能1：签名制作
		self.action_sign_generate.setText(_translate("MainWindow", "签名制作"))
		self.action_sign_generate.triggered.connect(self.goto_sign_create)
		# PDF编辑功能2：签名选择
		self.action_sign_select.setText(_translate("MainWindow", "签名选择"))
		self.action_sign_select.triggered.connect(self.goto_sign_select)
		# PDF编辑功能3：签名单页
		self.action_sign_single_page.setText(_translate("MainWindow", "签名单页"))
		self.action_sign_single_page.triggered.connect(self.goto_sign_operation)

		# PDF合成功能1：PDF排序合成
		self.action_pdf_multi_merge.setText(_translate("MainWindow", "PDF文件合成"))
		self.action_pdf_multi_merge.triggered.connect(self.goto_pdf_multi_merge)

		self.action_about_us.setText(_translate("MainWindow", "关于 HR Assistant"))
		self.action_about_us.triggered.connect(self.goto_about_us_intro)

		self.button_office_2_pdf.setText(_translate("Form", "选择office文件并转换"))

		self.button_sign_create.setText(_translate("Form", "新建签名"))
		self.button_sign_reset.setText(_translate("Form", "重置签名"))
		self.button_sign_save.setText(_translate("Form", "保存签名"))

		self.button_open_pdf.setText(_translate("Form", "打开PDF"))
		self.button_sign_page.setText(_translate("Form", "签名此页"))
		self.button_confirm_edit.setText(_translate("Form", "确认修改"))

		self.button_add_pdf_to_merge.setText(_translate("Form", "新增PDF"))
		self.button_remove_top_pdf.setText(_translate("Form", "移除顶端"))
		self.button_merge_select_pdf.setText(_translate("Form", "确认合并"))
		self.button_reset_merge_pdf.setText(_translate("Form", "重置合并"))

	# 菜单栏触发每个界面调用函数
	def goto_office_2_pdf(self):
		self.stackedWidget.setCurrentIndex(1)
	def goto_sign_create(self):
		self.stackedWidget.setCurrentIndex(2)

	def goto_sign_select(self):
		sig_png_name, _ = QFileDialog.getOpenFileName(None, "Open Sign File", self.img_signature_file, "*.png")
		sig_png_name = os.path.basename(sig_png_name)
		self.img_signature_select = sig_png_name
		print(self.img_signature_select)
		self.label_sign_manage.setText("当前签名文件： %s"%self.img_signature_select)
		self.stackedWidget.setCurrentIndex(3)
	def goto_sign_operation(self):
		self.stackedWidget.setCurrentIndex(4)
	def goto_pdf_multi_merge(self):
		self.stackedWidget.setCurrentIndex(5)
	def goto_about_us_intro(self):
		self.stackedWidget.setCurrentIndex(6)

	def office_2_pdf_exec(self):
		print("office 2 pdf")
		office_file_name, _ = QFileDialog.getOpenFileName(None, "Open Office File", "*.doc;*.docx;*.xls;*.xlsx;*.pdf")
		print("Open office file %s"%office_file_name)
		if office_file_name != '':	
			self.pdf_generator.run_office_2_pdf_transfer(office_file_name)

	def sign_create_exec(self):
		print("create new sign")
		# self.box.display_img()
		self.sig_op_form.show()

	def sign_create_reset(self):
		print("reset current sign")
		self.sig_op_form.reset_and_erase()

	def sign_create_save(self):
		print("save new sign")
		text, okPressed = QInputDialog.getText(None, "输入对话框", "请输出签名文件名(不带后缀):", QLineEdit.Normal, "")
		# 根据用户点击的结果进行处理
		if okPressed and text != '':
			sig_img_file_name = text + '.png'
			self.sig_img_whole_name = self.img_signature_file + sig_img_file_name
			print("已保存签名文件：" + self.sig_img_whole_name)
			self.sig_op_form.confirm_and_save(self.sig_img_whole_name)

	def open_pdf_exec(self):
		print("open pdf file")
		self.box.display_img()

	def sign_page_exec(self):
		print("sign one page")
		global img, crop_origin_file_name
		crop_origin_file_name = self.box.get_origin_image_name()
		# img = cv2.imread(crop_origin_file_name.decode())
		img = cv2.imdecode(np.fromfile(crop_origin_file_name,dtype=np.uint8),-1)
		if len(img) == 0:
			print('sign_page_exec fail. IMG file is empty.')
			return
		img_width = img.shape[1]
		img_height = img.shape[0]
		img_w_h_k = float(img_width/img_height)
		print(img_w_h_k)
		img_display_width = int(img_w_h_k * 1400)
		print("img weight height")
		print(img_width, img_height)
		cv2.namedWindow('image', cv2.WINDOW_NORMAL)
		cv2.setMouseCallback('image', self.sign_on_mouse)
		cv2.resizeWindow('image', img_display_width, 1400)
		cv2.imshow('image', img)
		cv2.waitKey(0)
		pass

	def confirm_edit_exec(self):
		print("confirm edition")
		# imgs_in_list = self.box.get_combine_files()
		# imgs_in_root = self.box.img_file_root_path()
		# img_background_add.pdf_recover_from_imgs(imgs_in_root, imgs_in_list, self.pdf_combine_file)
		sig_name_in, sig_extension = os.path.splitext(self.img_signature_select)
		print(sig_name_in)
		self.box.pdf_recover_from_imgs(sig_name_in)

	def add_pdf_to_merge_exec(self):
		print("add_pdf_to_merge_exec")
		pdf_single_file_name, _ = QFileDialog.getOpenFileName(None, "Open PDF File", "*.pdf")
		print("Open office file %s"%pdf_single_file_name)
		if pdf_single_file_name != '':	
			pdf_merger.pdf_merge_add_item_to_list(self.pdf_merge_list, pdf_single_file_name)
			pdf_merger.pdf_merge_display(self.pdf_merge_list)
			self.gui_pdf_merge_text_generate_and_display(self.pdf_merge_list)
			# file_name, file_extension = os.path.splitext(pdf_single_file_name)
			# file_basename = os.path.basename(file_name)
			# display_test = "PDF文件列表: " + file_basename
			# self.label_merge_pdf_for_one.setText(display_test)

			# label_new = QLabel()
			# file_name, file_extension = os.path.splitext(pdf_single_file_name)
			# file_basename = os.path.basename(file_name)
			# label_new.setText(file_basename)
			# label_new.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
			# label_new.setAlignment(Qt.AlignCenter)
			# label_new.setFont(QFont("Roman times", 15, QFont.Bold))
			# self.formMergePDF.addWidget(label_new)

	def remove_top_pdf_exec(self):
		print("remove_top_pdf_exec")
		pdf_merger.pdf_merge_remove_item_from_list(self.pdf_merge_list)
		pdf_merger.pdf_merge_display(self.pdf_merge_list)
		self.gui_pdf_merge_text_generate_and_display(self.pdf_merge_list)

	def merge_select_pdf_exec(self):
		print("merge_select_pdf_exec")
		if len(self.pdf_merge_list) == 0:
			print("[merge_select_pdf_exec] file is empty.")
			return
		pdf_merge_name, okPressed = QInputDialog.getText(None, "PDF合成命名", "请输出合成pdf名称:", QLineEdit.Normal, "")
		if okPressed and pdf_merge_name != '':
			pdf_merge_name = pdf_merge_name + '.pdf'
			pdf_merger.pdf_merge_by_list(self.pdf_merge_list, self.pdf_final_merge_file, pdf_merge_name)
		pdf_merger.pdf_merge_display(self.pdf_merge_list)
		self.gui_pdf_merge_text_generate_and_display(self.pdf_merge_list)

	def reset_pdf_merge_exec(self):
		print("reset_pdf_merge_exec")
		pdf_merger.pdf_merge_reset_list(self.pdf_merge_list)
		pdf_merger.pdf_merge_display(self.pdf_merge_list)
		self.gui_pdf_merge_text_generate_and_display(self.pdf_merge_list)

	def gui_pdf_merge_text_generate_and_display(self, pdf_list):
		print("gui_pdf_merge_text_generate_and_display")
		display_test = "PDF文件列表: "
		for pdf_file in pdf_list:
			file_name, file_extension = os.path.splitext(pdf_file)
			file_basename = os.path.basename(file_name)
			display_test += ('\n' + file_basename)
		self.label_merge_pdf_for_one.setText(display_test)

	def sign_on_mouse(self, event, x, y, flags, param):
		global img, crop_origin_file_name, point1, point2
		img2 = img.copy()
		if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
			point1 = (x, y)
			cv2.circle(img2, point1, 10, (0, 255, 0), 5)
			cv2.imshow('image', img2)
			# print("crop img EVENT_LBUTTONDOWN")
		elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
			cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
			cv2.imshow('image', img2)
			# print("crop img EVENT_MOUSEMOVE")
		elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
			point2 = (x, y)
			cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
			print(point1, point2)
			cv2.imshow('image', img2)
			# print("crop img EVENT_LBUTTONUP")

			left = point1[0]
			upper = point1[1]
			right = point2[0]
			lower = point2[1]
			crop = img[upper:lower, left:right]

			crop_image_width = math.fabs(right - left)
			# cv2.imshow(cut)

			img_bg_in = Image.open(crop_origin_file_name)
			img_sg_in = Image.open(self.sig_img_whole_name).convert("RGBA")

			sg_img_origin_width = img_sg_in.size[0]
			sg_img_final_width = crop_image_width
			sg_resize_ratio = float(sg_img_final_width/sg_img_origin_width)

			print("origin width: %d final width: %d  ratio: %f" % (sg_img_origin_width, sg_img_final_width, sg_resize_ratio))
			new_com_img_name = self.box.get_combine_image_name()
			print("---sign_on_mouse. Get new_com_img_name.")
			print(new_com_img_name)
			img_background_add.pdf_img_sinature_exec(img_bg_in, img_sg_in, new_com_img_name, point1, sg_resize_ratio)
			self.box.update_new_img()
			# cv2.imwrite(r'E:\2.png', crop)
			# cv2.imshow(r'E:\2.png', crop)

if __name__ == "__main__":
	print("Running hr sheet manager. Author: Hank and Amy.")
	print("------- version 2.0.0 -------")
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())