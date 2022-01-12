import pandas as pd

df = pd.read_excel('C:\\Users\Administrator\\Desktop\\GCMS-FINAL-20210827\\GCMS-FINAL-XLSX-20210827\\English-files\\English\\English-1-L4-N-CBN-D24-32-SPME.xlsx',sheet_name='Sheet1')

cols = df.select_dtypes(['object']).columns # Trim the free spaces in front of the data
df[cols] = df[cols].apply(lambda x: x.str.strip())
print (df)
df.to_excel("C:\\Users\Administrator\\Desktop\\GCMS-FINAL-20210827\\GCMS-FINAL-XLSX-20210827\\English-files\\English\\AA-English-1-L4-N-CBN-D24-32-SPME.xlsx")

