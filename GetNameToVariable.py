
f = open('C:\\Users\\Mr.R\\Desktop\\test\\list\\list.txt', "r" )
lines = []
for line in f:
    line = line.strip()
    newid = line
    print(newid)#获取单行的内容作为下一步的variable

    path='C:\\Users\\Mr.R\\Desktop\\test\\target\\'+newid+'.txt'
    #file=open('C:\\Users\\Mr.R\\Desktop\\'+newid+'.txt', "r")
    textfile = open(path, "w")
    a = textfile.write('pythonguides---'+newid)
    textfile.close()
   # text = file.read().strip()
    print("text:"+newid)

f.close()
