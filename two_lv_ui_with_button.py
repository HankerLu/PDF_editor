import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


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

	def setupUi(self, MainWindow):
		# 创建界面
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1440, 773)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)
		# 一级菜单栏布置
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
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
		self.action_sign_confirm.setObjectName("action_sign_confirm")
		self.action_pdf_multi_merge.setObjectName("action_pdf_multi_merge")
		self.action_about_us.setObjectName("action_about_us")
		self.menu_pdf_tran.addAction(self.actionoffice2pdf)
		self.menu_pdf_edit.addAction(self.action_sign_generate)
		self.menu_pdf_edit.addAction(self.action_sign_select)
		self.menu_pdf_edit.addAction(self.action_sign_single_page)
		self.menu_pdf_edit.addAction(self.action_sign_confirm)
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
		self.form2 = QWidget()
		self.formLayout2 = QHBoxLayout(self.form2)
		self.label2 = QLabel()
		self.label2.setText("签名制作")
		self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label2.setAlignment(Qt.AlignCenter)
		self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout2.addWidget(self.label2)

		# 设置第3个面板：
		self.form3 = QWidget()
		self.formLayout3 = QHBoxLayout(self.form3)
		self.label3 = QLabel()
		self.label3.setText("签名选择")
		self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label3.setAlignment(Qt.AlignCenter)
		self.label3.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout3.addWidget(self.label3)

		# 设置第4个面板：
		self.form_sign_single_page = QWidget()
		self.formLayoutSignSinglePage = QHBoxLayout(self.form_sign_single_page)
		self.label_sign_single_page = QLabel()
		self.label_sign_single_page.setText("签名单页")
		self.label_sign_single_page.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label_sign_single_page.setAlignment(Qt.AlignCenter)
		self.label_sign_single_page.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayoutSignSinglePage.addWidget(self.label_sign_single_page)

		# 设置第5个面板：
		self.form5 = QWidget()
		self.formLayout5 = QHBoxLayout(self.form5)
		self.label5 = QLabel()
		self.label5.setText("签名确认")
		self.label5.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label5.setAlignment(Qt.AlignCenter)
		self.label5.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout5.addWidget(self.label5)
		# 设置第6个面板：
		self.form6 = QWidget()
		self.formLayout6 = QHBoxLayout(self.form6)
		self.label6 = QLabel()
		self.label6.setText("PDF文件合成")
		self.label6.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label6.setAlignment(Qt.AlignCenter)
		self.label6.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout6.addWidget(self.label6)
		# 设置第7个面板：
		self.form7 = QWidget()
		self.formLayout7 = QHBoxLayout(self.form7)
		self.label7 = QLabel()
		self.label7.setText("关于 HR Assistant")
		self.label7.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.label7.setAlignment(Qt.AlignCenter)
		self.label7.setFont(QFont("Roman times", 50, QFont.Bold))
		self.formLayout7.addWidget(self.label7)

		# stackedWidget添加各种界面用于菜单切换
		self.stackedWidget.addWidget(self.form_main_windoow)
		self.stackedWidget.addWidget(self.form_office2pdf)
		self.stackedWidget.addWidget(self.form2)
		self.stackedWidget.addWidget(self.form3)
		self.stackedWidget.addWidget(self.form_sign_single_page)
		self.stackedWidget.addWidget(self.form5)
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
		self.actionoffice2pdf.triggered.connect(self.gotoColorWin)
		# PDF编辑功能1：签名制作
		self.action_sign_generate.setText(_translate("MainWindow", "签名制作"))
		self.action_sign_generate.triggered.connect(self.gotoTexWin)
		# PDF编辑功能2：签名选择
		self.action_sign_select.setText(_translate("MainWindow", "签名选择"))
		self.action_sign_select.triggered.connect(self.gotoDaisyWin)
		# PDF编辑功能3：签名单页
		self.action_sign_single_page.setText(_translate("MainWindow", "签名单页"))
		self.action_sign_single_page.triggered.connect(self.gotoEHDWin)
		# PDF编辑功能4：签名确认
		self.action_sign_confirm.setText(_translate("MainWindow", "签名确认"))
		self.action_sign_confirm.triggered.connect(self.gotoHOGWin)
		# PDF合成功能1：PDF排序合成
		self.action_pdf_multi_merge.setText(_translate("MainWindow", "PDF文件合成"))
		self.action_pdf_multi_merge.triggered.connect(self.gotoVGGWin)
		# deep-learning方法2：ResNet
		self.action_about_us.setText(_translate("MainWindow", "关于 HR Assistant"))
		self.action_about_us.triggered.connect(self.gotoResWin)

	# 菜单栏触发每个界面调用函数
	def gotoColorWin(self):
		self.stackedWidget.setCurrentIndex(1)
	def gotoTexWin(self):
		self.stackedWidget.setCurrentIndex(2)
	def gotoDaisyWin(self):
		self.stackedWidget.setCurrentIndex(3)
	def gotoEHDWin(self):
		self.stackedWidget.setCurrentIndex(4)
	def gotoHOGWin(self):
		self.stackedWidget.setCurrentIndex(5)
	def gotoVGGWin(self):
		self.stackedWidget.setCurrentIndex(6)
	def gotoResWin(self):
		self.stackedWidget.setCurrentIndex(7)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())