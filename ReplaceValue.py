import pandas as pd
import os
df = pd.read_excel(r'D:\\Output-results\\gcms-bar-core.xls')#因为报错所以改成了xls
df.head()
print(df)
df=df.astype(str)#要转换为str类型，不然无法完成替换
#https://www.statology.org/pandas-to-string/
print(df.dtypes)

#将化学物质的列提到第一列

df1 = df.replace('0', '0.000001')
print("df1:", df1)
newpath="D:\\Output-results\\gcms-bar-core-new.xlsx"
df1.to_excel(newpath)

df2 = pd.read_excel(r'D:\\Output-results\\gcms-bar-core-new.xlsx')#因为报错所以改成了xls
df2.head()
print(df2)
#df2=df2.astype(float)#要转换为str类型，不然无法完成替换
#https://www.statology.org/pandas-to-string/
print(df2.dtypes)

newpath2="D:\\Output-results\\gcms-bar-core-new2.xlsx"
df1.to_excel(newpath2)