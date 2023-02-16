import sys
from pathlib import Path
import pdf_manager
import sig_operator
import img_crop_edit

base_dir = '.\sheet'

def hr_manager_file_search():
    p = Path(base_dir)
    # xlsx结尾的文件
    files_excel_all = p.rglob('*.xlsx')
    for excel in files_excel_all:
        if '1' in str(excel):
            print(excel)

if __name__ == "__main__":

    print("Running hr sheet manager. Author: Hank and Amy.")
    print("------- version 1.0.1 -------")

    # sig_op = sig_operator.SigOperator()
    # sig_op.sig_operator_run()

    app = img_crop_edit.QtWidgets.QApplication(sys.argv)
    MainWindow = img_crop_edit.QtWidgets.QMainWindow()
    ui = img_crop_edit.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
