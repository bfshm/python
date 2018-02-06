#%%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_excel("data.xls", sheetname='Sheet3', skiprows=4, index_col=0, usecols=4)

# log for test
print("head-------------------------------------------------------------------------")
print('length =',len(df))
print(df.head())
print("tail-------------------------------------------------------------------------")
print(df.tail())
print("shape-------------------------------------------------------------------------")
print(df.shape)
print("index-------------------------------------------------------------------------")
print(df.index)
print(df.index[0])
print("columns-------------------------------------------------------------------------")
print(df.columns)
print(df.columns[0])
print("values-------------------------------------------------------------------------")
print(df.values)
print("describe-------------------------------------------------------------------------")
print(df.describe())
print("row0-------------------------------------------------------------------------")
print(df[0:1].values)
print(len(df[0:1].values))
print("col0-------------------------------------------------------------------------")
print(df.iloc[0])
print(df.iloc[0].values)
print(len(df.iloc[0].values))

#draw pie
#调节图形大小，宽，高
plt.figure(figsize=(9,9))
#定义饼状图的标签，标签是列表
labels = df.columns#[u'第一部分',u'第二部分',u'第三部分',u'第四部分']
#每个标签占多大，会自动去算百分比
sizes = df.iloc[0].values
colors = ['red','yellow','yellowgreen','lightskyblue']
#将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0.05,0,0,0)
patches,l_text,p_text = plt.pie(sizes,explode=explode, labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
plt.title(df.index[0])

#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend() #色标
plt.show()