import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

data = pd.read_csv("table5.csv")
i = data["I"].values
x = data["x"].values

plt.plot(x, i, ls="--", marker="s", color="b")
xminorLocator = MultipleLocator(5)
yminorLocator = MultipleLocator(1)
xmajorLocator = MultipleLocator(25)
ymajorLocator = MultipleLocator(5)
ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.title("Рисунок 5")
plt.xlabel(u"x, дел")
plt.ylabel(u"I, $\mu$м")
plt.show()
