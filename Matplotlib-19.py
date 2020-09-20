import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(5)
#绘制三维图
ax=fig.add_subplot(1,1,1,projection='3d')
#获取X轴数据，Y轴数据
x,y=np.mgrid[-2:2:20j,-2:2:20j]
#获取Z轴的数据
z=x*np.exp(-x**2-y**2)

#绘制三维图
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_xlabel('x-name')
ax.set_ylabel('y-name')
ax.set_zlabel('z-name')

plt.show()