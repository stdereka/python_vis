import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

data = pd.read_csv("table6.csv")
x = data["x"].values
y = data["y"].values

plt.errorbar(x, y, xerr=0.04, yerr=0.005, ls="--", marker="o", color="k", fmt=None)
a = np.arange(min(x)-10, max(x)+10, 0.001)
p = np.poly1d(np.polyfit(x, y, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y, 1)))
plt.plot(a, p(a), color='k')
plt.xlim(0.7, 1.3)
plt.ylim(0.04, 0.11)

xminorLocator = MultipleLocator(0.025)
yminorLocator = MultipleLocator(0.005)
xmajorLocator = MultipleLocator(0.125)
ymajorLocator = MultipleLocator(0.025)
ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.title("Рис.5: График зависимости d(1/D)")
plt.xlabel(u"1/D, 1/мм")
plt.ylabel(u"d, мм")
plt.show()
