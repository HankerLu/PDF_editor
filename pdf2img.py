import fitz
import re
import os

file_path = r'combine_new.pdf'  # PDF 文件路径
dir_path = r''  # 存放图片的文件夹
def pdf2image1(path, pic_path):
    checkIM = r"/Subtype(?= */Image)" # 正则表达式
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length() # 最新fitz库是没有._getXrefLength()
    count = 1
    print(lenXREF)
    for i in range(1, lenXREF):
        text = pdf.xref_object(i)# 最新fitz库是没有.getObjectString()
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        if pix.size < 10000:  # 在这里添加一处判断一个循环
            continue  # 不符合阈值则跳过至下
        new_name = f"img_{count}.png"
        pix._writeIMG(os.path.join(pic_path, new_name), 0)
        count += 1
        pix = None


if __name__ == "__main__":
    pdf2image1(file_path, dir_path)