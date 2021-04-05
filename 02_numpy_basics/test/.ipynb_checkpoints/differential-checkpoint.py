import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1) # x axis domain
x1 = 3 # domain = x axis / range = y axis
tangent_range = np.linspace(x1-2, x1+2, 10)

def f(x):
  return x**2

def slope(x):
  return 2*x

def line(x, x1, y1):
  return slope(x1)*(x-x1) + y1
  
plt.figure() # Graph figure
plt.plot(x,f(x)) 
plt.scatter(x1, f(x1), color='purple', s=50)
plt.plot(tangent_range, line(tangent_range, x1, f(x1)), color='purple', linewidth=2)
plt.savefig('img/diff_img.png')
