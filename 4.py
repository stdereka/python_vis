import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

data = pd.read_csv("table4.csv")

xT = data["LT_um"].values
xR = data["LR_um"].values
T = data["T"].values
R = data["R"].values
lnT = data["lnT"].values

plt.subplot(1, 2, 1)
plt.plot(xT, T, ls="--", marker="o", color="b", label=u"Прошедшая волна")
plt.plot(xR, R, ls="--", marker="s", color="r", label=u"Отражённая волна")
plt.grid(True)
plt.legend()
plt.xlabel(u"l, $\mu$м")
plt.ylabel(u"T, R")
plt.title(u"Рисунок 3")

plt.subplot(1, 2, 2)
plt.plot(xT, lnT, "bs")
a = np.arange(min(xT)-30, max(xT)+30, 0.01)
p = np.poly1d(np.polyfit(xT, lnT, 1))
print('Уравнение', np.poly1d(np.polyfit(T, lnT, 1)))
plt.plot(a, p(a), color='k')
plt.xlim(450, 750)
plt.ylim(-1, 0.2)
plt.title(u"Рисунок 4")
xminorLocator = MultipleLocator(10)
yminorLocator = MultipleLocator(0.01)
xmajorLocator = MultipleLocator(50)
ymajorLocator = MultipleLocator(0.1)
ax = plt.subplot(1, 2, 2)
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.xlabel("x, $\mu$")
plt.ylabel(u"lnT")

plt.show()
