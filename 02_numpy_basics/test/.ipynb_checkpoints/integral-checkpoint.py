import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 

def f(x):
  return x**2

min_limit, max_limit = -3, 3
x = np.linspace(-5, 5)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=2) 
ax.set_ylim(bottom=0)

ix = np.linspace(min_limit, max_limit)
iy = f(ix)
verts = [(min_limit, 0), *zip(ix, iy), (max_limit, 0)] # Vertices to colorize
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_xticks((min_limit, max_limit))
ax.set_yticks((f(min_limit), f(max_limit)))

plt.savefig('img/integral_img.png')
