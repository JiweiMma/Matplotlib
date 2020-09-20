import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)
# 网格
ax.grid(True, linestyle='-.')
# 坐标
ax.tick_params(axis='x',labelcolor='gold', labelsize='medium', width=3)
ax.tick_params(axis='y',labelcolor='b', labelsize='medium', width=2)


plt.show()