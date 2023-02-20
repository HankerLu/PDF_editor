import PyPDF2

# 打开PDF文件
pdf_file = open('amy_final.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# 获取第一页
page = pdf_reader.getPage(0)

# 获取页面的Media Box
media_box = page.mediaBox

# 输出页面的大小和位置
print('Media Box:')
print('Left:', media_box.getLowerLeft_x())
print('Bottom:', media_box.getLowerLeft_y())
print('Right:', media_box.getUpperRight_x())
print('Top:', media_box.getUpperRight_y())

# 获取页面的Crop Box
crop_box = page.cropBox

# 输出页面内容的实际边界
print('Crop Box:')
print('Left:', crop_box.getLowerLeft_x())
print('Bottom:', crop_box.getLowerLeft_y())
print('Right:', crop_box.getUpperRight_x())
print('Top:', crop_box.getUpperRight_y())

# 关闭文件
pdf_file.close()