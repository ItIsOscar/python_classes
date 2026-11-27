import matplotlib.pyplot as plt
import numpy as np
_R_SPHERE = 10
_X_MAX = 10
_Y_MAX = 10
_Z_MAX = 10
_START_CRD = [0,0, -_Z_MAX]

X_sphere = np.linspace(-_R_SPHERE, _R_SPHERE, num=100)
Y_sphere = np.linspace(-_R_SPHERE, _R_SPHERE, num=100)
Z_sphere = _R_SPHERE**2 - (X_sphere**2 + Y_sphere**2)
print(Z_sphere)
#X_sphere, Y_sphere, Z_sphere = np.meshgrid(X_sphere, Y_sphere, Z_sphere)

X1 = np.random.random((100,100))
Y1 = np.random.random((100,100))


plt.style.use('_mpl-gallery')

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(X_sphere, Y_sphere, Z_sphere, cmap="Blues")

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()