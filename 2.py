import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

data = pd.read_csv("table2.csv")

x = np.array(data["m"].values)
y1 = np.array(data["a"].values)
y2 = np.array(data["b"].values)
y3 = np.array(data["c"].values)

xminorLocator = MultipleLocator(1)
yminorLocator = MultipleLocator(5)
xmajorLocator = MultipleLocator(2)
ymajorLocator = MultipleLocator(25)

ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.plot(x, y1, 'ks', color='k', label=r"$\nu$ = 1.006 Мгц")
plt.plot(x, y2, 'ko', color='k', label=r"$\nu$ = 1.132 Мгц")
plt.plot(x, y3, 'k^', color='k', label=r"$\nu$ = 1.256 Мгц")

a = np.arange(min(x)-10, max(x)+10, 0.001)
p = np.poly1d(np.polyfit(x, y1, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y1, 1)))
plt.plot(a, p(a), color='k')
p = np.poly1d(np.polyfit(x, y2, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y2, 1)))
plt.plot(a, p(a), color='k')
p = np.poly1d(np.polyfit(x, y3, 1))
print('Уравнение', np.poly1d(np.polyfit(x, y3, 1)))
plt.plot(a, p(a), color='k')

plt.xlim(-3, 3)
plt.ylim(0, 180)
plt.xlabel("m", size="15")
plt.ylabel("Y, дел", size="15")
plt.title("Зависимость Y(m)", size="15")

plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')
plt.legend()
plt.show()
