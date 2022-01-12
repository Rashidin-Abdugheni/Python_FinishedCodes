# 重要：安装xlrd时要安装以下这个！
# pip install xlrd==1.2.0
# pip install pandas

#1 Move files based on file extension
import glob
import os
import shutil

#path= 'D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210803-SCFA-Done'
src_folder = r'D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals'
dst_folder = r"D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1\\"

# Search files with .txt extension in source directory
pattern = "\*.xlsx"
files = glob.glob(src_folder + pattern)

# move the files with txt extension
for file in files:
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)


#2 Merge xlsx files
import os
import pandas as pd
import numpy as np


dir = "D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1"#设置工作路径，读取其中的多个excel表

#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:

        filename_excel.append(os.path.join(root,file))

        # excel转换成DataFrame
        df = pd.read_excel(os.path.join(root,file))
        frames.append(df)
#打印文件名
print(filename_excel)

 #合并所有数据
result = pd.concat(frames)

#查看合并后的数据
result.head()
result.shape

#Merge and output
result.to_csv('D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1.csv',sep=',', index=False)

#3 Transfer csv into xlsx

import openpyxl
import csv

wb = openpyxl.Workbook()
sh = wb.create_sheet('GCMS-DATA')

with open('D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        sh.append(row)

wb.save('D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1.xlsx')

#4 sort the data: reference
#https://pythoninoffice.com/sort-excel-data-using-python/
import pandas as pd

df = pd.read_excel('D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\1.xlsx',sheet_name='GCMS-DATA')

print(df)

#df1=df.sort_index(axis=1)
#print(df1)

#df.sort_values(by='ID')

print(",\,")
df1=df.sort_values(by=['Name'])
print(df1)


df1.to_excel("D:\\GCMS-DATA-Management20210825\\GCMS-DATA-FINAL\\GCMS-20210825\\20210825Finals\\Final.xlsx")

