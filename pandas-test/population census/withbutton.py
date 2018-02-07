#%%
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import time


def draw_pie(subplot, title, labels, datas):
    colors = ['red','yellowgreen','lightskyblue']
    #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0.05,0,0)

    # draw pie
    patches,l_text,p_text = subplot.pie(datas,explode=explode, labels=labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                    startangle = 90,pctdistance = 0.6)
    subplot.title.set_text(title)

    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    subplot.axis('equal')
    subplot.legend() #色标    
    

class toolbar(object):
    cur = 0

    def next(self, event):
        print('next:' + str(self.cur))
        self.cur += 1
        datas = df.iloc[self.cur].values # datas   
        subplot.clear()
        draw_pie(subplot, df.index[self.cur], labels, datas)
        fig.canvas.draw()

    def prev(self, event):
        print('preview:' + str(self.cur))
        self.cur -= 1
        datas = df.iloc[self.cur].values # datas
        subplot.clear()
        draw_pie(subplot, df.index[self.cur], labels, datas)
        fig.canvas.draw()


# load excel
df = pd.read_excel("data.xls", sheetname='Sheet3', skiprows=4, index_col=0, usecols=[0,1,2,3])
df = df.dropna() # remove Unnamed
print(df.head())

# draw the first graph
fig = plt.figure('btn', figsize=(9,9))
subplot = fig.add_subplot(111)
title = df.index[0]
labels = df.columns #定义饼状图的标签，标签是列表#[u'第一部分',u'第二部分',u'第三部分',u'第四部分']
datas = df.iloc[0].values # datas
draw_pie(subplot, title, labels, datas)

# init next and preview button
bar = toolbar()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bprev = Button(axprev, 'Previous')    
bnext.on_clicked(bar.next)
bprev.on_clicked(bar.prev)

plt.show()
