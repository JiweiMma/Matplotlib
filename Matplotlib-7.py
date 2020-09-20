from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
t = "啦啦啦"
plt.text(4, 1, t,FontProperties=font,ha='left', rotation=15, wrap=True)
plt.text(6, 5, t,FontProperties=font,ha='left', rotation=15, wrap=True)
plt.text(5, 5, t,FontProperties=font, ha='right', rotation=-15, wrap=True)
plt.text(5, 10, t,FontProperties=font, fontsize=18, style='oblique', ha='center',va='top',wrap=True)
plt.text(3, 4, t,FontProperties=font, family='serif', style='italic', ha='right', wrap=True)
plt.text(-1, 0, t,FontProperties=font, ha='left', rotation=-15, wrap=True)
plt.show()