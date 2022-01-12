import pandas as pd

df = pd.read_excel('D:\GCMS-DATA-Management20210825\GCMS-DATA-FINAL\GCMS-Blautia\\Final-GCMS-20210825-and Blautia-andL.e.xlsx',sheet_name='Sheet1')

print(df)

#df1=df.sort_index(axis=1)
#print(df1)

#df.sort_values(by='ID')

print(",\,")
df1=df.sort_values(by=['Name'])
print(df1)


df1.to_excel("D:\GCMS-DATA-Management20210825\GCMS-DATA-FINAL\GCMS-Blautia\\Final-GCMS-20210825-and Blautia-andL.e-Sorted.xlsx")
