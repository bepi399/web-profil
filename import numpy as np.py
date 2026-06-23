import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)
y_actual = np.sin(t)
noise = np.random.normal(0, 0.2, len(t))
y_noisy = y_actual + noise

mse = np.mean((y_actual - y_noisy)**2)

plt.figure(figsize=(8, 5))
plt.plot(t, y_actual, label='DATA ACTUAL')
plt.plot(t, y_noisy, label='DATA NOISE', alpha=0.6)
plt.xlabel("WAKTU")
plt.ylabel("HASIL OUTPUT")
plt.legend()
plt.grid(True)
plt.show()

print("MSE =", round(mse, 4))