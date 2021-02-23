# Plotting field strength in 2D

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)

xx,yy = np.meshgrid(x,y)

plt.quiver(xx,yy,xx,yy)
plt.savefig('quiver.pdf')
plt.show()

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)

# xx,yy = np.meshgrid(x,y)

# plt.pcolormesh(xx,yy,xx**2/3 + yy**2, vmax=80)
# plt.colorbar()
# plt.savefig('colormap2.pdf')
# plt.show()


# def f(x,y):
#     return np.sin(x*y)

# x = np.linspace(-np.pi, np.pi, 100)
# y = np.linspace(-np.pi, np.pi, 100)

# xx,yy = np.meshgrid(x,y)

# plt.title("Heatmap av $f(x,y) = sin(xy)$")
# plt.xlabel("One axis")
# plt.ylabel("Another axis")
# plt.pcolormesh(xx,yy,f(xx,yy), vmax=1)
# plt.colorbar()
# plt.savefig('heatmap.pdf')
# plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(xx,yy,f(xx,yy),cmap='coolwarm')
# plt.savefig('3d.pdf')
# plt.show()
