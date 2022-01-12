

import pandas as pd

df = pd.read_excel('D:\\USB-GCMS-FILES\\SCFA-GCMS-EXCEL-RESULT_OF_EACH_STRAIN\\English-all.xlsx',sheet_name='GCMS-DATA')

print(df)

#df1=df.sort_index(axis=1)
#print(df1)

#df.sort_values(by='ID')

print(",\,")
df1=df.sort_values(by=['Name'])
print(df1)



df1.to_excel("D:\\USB-GCMS-FILES\\SCFA-GCMS-EXCEL-RESULT_OF_EACH_STRAIN\\English-all-Sorted.xlsx")