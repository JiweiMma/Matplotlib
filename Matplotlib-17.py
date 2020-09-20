import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(2)
#极坐标的子图
ax1 = fig.add_subplot(1,2,1,polar=True)
theta=np.arange(0,2*np.pi,0.02)

ax1.plot(theta,2*np.ones_like(theta),lw=2)
ax1.plot(theta,theta/6,linestyle='--',lw=2)

ax2 = fig.add_subplot(1,2,2,polar=True)
ax2.plot(theta,np.cos(5*theta),linestyle='--',lw=2)
ax2.plot(theta,2*np.cos(4*theta),lw=2)

#轴线刻度和显示位置
ax2.set_rgrids(np.arange(0.2,2,0.2),angle=45)
#角度网格轴
ax2.set_thetagrids([0,45,90])

plt.show()