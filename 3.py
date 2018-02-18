import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

data = pd.read_csv("table3.csv")

x = np.array(data["nur"].values)
y = np.array(data["L"].values)

xminorLocator = MultipleLocator(0.01)
yminorLocator = MultipleLocator(0.01)
xmajorLocator = MultipleLocator(0.05)
ymajorLocator = MultipleLocator(0.05)

ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.plot(x, y, 'ks', color='k')
a = np.arange(min(x)-10, max(x)+10, 0.001)
p = np.poly1d(np.polyfit(x, y, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y, 1)))
plt.plot(a, p(a), color='k')

plt.xlabel(r"$1/\nu$, с", size="15")
plt.ylabel("$\Lambda, 10^{-3}$м", size="15")

plt.ylim(0.8, 1.5)
plt.xlim(0.5, 1)
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.show()
