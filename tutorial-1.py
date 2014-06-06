"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpltools import layout

figsize = layout.figaspect(scale=0.8)
fig, axes = plt.subplots(figsize=figsize)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, alpha=0.5)
plt.title('Tutorial Matplotlib')
plt.show()

fig.savefig('tutorial-1.png', bbox_inches='tight')
