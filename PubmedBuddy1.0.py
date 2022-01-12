# encoding: utf-8

from tkinter import *
from tkinter.ttk import *
import requests
import re
import webbrowser
import hashlib
import json
import http.client
import urllib
import random
from lxml.html import etree #pip install lxml


# 第二部分 功能实现
# 定义一个函数，根据page获取页面文章标题和id，并显示标题信息
def getpagemessage(page):
    global item, year, titledict, iddict
    url = 'https://pubmed.ncbi.nlm.nih.gov/?term={}&page={}{}'.format(item, page, year)
    r = requests.get(url)
    # 获取文章标题
    reg_title = re.compile('data-article-id="\d{8}">\s*(.*?)\s*</a>')
    titles = reg_title.findall(r.text)
    # 获取期刊和年份
    reg_journal = re.compile('short-journal-citation">(.*?)</span>')
    journals = reg_journal.findall(r.text)
    article_text = []
    for i in range(len(titles)):
        # 替换htmL标签
        reg = re.compile('<[^>]+>')
        titles[i] = reg.sub('', titles[i])
        text = '{}、{}({})\n'.format(str(i + 1), titles[i], journals[i])
        text1.insert('end', text)
        text1.see(END)
        text1.update()
        article_text.append(text)
    titledict[page] = article_text
    # 获取文章id
    reg_id = re.compile('<meta name="log_displayeduids" content="(.*?)" />')
    idlist = reg_id.findall(r.text)
    idlist = idlist[0].split(',')
    iddict[page] = idlist


# 定义一个函数，根据num获取文章摘要并显示
def getabstract(num):
    global iddict, page, absdict
    id = iddict[page][num]
    url = 'https://pubmed.ncbi.nlm.nih.gov/{}/'.format(id)
    r = requests.get(url)
    html = etree.HTML(r.text)
    abs_xpaths = html.xpath('//*[@id="en-abstract"]/p')
    abs = ''
    for abs_xpath in abs_xpaths:
        text = abs_xpath.xpath('./text()')
        text = text[-1].replace('\n', '').strip()
        abs += text + '\n'
    reg_title = re.compile('<title>(.*?) - PubMed</title>')
    title = reg_title.findall(r.text)[0] + '.'
    content = title + '\n' + abs
    content = content.replace('&#39;', "' ")
    # 替换htmL标签
    reg = re.compile('<[^>]+>')
    content = reg.sub('', content)
    text2.delete(1.0, 'end')  # 清空文本框
    text2.insert('end', content)
    text2.see(END)
    text2.update()
    absdict[id] = content


# 定义一个函数，根据年份搜索,并显示搜索结果
def search_by_year(year):
    # 恢复初始值
    global item, page, titledict, iddict, absdict, num, max_page, counts
    item = entry1.get().replace(' ', '+')
    page = 1
    num = 0
    titledict = {}
    iddict = {}
    absdict = {}
    # 更新文本框
    text1.delete(1.0, 'end')  # 清空文本框
    text1.insert('end', 'سەۋرقىلىڭ\n')
    text1.insert('end', '                          \n')
    text1.insert('end', 'ئىزدەۋاتىدۇ....\n')
    text1.see(END)
    text1.update()

    # 获取搜索信息
    url_start = 'https://pubmed.ncbi.nlm.nih.gov/?term={}&page={}{}'.format(item, page, year)
    r = requests.get(url_start)
    # 获取搜索结果数目
    try:
        reg_counts = re.compile('<span class="value">(.*?)</span>')
        counts = reg_counts.findall(r.text)
        counts = counts[0].replace(',', '')
        max_page = int(counts) // 10 + 1
        text1.delete(1.0, 'end')  # 清空文本框
        text1.insert('end', 'كەچۈرۈڭ! You got {} results：This is page {} of all {} pages.\n'.format(counts, str(page), str(max_page)))
        getpagemessage(page)
        getabstract(num)
    except:
        text1.insert(END, 'تېپىلمىدى,كەچۈرۈڭ\n')
        text1.see(END)
        text1.update()


# 默认搜索
def searchall():
    global year
    year = ''
    search_by_year(year)


# 绑定enter键
def searchall_enter(self):
    searchall()


# 最近1年
def search1year():
    global year
    year = '&filter=ds1.y_1'
    search_by_year(year)


# 最近5年
def search5year():
    global year
    year = '&filter=ds1.y_5'
    search_by_year(year)


# 最近10年
def search10year():
    global year
    year = '&filter=ds1.y_10'
    search_by_year(year)


