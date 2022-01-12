#pip install PyPDF2

from PyPDF2 import PdfFileMerger, PdfFileReader
from glob import glob

print(glob(pathname="D:\\0-Non-LachnospiraceaeFiles\\简历Resume\\文章首页/*.pdf"))

mergepdf_base = PdfFileMerger()

for temppdfname in glob(pathname="D:\\0-Non-LachnospiraceaeFiles\\简历Resume\\文章首页/*.pdf"):
    mergepdf_base.append(PdfFileReader(temppdfname))
    print("These are target PDF files:", temppdfname)

mergepdf_base.write("D:\\0-Non-LachnospiraceaeFiles\\简历Resume\\文章首页2015-202109所有热西丁文章Merged.pdf")
 #Print("Merging of PDF files is finished！")

