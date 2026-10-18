import cvxpy as cp #using cvxpy to find the soln
import numpy as np
import matplotlib.pyplot as plt
from plotting.funcs import label_pts
x1=np.linspace(1,4,200) 
y1=(x1+4/x1)

#Plotting
plt.plot(x1,y1)
x=cp.Variable()
q=cp.Minimize(x+(4*cp.inv_pos(x)))
con=[x>=0]
pb=cp.Problem(q,con)
sol=pb.solve() 
print(sol) #printing soln ans using cvxpy

#Labeling minimum point using funcs.py
pts = np.array([[x.value], [sol]])
plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
label_pts(pts, [f"({x.value:.2f}, {sol:.2f})"])

plt.grid(True)
plt.savefig("/sdcard/github/fig.png")
