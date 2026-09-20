#MAdhur
#coded on 10-09-26
#import 
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
import math
import sympy as sp
#raphson and function solution
def func(x):
    return math.exp(x)-2
def raph(x):
    return  (x-((math.exp(x)-2)/(math.exp(x))))
x=1;
x1=np.linspace(-3,2,1000);
y1=(np.exp(x1)-2)
plt.plot(x1,y1)
plt.grid()
for i in range (20):
    plt.plot(x,func(x),"o")
    x=raph(x)
print("RAPHSON gave",x)
#solving using sympy
X=sp.symbols("X")
wq=sp.Eq(sp.exp(X),2)
sol=sp.solve(wq,X)
plt.axvline(x=sol)
print("The solution is",sol)
#saving it
plt.savefig("raph.pdf")
subprocess.run(shlex.split("termux-open raph.pdf"))
