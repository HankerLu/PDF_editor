import sys
from pathlib import Path
import xsl2pdf
import sig_operator

if __name__ == "__main__":

    print("Running hr sheet manager. Author: Hank and Amy.")
    print("------- version 1.0.1 -------")

    base_dir = 'D:\Entrepreneurship\HankAmy\SW2304\hr_sheet_manager\sheet'
    keywords = '1'

    p = Path(base_dir)

    # 当前目录下包含BBC的所有文件名称
    #files = p.glob(keywords)
    # files的类型是迭代器
    # 通过list()函数转换为列表输出
    # print(list(files))

    # 遍历子目录和所有文件
    #files3 = p.glob('**/*')
    #print(list(files3))

    # xlsx结尾的文件
    files_excel_all = p.rglob('*.xlsx')
    #print(list(files_excel_all))


    for excel in files_excel_all:
        if '1' in str(excel):
            print(excel)

    # pdf_gen = xsl2pdf.PdfGenerator(".")
    # pdf_gen.gen_single_pdf_from_1st_sheet()
    # pdf_gen.run_conver()

    sig_op = sig_operator.SigOperator()
    sig_op.sig_operator_run()