import pandas as pd
df = pd.read_excel('D:\\20210911-FINAL\\Dropduplicates.xlsx')
print("Here is the df:\n",df)

#trim
cols = df.select_dtypes(['object']).columns # Trim the free spaces in front of the data
df[cols] = df[cols].apply(lambda x: x.str.strip())
#df1=df.sort_index(axis=1)
#df.sort_values(by='ID')
df1 = df.sort_values(by=['Name'])
print("Here is the df1:\n",df1)
df1.to_excel("D:\\20210911-FINAL\\Dropduplicates-1.xlsx")

## 1 Remove duplicates on all columns
#df.drop_duplicates()
import sys #print with color
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
dfx = pd.read_excel('D:\\20210911-FINAL\\Dropduplicates-1.xlsx')
#2 Remove duplicates on select column
df2=dfx.drop_duplicates('Name', keep='last')
prRed(df2)
df2.to_excel('D:\\20210911-FINAL\\Dropduplicates-2.xlsx')