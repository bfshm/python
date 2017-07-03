#%%
import matplotlib.pyplot as plt
import numpy as np

P = 1300000000#p(2017)
b = 3.74*0.01
d = 1.23*0.01
#print(P, b, d)
x,y = [], []
for t in range(2018,2038):
    δ=P*(b-d)
    P += δ
    x.append(t)
    y.append(P)
#print(P)
print(x)
print(y)
plt.bar(x, y)
plt.show()

