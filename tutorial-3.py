"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpltools import style
from mpltools import layout
import brewer2mpl

colors = brewer2mpl.get_map('Set2', 'qualitative', 3).mpl_colors
style.use('ggplot')

alpha = 0.9

figsize = layout.figaspect(scale=0.8)
fig, axes = plt.subplots(figsize=figsize)


N = 50
data1 = [np.random.rand(N), np.random.rand(N)]
data2 = [np.random.rand(N), np.random.rand(N)]
data3 = [np.random.rand(N), np.random.rand(N)]
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(data1[0], data1[1], s=area, alpha=alpha, color=colors[0])
plt.scatter(data2[0], data2[1], s=area, alpha=alpha, color=colors[1])
plt.scatter(data3[0], data3[1], s=area, alpha=alpha, color=colors[2])
plt.title('Tutorial Matplotlib')

fig.tight_layout()

plt.show()

fig.savefig('tutorial-3.png', bbox_inches='tight')
