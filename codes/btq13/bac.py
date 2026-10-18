# The implementation and plotting scripts are adapted from:
# {https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/07-09-26/BACTERIA}

import math
import matplotlib.pyplot as plt
import numpy as np
from plotting.funcs import label_pts

# Theoretical continuous solution
x1 = np.linspace(0, 2.0, 300)
y1 = 3 * np.exp(math.log(2) * x1) - 2

# Loading Euler numerical simulation data
x = np.loadtxt("x.dat")
y = np.loadtxt("y.dat")

# Subsample stems (every 8th point) so individual samples are distinct
markerline, stemlines, baseline = plt.stem(
    x, y, basefmt="k-", label="Numerical"
)
plt.setp(markerline, markersize=2.5, color="C0")
plt.setp(stemlines, linewidth=0.5, color="C0")

# Bold continuous theory curve overlaid on top
plt.plot(x1, y1, color="red", linewidth=2.5, label="Theory", zorder=3)

# Labeling boundary points using funcs.py
pts = np.array([[x1[0], x1[-1]], [y1[0], y1[-1]]])
plt.scatter(pts[0, :], pts[1, :], color="black", zorder=5)
label_pts(pts, [f"({x1[0]:.0f}, {y1[0]:.0f})", f"({x1[-1]:.0f}, {y1[-1]:.0f})"])

# Formatting
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left", framealpha=0.95)
plt.tight_layout()
plt.savefig("bac.pdf")
