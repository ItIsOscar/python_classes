import matplotlib.pyplot as plt
import numpy as np
import vika
_R_SPHERE = 10
plt.style.use('_mpl  -gallery')
O_TREE mktree()
DOUBLE checkTree(V_Tree tree)

# Make data
X_sphere = np.linspace(-_R_SPHERE, _R_SPHERE, num=100)
Y_sphere = np.linspace(-_R_SPHERE, _R_SPHERE, num=100)

X_sphere, Y_sphere = np.meshgrid(X_sphere, Y_sphere)

Z_sphere = np.sqrt(_R_SPHERE - (-X_sphere**2 + Y_sphere**2))
Z_sphere1 = -Z_sphere
# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X_sphere, Y_sphere, Z_sphere)
ax.plot_surface(X_sphere, Y_sphere, Z_sphere1)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()