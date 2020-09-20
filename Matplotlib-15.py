# 导入包
import matplotlib.pyplot as plt
import numpy as np
# x与y数据
x=np.linspace(0,2,500)
y1=np.sin(2*np.pi*x)
y2=1.1*np.sin(3*np.pi*x)

# 绘图
fig=plt.figure()
ax=fig.add_subplot(111)

# 绘制y1和y2，
ax.plot(x,y1,color='k',lw=1,ls='-')
ax.plot(x,y2,color='k',lw=1,ls='-')

# y1<=y2部分
ax.fill_between(x,y1,y2,where=y2>=y1,facecolor='cornflowerblue',alpha=0.7)
# y1>=y2的部分
ax.fill_between(x,y1,y2,where=y2<=y1,interpolate=False,facecolor='darkred',alpha=0.7)

ax.set_xlim(-0.4,2.3)
ax.set_ylim(-1.5,1.5)

ax.grid(ls=':',lw=1,color='gray',alpha=0.5)
plt.show()

