import pandas as pd

df = pd.read_excel('D:\\GCMS -Final-Trimed-20210910.xlsx',sheet_name='Sheet1')

cols = df.select_dtypes(['object']).columns # Trim the free spaces in front of the data
df[cols] = df[cols].apply(lambda x: x.str.strip())
print (df)


#df1=df.sort_index(axis=1)
#print(df1)

df.to_excel("D:\\GCMS -Final-Trimed-20210910.xlsx")
