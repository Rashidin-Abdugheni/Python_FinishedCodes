import numpy as np
import xlrd
import openpyxl
import pandas as pd
from openpyxl import *

import numpy as np

data = xlrd.open_workbook('G:/GCMS-TABLE/Splited_SPME/SPME-MergedFile1-161.xlsx')
table = data.sheets()[0]

# print(table)
# nrows = table.nrows #行数
# ncols = table.ncols #列数
# c1=arange(0,nrows,1)
# print(c1)

start = 2  # 开始的行
end = 4 # 结束的行

rows = end - start

list_values = []
for x in range(start, end):
    values = []
    row = table.col_values(x)
    for i in range(1, 7):
        # print(value)
        values.append(row[i])
    list_values.append(values)
# print(list_values)
datamatrix = np.array(list_values)
print(datamatrix)

