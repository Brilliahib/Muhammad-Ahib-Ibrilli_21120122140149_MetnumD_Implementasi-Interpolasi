import numpy as np
import matplotlib.pyplot as plt

def calculate_divided_differences(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])

    return table

def evaluate_newton_polynomial(x, table, x0):
    n = len(x)
    result = table[0, 0]

    for i in range(1, n):
        term = table[0, i]
        for j in range(i):
            term *= (x0 - x[j])
        result += term

    return result

x_values = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_values = np.array([40, 30, 25, 40, 18, 20, 22, 15])
i
diff_table = calculate_divided_differences(x_values, y_values)

x_interp_values = np.linspace(5, 40, 100)
y_interp_values = np.array([evaluate_newton_polynomial(x_values, diff_table, x) for x in x_interp_values])

plt.plot(x_values, y_values, 'o', color='red', label='Data Asli')
plt.plot(x_interp_values, y_interp_values, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Pata (jam)')
plt.title('Interpolasi dengan Polinomial Newton')
plt.legend()
plt.box(False)
plt.grid(False)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()
