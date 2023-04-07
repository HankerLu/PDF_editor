
from PIL import Image
import img2pdf
import os

def pdf_img_sinature_exec(img_pdf, img_signature, path_file_result, sign_pos, sign_ratio):
    img_sg_reize_w = int(img_signature.size[0] * sign_ratio)
    img_sg_reize_h = int(img_signature.size[1] * sign_ratio)
    # print("pdf_img_sinature_exec  w:%d h:%d" %(img_sg_reize_w, img_sg_reize_h))
    img_sg_resize = img_signature.resize((img_sg_reize_w, img_sg_reize_h), 1)
    # img_sg_resize.show()
    print(img_signature.size[0], img_signature.size[1])
    print(img_sg_resize.size[0], img_sg_resize.size[1])

    img_pdf.paste(img_sg_resize, (sign_pos[0], sign_pos[1]), mask = img_sg_resize)
    img_pdf.save(path_file_result)
    img_pdf.show()

    print("Image read background and signature.")

# def pdf_recover_from_imgs(file_in_root, file_in_imgs, path_out_pdf):
#     cnt = 0
#     if len(file_in_imgs) == 0:
#         print("[pdf_recover_from_imgs]File list is empty.")
#         return
#     file_name, file_extension = os.path.splitext(file_in_imgs[0])
#     base_name = os.path.basename(file_name)
#     for img in file_in_imgs:
#         print("img name: %s" %(img))
#         total_file_name = os.path.join(file_in_root, img)
#         img_b = Image.open(total_file_name)
#         bg_sg_combine_pdf_bytes = img2pdf.convert(img_b)
#         file_single_out_pdf = path_out_pdf + base_name + '.pdf'
#         print(file_single_out_pdf)
#         file = open(file_single_out_pdf, "w")
#         file.write(bg_sg_combine_pdf_bytes)
#         file.close()
#         cnt + 1
    

if __name__ == "__main__":
    img_bg_path = 'D:\Entrepreneurship\HankAmy\SW2304\hr_sheet_manager\pyqt_display_test.png'
    img_sg_path = 'D:\Entrepreneurship\HankAmy\SW2304\hr_sheet_manager\signature.png'
    img_bg = Image.open(img_bg_path)
    img_sg = Image.open(img_sg_path).convert("RGBA")

    img_sg_resize_ratio = 0.5

    pdf_img_sinature_exec(img_bg, img_sg, 'combine_new.pdf', (500, 500), 0.7)

    # img_bg = Image.open(img_bg_path)
    # img_sg = Image.open(img_sg_path).convert("RGBA")
    #
    # img_sg_reize_w = int(img_sg.size[0] * img_sg_resize_ratio)
    # img_sg_reize_h = int(img_sg.size[1] * img_sg_resize_ratio)
    # print(img_sg_reize_w, img_sg_reize_h)
    # img_sg_resize = img_sg.resize((img_sg_reize_w, img_sg_reize_h), 0)
    # print(img_sg.size[0], img_sg.size[1])
    # print(img_sg_resize.size[0], img_sg_resize.size[1])
    #
    # img_bg.paste(img_sg_resize, (0, 500), mask = img_sg_resize)
    # img_bg.show()
    # print("Image read background and signature.")
