import os
import win32com.client
from win32com.client import Dispatch, constants, gencache, DispatchEx

class PdfGenerator:
    def __init__(self, _export_folder):
        print("Init pdf generator.")
        self._handle_postfix = ['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']
        self._export_folder = _export_folder

    def _is_legal_postfix(self, filename):
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith(
            '~')

    def run_office_2_pdf_transfer(self, filename):
        postfix = filename.split('.')[-1].lower()
        funcCall = getattr(self, postfix)
        filename_whole_path = os.path.abspath(filename)
        print('原文件：', filename_whole_path)
        funcCall(filename_whole_path)
        print('转换完成！')

    def doc(self, filename):
        '''
        doc 和 docx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        print('保存 PDF 文件：', exportfile)
        # gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        # w = Dispatch("Word.Application")
        # doc = w.Documents.Open(filename)
        # doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF,
        #                         Item=constants.wdExportDocumentWithMarkup,
        #                         CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        #
        # w.Quit(constants.wdDoNotSaveChanges)
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(filename, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF)
        word.Quit()
    # def doc(self, filename):
    #     name = os.path.basename(filename).split('.')[0] + '.pdf'
    #     exportfile = os.path.join(self._export_folder, name)
    #     word_app = win32com.client.Dispatch("Word.Application")
    #     word_document = word_app.Documents.Open(filename)
    #     word_document.ExportAsFixedFormat(exportfile, 
    #                                     ExportFormat=17, 
    #                                     CreateBookmarks=win32com.client.constants.wdExportCreateNoBookmarks)
    #     word_document.Close()
    #     word_app.Quit()

    def docx(self, filename):
        self.doc(filename)

    def xls(self, filename):
        '''
        xls 和 xlsx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = DispatchEx("Excel.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('保存 PDF 文件：', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename)

    def ppt(self, filename):
        '''
        ppt 和 pptx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        p = Dispatch("PowerPoint.Application")
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixedFormat(exportfile, 2, PrintRange=None)
        print('保存 PDF 文件：', exportfile)
        p.Quit()


    def pptx(self, filename):
        self.ppt(filename)


if __name__ == "__main__":
    p_g = PdfGenerator('.')
    p_g.xls('1.xlsx')
    # p_g.run_conver()
    # p_g.pdf_multi_files_merge("D:\Entrepreneurship\HankAmy\SW2304\hr_sheet_manager\pdfconver")


