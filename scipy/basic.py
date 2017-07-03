#%%
import numpy as np
np.mgrid[0:5, 0:5, 0:5, 0:5]

#%%
import numpy as np
a = np.r_[3,[0]*5,-1:1:40j]
print(a)

#%%
import numpy as np
np.mgrid[0:5,0:5]

#%%
from numpy import poly1d
p = poly1d([3,4,5])
print(p)
print(p*p)
print(p.integ(k=6))
print(p.deriv())
p([4, 5])

#Vectorizing functions (vectorize)
#%%
def addsubtract(a,b):
    if a > b:
        return a - b
    else:
        return a + b

import numpy as np
vec_addsub = np.vectorize(addsubtract)
print(vec_addsub([0,3,6,9],[1,3,5,7]))