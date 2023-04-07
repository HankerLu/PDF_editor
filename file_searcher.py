import sys
from pathlib import Path

base_dir = '.\sheet'

def office_file_search():
    p = Path(base_dir)
    # xlsx结尾的文件
    files_excel_all = p.rglob('*.xlsx')
    for excel in files_excel_all:
        if '1' in str(excel):
            print(excel)

if __name__ == "__main__":
    print("Running office 2 pdf.")