#pip install FPDF
import os
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(0)         # 自动分页设为False

path = r"D:\0-Non-LachnospiraceaeFiles\简历Resume\奖状类合并\图片格式"
imagelist = [i for i in os.listdir(path)]


for image in sorted(imagelist):
    pdf.add_page()
    pdf.image(os.path.join(path, image), w=190)      # 指定宽高

pdf.output(os.path.join(path, "就业推荐表.pdf"), "F")