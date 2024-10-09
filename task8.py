import numpy as np
import matplotlib.pyplot as plt

sin_wave = np.load('task7_sin.npy')
cos_wave = np.load('task7_cos.npy')

x = np.linspace(0, 10, 101)

plt.plot(x, sin_wave, label="sin(x)")
plt.plot(x, cos_wave, label="cos(x)")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
