import os
# pip install xlwings
import xlwings as xw
f='C:\\Users\\Mr.R\\Desktop\\test\\target'
l=os.listdir(f)

app=xw.App(visible=False, add_book=False)
for i in f:
    if i.startswith('~$'):
        continue
        fp=os.path.join(f,i)
        workbook=app.books.open(fp)
        workbook.api.PrintOut()
app.quit()