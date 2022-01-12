# 重要：安装xlrd时要安装以下这个！
# pip install xlrd==1.2.0
# pip install pandas

import os
import pandas as pd
import numpy as np


dir= "D:\\GCMS-DATA-Management20210825\\GCMS-FINAL-20210829\\GCMS-FINAL-XLSX-20210827\\English-files"#设置工作路径，读取其中的多个excel表

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

#合并文件输出
result.to_csv('D:\\GCMS-DATA-Management20210825\\GCMS-FINAL-20210829\\GCMS-FINAL-XLSX-20210827\\English-files-MergedOnly-With-CK.csv', sep=',', index=False)

#3 Transfer csv into xlsx

import openpyxl
import csv

wb = openpyxl.Workbook()
sh = wb.create_sheet('GC-MS')

with open('D:\\GCMS-DATA-Management20210825\\GCMS-FINAL-20210829\\GCMS-FINAL-XLSX-20210827\\English-files-MergedOnly-With-CK.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        sh.append(row)

wb.save('D:\\GCMS-DATA-Management20210825\\GCMS-FINAL-20210829\\GCMS-FINAL-XLSX-20210827\\English-files-MergedOnly-With-CK.xlsx')