# 翻页功能
def nextpage():
    global item, year, page, max_page, num, titledict, iddict, absdict, counts
    if page < max_page:
        page += 1
        num = 0
        if page in titledict:
            # 显示标题信息
            text1.delete(1.0, 'end')  # 清空文本框
            text1.insert('end', '本次搜索共找到{}结果：第{}页，共{}页\n'.format(counts, str(page), str(max_page)))
            for i in range(len(titledict[page])):
                text1.insert('end', titledict[page][i])
                text1.see(END)
                text1.update()
            # 显示摘要信息
            id = iddict[page][num]
            conent = absdict[id]
            text2.delete(1.0, 'end')  # 清空文本框
            text2.insert('end', conent)
            text2.see(END)
            text2.update()
        else:
            text1.delete(1.0, 'end')  # 清空文本框
            text1.insert('end', '本次搜索共找到{}结果：第{}页，共{}页\n'.format(counts, str(page), str(max_page)))
            getpagemessage(page)
            getabstract(num)
    else:
        pass


def lastpage():
    global item, year, page, max_page, num, titledict, iddict, absdict, counts
    if page > 1:
        page -= 1
        num = 0
        # 显示标题信息
        text1.delete(1.0, 'end')  # 清空文本框
        text1.insert('end', '本次搜索共找到{}结果：第{}页，共{}页\n'.format(counts, str(page), str(max_page)))
        for i in range(len(titledict[page])):
            text1.insert('end', titledict[page][i])
            text1.see(END)
            text1.update()
        # 显示摘要信息
        id = iddict[page][num]
        text2.delete(1.0, 'end')  # 清空文本框
        text2.insert('end', absdict[id])
        text2.see(END)
        text2.update()
    else:
        pass


# 翻篇功能
def nextarticle():
    global num, iddict, absdict, page, max_page
    if num < len(iddict[page]) - 2:
        num += 1
        id = iddict[page][num]
        if id in absdict:
            conent = absdict[id]
            text2.delete(1.0, 'end')  # 清空文本框
            text2.insert('end', conent)
            text2.see(END)
            text2.update()
        else:
            getabstract(num)
    else:
        if page < max_page:
            nextpage()
        else:
            pass


def lastarticle():
    global num, iddict, absdict, page, max_page
    if num > 0:
        num -= 1
        id = iddict[page][num]
        if id in absdict:
            conent = absdict[id]
            text2.delete(1.0, 'end')  # 清空文本框
            text2.insert('end', conent)
            text2.see(END)
            text2.update()
        else:
            getabstract(num)
    else:
        if page > 1:
            page -= 1
            num = 9
            text1.delete(1.0, 'end')  # 清空文本框
            text1.insert('end', '本次搜索共找到{}结果：第{}页，共{}页\n'.format(counts, str(page), str(max_page)))
            for i in range(len(titledict[page])):
                text1.insert('end', titledict[page][i])
                text1.see(END)
                text1.update()
            id = iddict[page][num]
            if id in absdict:
                conent = absdict[id]
                text2.delete(1.0, 'end')  # 清空文本框
                text2.insert('end', conent)
                text2.see(END)
                text2.update()
            else:
                getabstract(num)
        else:
            pass


# 翻译
def translate(text):
    '''
    将输入文本翻译成所需语种
    :param text:  chr, 原文
    :param toLang: chr, 译文语种
    :return: chr, 译文
    '''
    appid = '你的appid'  # 填写你的appid
    secretKey = '你的密钥'  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        text) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        textall = ''
        for r in result['trans_result']:
            textall += r['dst'] + '\n'
        return textall
    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()


def translation():
    text = text2.get(1.0, 'end')
    text = translate(text)
    text3.delete(1.0, 'end')  # 清空文本框
    text3.insert('end', text)
    text3.see(END)
    text3.update()


# 打开原文
def openarticle():
    global page, num, iddict
    id = iddict[page][num]
    url = 'https://pubmed.ncbi.nlm.nih.gov/{}/'.format(id)
    webbrowser.open(url)


# 清除
def deletetext():
    text3.delete(1.0, 'end')  # 清空文本框
    text3.see(END)
    text3.update()


# 帮助
def HelpDocumentation():
    documentation = '''PubMed检索规则与语法：
1）布尔运算符AND，OR，NOT必须大写，如：vitaminc OR zinc；
2）PubMed从左至右进行布尔运算，你可以通过加括符改变运算顺序，如： commoncold AND (vitamincORzinc)；
3）指定文献记录字段名称检索，如: dna[MH] AND crick[AU] AND 1993[DP],下面列出常用字段名称缩写：
    DP——出版日期采用YYYY/MM/DD[DP]格式，如1998/03/06[DP]。输入日期范围则用冒号连接，如1996:1998[DP]，1998/01:1998/04[DP]
    AD——第一作者机构名称、地址、资助号如LM05545/LM/NLM[AD]
    AU——作者姓名如o'brienj[AU]
    TA——期刊名称包括期刊名全称、简称、ISSN。jbiolchem[TA]或0021-9258[TA]
    LA——文献出版语言 Chinese[LA]
    MH-Mesh 主题词 neoplasms[MH]或neoplasms/dt[MH]
    PT——出版类型 review[PT]
    TW——自由词AA001794[TW]
    T1——文献标题内自由词leiomyosarcoma[TI] 
有趣的搜索：
1）通过时间和期刊字段的组合，定期查看某期刊的文章动态，如science[TA] AND 2020/05:2020/06[DP]
2）通过关键词和期刊字段的组合，查看顶级期刊上关于xxx的研究进展，如miRNA[MH] AND (science[TA] OR nature[TA] OR cell[TA])
    '''
    text1.delete(1.0, 'end')  # 清空文本框
    text1.insert('end', documentation)
    text1.see(END)
    text1.update()


