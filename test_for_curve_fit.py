import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = range(30)
y = [1, 1, 1, 2, 1, 1, 1, 2, 4, 5, 8, 12, 13, 14, 12, 11, 9, 6, 5, 4, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1 ]

s = UnivariateSpline(x, y, s=5)
xs = np.linspace(0, 29, 100)
ys = s(xs)

plt.plot(x, y, 'o')
plt.plot(xs, ys)
plt.show()