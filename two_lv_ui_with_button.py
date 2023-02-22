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
import math
import os

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

		self.sig_op_form = sig_operator.SigOperator()

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
		self.label0 = QLabel()
		self.label0.setText("Amy HR Assistant")
		self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label0.setAlignment(Qt.AlignCenter)
		self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout.addWidget(self.label0)  # 添加控件

		# 设置第1个面板：
		self.form_office2pdf = QWidget()
		self.formLayoutOffice2PDF = QHBoxLayout(self.form_office2pdf)  # 水平布局
		self.label_office2pdf = QLabel()
		self.label_office2pdf.setText("office文件转换")
		self.label_office2pdf.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_office2pdf.setAlignment(Qt.AlignCenter)
		self.label_office2pdf.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayoutOffice2PDF.addWidget(self.label_office2pdf)  # 添加控件

		# 设置第2个面板：
		self.form_sign_create = QWidget()
		self.formLayoutSignCreate = QHBoxLayout(self.form_sign_create)
		self.label_sign_create = QLabel()
		self.label_sign_create.setText("签名制作")
		self.label_sign_create.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_sign_create.setAlignment(Qt.AlignCenter)
		self.label_sign_create.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayoutSignCreate.addWidget(self.label_sign_create)
		
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

		self.button_sign_save = QtWidgets.QPushButton(self.form_sign_create)
		self.button_sign_save.setGeometry(QtCore.QRect(30, 400, 81, 41))
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
		self.form3 = QWidget()
		self.formLayout3 = QHBoxLayout(self.form3)
		self.label3 = QLabel()
		self.label3.setText("当前签名文件： %s"%self.img_signature_select)
		self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label3.setAlignment(Qt.AlignCenter)
		self.label3.setFont(QFont("Roman times", 30, QFont.Bold))
		self.formLayout3.addWidget(self.label3)

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

		self.box = img_crop_edit.ImageBox()
		# self.formLayoutSignSinglePage.addWidget(self.box)
		self.gridLayout.addWidget(self.box)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.open_pdf = QtWidgets.QPushButton(self.form_sign_single_page)
		self.open_pdf.setGeometry(QtCore.QRect(30, 100, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.open_pdf.setFont(font)
		self.open_pdf.setObjectName("open_pdf")
		self.open_pdf.clicked.connect(self.open_pdf_exec)

		self.sign_page = QtWidgets.QPushButton(self.form_sign_single_page)
		self.sign_page.setGeometry(QtCore.QRect(30, 200, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.sign_page.setFont(font)
		self.sign_page.setObjectName("sign_page")
		self.sign_page.clicked.connect(self.sign_page_exec)

		self.confirm_edit = QtWidgets.QPushButton(self.form_sign_single_page)
		self.confirm_edit.setGeometry(QtCore.QRect(30, 300, 81, 41))
		font = QtGui.QFont()
		font.setFamily("Aharoni")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.confirm_edit.setFont(font)
		self.confirm_edit.setObjectName("confirm_edit")
		self.confirm_edit.clicked.connect(self.confirm_edit_exec)

		self.form6 = QWidget()
		self.formLayout6 = QHBoxLayout(self.form6)
		self.label6 = QLabel()
		self.label6.setText("PDF文件合成")
		self.label6.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label6.setAlignment(Qt.AlignCenter)
		self.label6.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout6.addWidget(self.label6)

		self.form7 = QWidget()
		self.formLayout7 = QHBoxLayout(self.form7)
		self.label7 = QLabel()
		self.label7.setText("啦啦啦啦啦，就不告诉你，略略略")
		self.label7.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label7.setAlignment(Qt.AlignCenter)
		self.label7.setFont(QFont("微软雅黑", 40, QFont.Bold))
		self.formLayout7.addWidget(self.label7)

		# stackedWidget添加各种界面用于菜单切换
		self.stackedWidget.addWidget(self.form_main_windoow)
		self.stackedWidget.addWidget(self.form_office2pdf)
		self.stackedWidget.addWidget(self.form_sign_create)
		self.stackedWidget.addWidget(self.form3)
		self.stackedWidget.addWidget(self.form_sign_single_page)
		# self.stackedWidget.addWidget(self.form5)
		self.stackedWidget.addWidget(self.form6)
		self.stackedWidget.addWidget(self.form7)

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

		self.button_sign_create.setText(_translate("Form", "新建签名"))
		self.button_sign_save.setText(_translate("Form", "保存签名"))

		self.open_pdf.setText(_translate("Form", "打开PDF"))
		self.sign_page.setText(_translate("Form", "签名此页"))
		self.confirm_edit.setText(_translate("Form", "确认修改"))

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
		self.label3.setText("当前签名文件： %s"%self.img_signature_select)
		self.stackedWidget.setCurrentIndex(3)
	def goto_sign_operation(self):
		self.stackedWidget.setCurrentIndex(4)
	def goto_pdf_multi_merge(self):
		self.stackedWidget.setCurrentIndex(5)
	def goto_about_us_intro(self):
		self.stackedWidget.setCurrentIndex(6)

	def sign_create_exec(self):
		print("create new sign")
		# self.box.display_img()
		self.sig_op_form.show()

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
		img = cv2.imread(crop_origin_file_name)
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
		sig_name_in,sig_extension = os.path.splitext(self.img_signature_select)
		print(sig_name_in)
		self.box.pdf_recover_from_imgs(sig_name_in)

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
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())