# 第一部分 窗口布局
# 创建面板
root = Tk()
root.title("❀ سالام! مەن سىزنىڭ ماقالە ئىزدىگۈچى ياخشى دوستىڭىز❀ ياسىغۇچى: راشىدىن ئابدۇغېنى              ")
root.configure(bg='light blue')
root.geometry('1000x540')
root.minsize(width=600, height=400)

# 创建分区
fm1 = Frame(height=250, width=300)  # 摘要显示区
fm2 = Frame(height=350, width=300)  # 提示显示区
fm3 = Frame(height=50, width=300)  # 摘要按钮区
fm4 = Frame(height=250, width=300)  # 搜索控件区
fm5 = Frame(height=350, width=300)  # 翻译显示区
fm6 = Frame(height=50, width=300)  # 翻译按钮区

# 创建控件
# 滚动文本框
scr1 = Scrollbar(fm1)
text1 = Text(fm1, font=('微软雅黑', 12))
scr1.pack(side=RIGHT, fill=Y, anchor='center')
text1.pack(side=LEFT, fill=Y)
scr1.config(command=text1.yview)
text1.config(yscrollcommand=scr1)
scr2 = Scrollbar(fm2)
text2 = Text(fm2, font=('微软雅黑', 12))
scr2.pack(side=RIGHT, fill=Y, anchor='center')
text2.pack(side=LEFT, fill=Y)
scr2.config(command=text2.yview)
text2.config(yscrollcommand=scr2)
scr3 = Scrollbar(fm5)
text3 = Text(fm5, font=('微软雅黑', 12))
scr3.pack(side=RIGHT, fill=Y, anchor='center')
text3.pack(side=LEFT, fill=Y)
scr3.config(command=text3.yview)
text3.config(yscrollcommand=scr3)

# 摘要控制区
b1 = Button(fm3, text="ئالدىنقى ماقالە", command=lastarticle)
b2 = Button(fm3, text="كېيىنكى ماقالە", command=nextarticle)
b3 = Button(fm3, text="ئەسلى ماقالىنى ئوقۇش", command=openarticle)
b1.pack(side=LEFT, anchor='w')
b2.pack(side=LEFT, anchor='center')
b3.pack(side=LEFT, anchor='e')
# 搜索区
l1 = Label(fm4, text="ئىزدىگۈچىسى ماقالەPubMed ئۇيغۇرۇم", font=('微软雅黑', 16))
entry1 = Entry(fm4, width=25)
b4 = Button(fm4, text="ئىزدەش", command=searchall)
b5 = Button(fm4, text="بىر يىللىق", command=search1year)
b6 = Button(fm4, text="بەش يىللىق", command=search5year)
b7 = Button(fm4, text="ئون يىللىق", command=search10year)
b8 = Button(fm4, text="ئالدىنقى بەت", command=lastpage)
b9 = Button(fm4, text="كېيىنكى بەت", command=nextpage)
b10 = Button(fm4, text="ياردەم", command=HelpDocumentation)
l2 = Label(fm4, text='_________________________________')
l1.grid(row=0, columnspan=3,)
entry1.grid(row=1, column=0, columnspan=2)
entry1.bind("<Return>", searchall_enter)
b4.grid(row=1, column=2)
b5.grid(row=2, column=0)
b6.grid(row=2, column=1)
b7.grid(row=2, column=2)
b8.grid(row=3, column=0)
b9.grid(row=3, column=1)
b10.grid(row=3, column=2)
l2.grid(row=6, columnspan=3)

# 翻译控件
b11 = Button(fm6, text="تەرجىمە", command=translation)
b11.pack(side=RIGHT, anchor='center')
b12 = Button(fm6, text="ئۆچۈرۈش", command=deletetext)
b12.pack(side=LEFT, anchor='center')

# 布局分区
root.rowconfigure(0, weight=70)
root.rowconfigure(1, weight=70)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
fm1.grid(row=0, column=0)
fm2.grid(row=1, column=0)
fm3.grid(row=2, column=0)
fm4.grid(row=0, column=1)
fm5.grid(row=1, column=1)
fm6.grid(row=2, column=1)

# 显示界面
root.mainloop()