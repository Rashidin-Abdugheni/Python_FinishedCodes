from scihub import SciHub
import time,random

def download_doi(path,refdata):
    for i in range(len(refdata)):
        sleeptime=random.randint(0,25)
        print('-----进度-------',str((num+1)/len(title_doilist)*100),'%')
        title=refdata['Title'][i]
        doiname=refdata['DOI'][i]
        refname=path+"\\"+title.replace(' ','_')+'.pdf'
        if os.path.exists(refname):
            print('已存在:',refname,doiname)
        else:
            if doiname=='Null':
                print('没有DOI：',refname)
            else:
                try:
                    print('开始下载：',title,doiname)
                    time.sleep(sleeptime)
                    sh = SciHub()
                    result = sh.download(doiname, path=refname)
                    if os.path.exists(refname):
                        print('√下载完成',title,doiname)
                    else:
                        print('×下载失败',title,doiname)
                except:
                    print('×下载失败',title,doiname)
