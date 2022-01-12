
#path = r'C:/Users/Administrator/Desktop/A1'
import os

pathdir = r"D:/USB-GCMS-FILES/GCMS-DATA/GCMS文件大全/GCMS20200928/SCFAs-20200928"
for file in os.listdir(pathdir):
    ext = os.path.splitext(file)

    if ext[1] == '.qgd':
        newext = '-SCFAs-20200928.qgd'
        filename = ext[0] + newext
        oldfile = os.path.join(pathdir, file)
        newfile = os.path.join(pathdir, filename)
        os.rename(oldfile, newfile)