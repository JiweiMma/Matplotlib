import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(6)
#添加一个子图
ax=fig.add_subplot(1,1,1)
#创建矩形  （X,Y），宽，高
rect1 = plt.Rectangle((0.1,0.2),0.2,0.3,color='r')
#创建椭圆 参数：中心点，半径
circ1 = plt.Circle((0.7,0.2),0.15,color='r',alpha=0.3)
#创建一个多边形     每个顶点坐标
pgon1 = plt.Polygon([[0.45,0.45],[0.65,0.6],[0.2,0.6]])

#将形状添加到子图上
ax.add_patch(rect1)
ax.add_patch(circ1)
ax.add_patch(pgon1)

fig.canvas.draw()
plt.show()