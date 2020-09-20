
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 6)
y = x * x
plt.plot(x, y, marker='o')
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
plt.show()