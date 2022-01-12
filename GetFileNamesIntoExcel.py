# 打开目标目录并且对其中的所有文件提取其文件名，并把文件名写到xl文件
import os
file_dir = "D:\\20210911-FINAL\\merged\\Taxon-dropduplicated\\"
for root, dirs, files in os.walk(file_dir, topdown=False):
    print(root)     # 当前目录路径
    print(dirs)     # 当前目录下所有子目录
    print(files)        # 当前路径下所有非目录子文件
f = open (r'D:\\20210911-FINAL\\Names_all.txt','w')
print (files,file = f)
f.close()

#重开个txt文件，进行换行，进行替换，来调整格式，
fin = open('D:\\20210911-FINAL\\Names_all.txt', "rt") #打开一个txt文件
data = fin.read()#读取txt
#replace all occurrences of the required string
data = data.replace(".xlsx', '", "\n") #找到特殊字符进行替换
#data = data.replace(".qgd', '", "\n") #找到特殊字符进行替换
data = data.replace(".xlsx']", "")
#data = data.replace("['", "")
#close the input file
fin.close()
#open the input file in write mode
fin = open('D:\\20210911-FINAL\\Names_all.txt', "wt")
#overrite the input file with the resulting data
fin.write(data)#将处理好的结果再写进前面的txt内。
#close the file
fin.close()
print("Name of data:",data)

import os
import xlwt
#p="D:\\20210911-FINAL\\scfa\\"#
datas=os.listdir('D:\\20210911-FINAL\\merged\\Taxon-dropduplicated\\')
datas=list(datas)
a = xlwt.Workbook(encoding='utf-8')
s = a.add_sheet('namelist',cell_overwrite_ok=True)
i=0
for x in datas:
        s.write(i,0,x)
        i=i+1
a.save('D:\\20210911-FINAL\\merged\\Merged-SCFA-SPME-list-913.xls')
