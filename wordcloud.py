from wordcloud import WordCloud
import PIL.Image as image

with open("D:\\2-bacdive\\bacdive-final.txt") as fp:
        text = fp.read()
        # print(text)
        # 将文本放入WordCoud容器对象中并分析
        WordCloud = WordCloud().generate(text)
        image_produce = WordCloud.to_image()
        image_produce.show()

# coding: utf-8
import codecs
import matplotlib.pyplot as plt
import jieba
    # import sys
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']

stopword = [u'。', u',', u'，', u'(', u')', u'"', u':', u';', u'、', u',', u'，', u'”', u'“', u'；', u'：', u'的', u'有',
                u'也']
word = []
counter = {}

with codecs.open('G:\\32a\\medium wordcloud.txt') as fr:
        for line in fr:
            line = line.strip()
            # print type(line)
            if len(line) == 0:
                continue
            line = jieba.cut(line, cut_all=False)
            for w in line:  # .decode('utf-8'):
                if (w in stopword) or len(w) == 1: continue
                if not w in word:
                    word.append(w)
                if not w in counter:
                    counter[w] = 0
                else:
                    counter[w] += 1

counter_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print(counter_list[:50])
# for i,j in counter_list[:50]:print i
label = list(map(lambda x: x[0], counter_list[:10]))
value = list(map(lambda y: y[1], counter_list[:10]))

plt.bar(range(len(value)), value, tick_label=label)
plt.show()