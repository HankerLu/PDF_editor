import os
from PyPDF2 import PdfMerger

def pdf_merge_add_item_to_list(pdf_file_list, pdf_file):
    print("pdf_merge_add_item_to_list")
    if len(pdf_file_list) != 0:
        pdf_file_list.append(pdf_file)

def pdf_merge_remove_item_from_list(pdf_file_list):
    print("pdf_merge_remove_item_from_list")
    if len(pdf_file_list) != 0:
        del pdf_file_list[-1]

def pdf_merge_reset_list(pdf_file_list):
    print("pdf_merge_reset_list")
    if pdf_file_list:
        del pdf_file_list

def pdf_merge_by_list(pdf_file_list, pdf_merge_out_name):
    print("pdf_merge_by_list")
    if len(pdf_file_list) == 0:
        print("len(pdf_file_list) == 0")
        return 
    list_file_merger = PdfMerger() 
    for single_file in pdf_file_list:
        list_file_merger.append(single_file)
    list_file_merger.write(pdf_merge_out_name)

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