#参考https://blog.csdn.net/milton2017/article/details/54406482
#merge two files

import pandas as pd
import os
firstname="English-57-3-ZM-XN-D5-91-SCFAs-结果"
firstname_No="Taxon_"+"14.3_"+firstname
second="English-57-3-ZM-XN-D5-91-SCFAs-结果"
#first = firstname +'-SCFA'
#6271270
path1="D:\\20210911-FINAL\\scfa\\"+firstname+".xlsx"
path2="D:\\20210911-FINAL\\scfa\\"+second+".xlsx"
df1 = pd.DataFrame(pd.read_excel(path1))
df2 = pd.DataFrame(pd.read_excel(path2))
print(df1)
print(df2)
frames=[df1,df2]
#final_file=df1.append(df2)可以上下合并
final_file=pd.concat(frames)
#final_file = pd.merge(df1, df2)
final_file.to_excel('D:\\20210911-FINAL\\merged\\'+firstname+'-SPME-SCFA-Merged.xlsx', index=False)
import sys #print with color
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
prRed(final_file)

import pandas as pd
dffnl = pd.read_excel('D:\\20210911-FINAL\\merged\\'+firstname+'-SPME-SCFA-Merged.xlsx')
print("Here is the df:\n",dffnl)

#Trim the free spaces in front of the data
cols = dffnl.select_dtypes(['object']).columns
dffnl[cols] = dffnl[cols].apply(lambda x: x.str.strip())
#df1=df.sort_index(axis=1)
#df.sort_values(by='ID')
dffnl1 = dffnl.sort_values(by=['Name'])
print("Here is the df1:\n",dffnl1)
merged_path='D:\\20210911-FINAL\\merged\\'+firstname_No+'-SPME-SCFA-Merged.xlsx'
dffnl1.to_excel(merged_path)

import pandas as pd
df = pd.read_excel(merged_path)
print("Here is the df:\n",df)

#trim
cols = df.select_dtypes(['object']).columns # Trim the free spaces in front of the data
df[cols] = df[cols].apply(lambda x: x.str.strip())
#df1=df.sort_index(axis=1)
#df.sort_values(by='ID')
df1 = df.sort_values(by=['Name'])
print("Here is the df1:\n",df1)
df1.to_excel(merged_path)

## 1 Remove duplicates on all columns
#df.drop_duplicates()
import sys #print with color
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
dfx = pd.read_excel(merged_path)
#2 Remove duplicates on select column
df2=dfx.drop_duplicates('Name', keep='last')
prRed(df2)
df2.to_excel(merged_path)




