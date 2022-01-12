#批量vlookup
#参考:https://blog.csdn.net/ShirleyLGY/article/details/114481873
import pandas as pd
import os
inputdir_path = dir
fileList = os.listdir(inputdir_path)
Writer = pd.ExcelWriter("./kde/merge.xlsx")
#人口密度表，含区域id（"FID_nnbjne"），人口密度
df_density = pd.read_excel("./kde/peopledensity.xlsx")
df_density.head()
#循环读取要查找数据的表
for filename in fileList:
    excelPath = os.path.join(inputdir_path, filename)
    df_poi = pd.read_excel(excelPath)
    df_poi.head()
    #只读取id和poi密度值
    df_poi = df_poi[["FID_nnbjne", "MEAN"]]
    df_poi.head()
    df_merge = pd.merge(left=df_density, right=df_poi,  how="outer", left_on="FID_nnbjne", right_on="FID_nnbjne")
    df_merge.head()
    df_merge.to_excel(Writer, sheet_name=filename.replace(".xlsx",""), index=False)
Writer.save()
Writer.close()
