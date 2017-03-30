"""
Demo of the fill function with a few features.

In addition to the basic fill plot, this demo shows a few optional features:

    * Multiple curves with a single command.
    * Setting the fill color.
    * Setting the opacity (alpha value).
"""
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x1)
y2 = np.sin(3 * x1)

plt.figure()
plt.subplot(1,2,1)
plt.title('fill_demo_feature')

plt.fill(x1, y1, 'b', x1, y2, 'r', alpha=0.3)


x3 = np.linspace(0, 1, 500)
y3 = np.sin(4 * np.pi * x3) * np.exp(-5 * x3)

plt.subplot(1,2,2)
plt.title('fill_demo')

plt.fill(x3, y3, zorder=10)
plt.grid(True, zorder=5)
plt.show()
