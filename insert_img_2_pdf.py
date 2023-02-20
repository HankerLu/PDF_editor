# import PyPDF2
#
# # 打开PDF文件
# pdf_file = open('example.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#
# # 创建一个新的PDF页面
# pdf_output = PyPDF2.PdfFileWriter()
#
# # 将原始PDF文件的所有页面添加到新的PDF页面中
# for page_num in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(page_num)
#     pdf_output.addPage(page)
#
# # 获取第一页
# page = pdf_output.getPage(0)
#
# # 读取要插入的图片
# with open('image.jpg', 'rb') as image_file:
#     image = PyPDF2.pdf.ImageReader(image_file)
#
# # 计算图片在页面上的位置和大小
# x = 100   # 图片的左上角在页面上的X坐标
# y = 100   # 图片的左上角在页面上的Y坐标
# width = image.getSize()[0]   # 图片的宽度
# height = image.getSize()[1]  # 图片的高度
#
# # 将图片添加到页面的指定位置
# page.mergeTranslatedPage(image, x, y, expand=False)
#
# # 将新的PDF页面保存到文件
# with open('output.pdf', 'wb') as output_file:
#     pdf_output.write(output_file)
#
# # 关闭文件
# pdf_file.close()