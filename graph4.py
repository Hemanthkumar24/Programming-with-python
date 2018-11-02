import matplotlib.pyplot as plt
import numpy as np
x, y, z = np.loadtxt('graph.csv',delimiter=',', unpack=True)
plt.plot(x,y,z)
plt.show()