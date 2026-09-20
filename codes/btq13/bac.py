import math
import matplotlib.pyplot as plt
import numpy as np
x1=np.linspace(0,0.2,20)
y1=3*np.exp(math.log(2)*x1)-2
x=np.loadtxt("x.dat")
y=np.loadtxt("y.dat")
plt.plot(x1,y1,color='r')
plt.stem(x,y)
plt.savefig("bac.png")
