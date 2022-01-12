import os

# 打开目标目录并且对其中的所有文件提取其文件名，并把文件名写到txt文件
file_dir = "D:/USB-GCMS-FILES/GCMS全部文件/GCMS20201119-1-32带着编号-RXD-SCFAs"
for root, dirs, files in os.walk(file_dir, topdown=False):
    print(root)     # 当前目录路径
    print(dirs)     # 当前目录下所有子目录
    print(files)        # 当前路径下所有非目录子文件

f = open (r'D:/USB-GCMS-FILES/GCMS全部文件/GCMS20201119-1-32带着编号-RXD-SCFAs_all.txt','w')

print (files,file = f)

f.close()

#重开个txt文件，进行换行，进行替换，来调整格式，
fin = open('D:/USB-GCMS-FILES/GCMS全部文件/GCMS20201119-1-32带着编号-RXD-SCFAs_all.txt', "rt") #打开一个txt文件
data = fin.read()#读取txt
#replace all occurrences of the required string
data = data.replace(".qgd', '", "-SCFAs-GCMS20201119\n") #找到特殊字符进行替换
#data = data.replace(".qgd', '", "\n") #找到特殊字符进行替换
data = data.replace(".qgd']", "")
data = data.replace("['", "")
#close the input file
fin.close()
#open the input file in write mode
fin = open('D:/USB-GCMS-FILES/GCMS全部文件/GCMS20201119-1-32带着编号-RXD-SCFAs_Final_List.txt', "wt")
#overrite the input file with the resulting data
fin.write(data)#将处理好的结果再写进前面的txt内。
#close the file
fin.close()

#D:/USB-GCMS-FILES/GCMS-DATA/GCMS文件大全/GCMS20200902/GCMS结果20200902WWZ拷贝/Sample
