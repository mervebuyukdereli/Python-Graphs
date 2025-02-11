import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = "3d")

z = np.random.rand(12,4)
x = z*np.random.rand(12,4)*100
y = z*np.random.rand(12,4)

ax.plot_surface(x, y, z, color = "green")
plt.title("3 Boyutlu Grafik", size = 20)
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
ax.set_zlabel("Z Ekseni")
plt.show()
