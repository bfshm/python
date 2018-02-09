#ref:https://matplotlib.org/examples/pylab_examples/barchart_demo.html
#Sheet2
#%%
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
#from matplotlib.widgets import TextBox
import time

# load excel
df = pd.read_excel("data.xls", sheetname='Sheet2', skiprows=4, index_col=0, usecols=[0,11,12,13,14])
df = df.dropna() # remove Unnamed
cnt=len(df)

# draw the first graph
fig = plt.figure('x', figsize=(9,9))
subplot = fig.add_subplot(111)

#pillar
city = list(df.index[0:cnt])
men = df.values[:,0][0:cnt] + df.values[:,2][0:cnt]
std_men = men#(2, 3, 4, 1, 2)
women = df.values[:,1][0:cnt] + df.values[:,3][0:cnt]
std_women = women#(3, 5, 2, 3, 3)
people = men + women
print(people)

cityer = []
mener = []
womener = []
for i in range(0, cnt):
    if people[i] > 1000000:
        mener.append(men[i])
        womener.append(women[i])
        cityer.append(city[i])

std_men = mener#(2, 3, 4, 1, 2)
std_women = womener#(3, 5, 2, 3, 3)
# log for test
# print("男-------------------------------------------------------------------------")
# print(mener)
# print("女-------------------------------------------------------------------------")
# print(womener)
# print("city-------------------------------------------------------------------------")
# print(cityer)

index = np.arange(len(mener))
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = subplot.bar(index, mener, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Men')

rects2 = subplot.bar(index + bar_width, womener, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=std_women,
                 error_kw=error_config,
                 label='Women')

plt.xlabel('城市')
plt.ylabel('人数')
subplot.title.set_text('各城市20-29岁男女数量对比')
plt.xticks(index + bar_width / 2, cityer)
subplot.legend()

plt.show()
