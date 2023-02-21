import os
from PyPDF2 import PdfMerger

def pdf_multi_files_merge(files_in_path, files_out_name):
    print("Run pdf_multi_files_merge.path %s" % files_in_path)
    # target_path = r'pdf'
    pdf_lst = [f for f in os.listdir(files_in_path) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(files_in_path, filename) for filename in pdf_lst]

    file_merger = PdfMerger()
    for pdf in pdf_lst:
        # print(pdf)
        file_merger.append(pdf)  # 合并pdf文件

    file_merger.write(files_out_name)