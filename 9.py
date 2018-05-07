import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

data = pd.read_csv("table9.csv")

x = data["lambda"].values
y = data["sin"].apply(lambda v: abs(v)).values
yerr = data["sinerr"].values

plt.errorbar(x, y, xerr=0, yerr=yerr, ls="--", color="g", fmt=None, capsize=5)
a = np.arange(min(x)-10, max(x)+10, 0.01)
p = np.poly1d(np.polyfit(x, y, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y, 1)))
plt.plot(a, p(a), color='k')
plt.xlim(400, 590)
plt.ylim(0.19, 0.3)

xminorLocator = MultipleLocator(5)
yminorLocator = MultipleLocator(0.00325)
xmajorLocator = MultipleLocator(25)
ymajorLocator = MultipleLocator(0.01625)
ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.xlabel(u"$\lambda$, нм")
plt.ylabel(u"$\sin{\phi}$")
plt.show()
