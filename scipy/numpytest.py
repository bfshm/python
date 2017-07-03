#%% np.dtype
import numpy as np
mytype = np.dtype({'name':['name','age','weight'], 'format':['s32','i','f']}, align=True)
a = np.array([('zhang',32, 75.5), ('wang', 24, 65.2)], dtype=mytype)

#%% a.flags
a=np.array([[1,2],[2,3],[2,3]])
a.flags

#%% a.T
a = [1,2,3,4,5]
print(a.T)

#%% shape
a = [0, 1, 2, 3, 4]
#a + np.arange(1,6)
a.shape
#c = a.reshape(-1,1)
#c.shape

#%% where select piecewise
import numpy as np
x = np.arange(10)
print(x)
w = np.where(x<5,9-x,x)
print(w)
s = np.select([x<2,x>6,True], [7-x,x,2*x])
print(s)
p = np.piecewise(x,[x<2,x>6, True],[7-x,x,2*x])
print(p)

#%%

#%%