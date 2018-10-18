import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
for i in range(-10,11):
    plt.plot([-10, 10], [i,i], 'k-')
    plt.plot( [i,i], [-10, 10], 'k-')
plt.plot([-10,10], [0,0], 'k-', linewidth=3.0)
plt.plot([0,0], [-10,10], 'k-', linewidth=3.0)
plt.xlim((-10, 10))
plt.ylim((-10, 10))
plt.show()
