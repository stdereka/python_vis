import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def open_file(path):
    inp = open(path, 'r', encoding='utf-8')
    lines = inp.readlines()
    lines_ = []
    for i in range(len(lines)):
        if lines[i] != '\n':
            lines_.append(lines[i])
    lines = lines_
    for i in range(len(lines)):
        lines[i] = [float(x) for x in lines[i].split()]
    return lines


ar = open_file("table1")


x = []
xerr = []
y = []
yerr = []


for p in ar:
    x.append(p[0])
    xerr.append(p[1])
    y.append(p[2])
    yerr.append(p[3])


xminorLocator = MultipleLocator(0.05)
yminorLocator = MultipleLocator(0.01)
xmajorLocator = MultipleLocator(0.5)
ymajorLocator = MultipleLocator(0.1)


ax = plt.subplot()
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)


plt.plot(x, y, 'ko', color='k')
plt.grid(which='major', ls='-', lw=0.5, c='k')
plt.grid(which='minor', ls='--', lw=0.5, c='grey')


a = np.arange(min(x)-10, max(x)+10, 0.001)
p = np.poly1d(np.polyfit(x, y, 1))
plt.plot(a, p(a), color='k')

plt.xlim(0, 10)
plt.ylim(0, 1.5)
plt.title(u"Зависимость оптической плотности среды от объёма добавленного раствора", size=20)
plt.xlabel(r'$V_{р-ра\ Fe^{III}}$, мл', size=20)
plt.ylabel(r'D', size=20)


plt.show()
