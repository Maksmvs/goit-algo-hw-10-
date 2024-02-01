import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def f(x):
    return x ** 2
a = 0  
b = 2  

n_points = 10000
x_rand = np.random.uniform(a, b, n_points)
y_rand = np.random.uniform(0, f(2), n_points)

points_under_curve = sum(y_rand <= f(x_rand))

total_area = (b - a) * f(2)
area_under_curve = total_area * (points_under_curve / n_points)

print("Значення інтеграла (Метод Монте-Карло):", area_under_curve)

quad_result, quad_error = quad(f, a, b)
print("Значення інтеграла (Метод quad):", quad_result)

print("Похибка методу Монте-Карло:", abs(quad_result - area_under_curve))

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

points_under_curve_indices = np.where(y_rand <= f(x_rand))
ax.scatter(x_rand[points_under_curve_indices], y_rand[points_under_curve_indices], color='blue', s=1, alpha=0.5)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
