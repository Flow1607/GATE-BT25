import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(1,4,200)
y1=(x1+4/x1)
plt.plot(x1,y1)
x=cp.Variable()
q=cp.Minimize(x+(4*cp.inv_pos(x)))
con=[x>=0]
pb=cp.Problem(q,con)
sol=pb.solve()
print(sol)
plt.savefig("/sdcard/fig.png")
