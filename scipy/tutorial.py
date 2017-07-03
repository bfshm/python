#%%
import numpy as np
a = np.arange(15)
print(a)
print(a.ndim)
print(a.size)

b = np.arange(15).reshape(5,3)
print(b)
print(b.shape)
print(b.ndim)
print(b.size)

c = np.arange(15).reshape(5,3,1)
print(c)
print(c.shape)
print(c.ndim)
print(c.size)

#%%
from numpy import pi
import matplotlib.pyplot as plt
x = np.linspace(0, 2*pi, 100)
#print(x)
f = np.sin(x)
#print(f)
plt.plot(x, f)
#plt.plot(f)
plt.show()

#%%
import numpy as np
a = np.floor(10*np.random.random((2,2)))
print(a)
b = np.floor(10*np.random.random((2,2)))
print(b)
c = np.vstack((a, b))
print(c)
d = np.hstack((a, b))
print(d)

#%%
np.r_[1:4, 0, 4]

#%%
import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1)       # matplotlib version (plot)
plt.show()
