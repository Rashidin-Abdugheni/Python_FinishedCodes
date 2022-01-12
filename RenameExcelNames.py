import os

pathdir = r"G:\\GCMS-TABLE\\Splited_SPME0307"
for file in os.listdir(pathdir):
    ext = os.path.splitext(file)

    if ext[1] == '.csv':
        newext = '.xlsx'
        filename = ext[0] + newext
        oldfile = os.path.join(pathdir, file)
        newfile = os.path.join(pathdir, filename)
        os.rename(oldfile, newfile)
