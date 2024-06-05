import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung polinom Lagrange
def lagrange_interpolator(x_vals, y_vals, x):
    total_sum = 0
    n = len(x_vals)
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if j != i:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        total_sum += term
    return total_sum

# Melakukan interpolasi untuk nilai 5 <= x <= 40
x_range = np.linspace(5, 40, 100)
y_range = np.array([lagrange_interpolator(x_points, y_points, xi) for xi in x_range])

# Plot data interpolasi
plt.plot(x_range, y_range, color='red', label='Data Interpolasi')
plt.scatter(x_points, y_points, color='green', label='Data Asli')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.box(False)
plt.grid(False)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()
