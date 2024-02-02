import numpy as np
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0
b = 2

# Кількість точок для генерації
num_points = 10_000_000

# Генерація випадкових точок
random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, max(f(random_x)), num_points)

# Обчислення кількості точок, що під кривою
points_under_curve = sum(random_y <= f(random_x))

# Обчислення відношення площі під кривою до загальної площі
integral_approximation = (points_under_curve / num_points) * (b - a) * max(f(random_x))

# Обчислення результату інтегрування за допомогою scipy.integrate.quad
result, error = quad(f, a, b)

# Визначення стандардної похибки для методу Монте-Карло
standard_error = np.std(random_y) / np.sqrt(num_points)

print("Результат інтегрування, за допомогою scipy.integrate.quad:", result)

print(f"Результат інтегрування методом Монте-Карло: {integral_approximation:.4f} +/- {standard_error:.4f}")

