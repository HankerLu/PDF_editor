import fitz
import re
import os

g_pdf_path = r'annotation_test.pdf'  # PDF 文件路径
g_img_path = r''  # 存放图片的文件夹

def pdf2image_tranfer(pdf_path, img_path):
    # checkIM = r"/Subtype(?= */Image)" # 正则表达式
    # pdf = fitz.open(pdf_path)
    # lenXREF = pdf.xref_length() # 最新fitz库是没有._getXrefLength()
    # count = 1
    # print(lenXREF)
    # for i in range(1, lenXREF):
    #     text = pdf.xref_object(i)# 最新fitz库是没有.getObjectString()
    #     isImage = re.search(checkIM, text)
    #     if not isImage:
    #         continue
    #     pix = fitz.Pixmap(pdf, i)
    #     if pix.size < 10000:  # 在这里添加一处判断一个循环
    #         continue  # 不符合阈值则跳过至下
    #     new_name = f"pdf2img_{count}.png"
    #     pix._writeIMG(os.path.join(img_path, new_name), 0)
    #     count += 1
    #     pix = None
    pdf_file = fitz.open(pdf_path)

    # 遍历PDF的所有页面
    for page_index in range(len(pdf_file)):
        # 获取页面对象
        page = pdf_file[page_index]

        # 将页面转换为图像对象
        pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))

        # 保存图像文件
        img_path = 'tmp_img_page{}.png'.format(page_index)
        pix._writeIMG(img_path, 0)

    # 关闭PDF文件
    pdf_file.close()


if __name__ == "__main__":
    pdf2image_tranfer(g_pdf_path, g_img_path)