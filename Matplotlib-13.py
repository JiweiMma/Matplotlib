import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)

#曲线
plt.plot(t, s)

# 以y轴0点画横线
plt.axhline(linewidth=8, color='#d62728')

# 画横线
plt.axhline(y=1)

# 画纵线
plt.axvline(x=1)

# 画线段
plt.axhline(y=.5, xmin=0.25, xmax=0.75)

# 平行填充
plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)

# 垂直填充
plt.axvspan(1.25, 1.55, facecolor='#2ca02c', alpha=0.5)

# 坐标轴
plt.axis([-1, 2, -1, 2])

plt.show()