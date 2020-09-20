import matplotlib.pyplot as plt
from numpy import *
x=linspace(0,180,5)

#rotation 可以控制字体的方向
for i in range(size(x)):
    print(x[i])
    plt.text(i*0.2,0.5,'matplotlib',rotation=x[i])
plt.savefig('rotation.png')
plt.show()