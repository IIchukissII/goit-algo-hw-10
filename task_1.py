import pulp as plp

# Створення моделі
model = plp.LpProblem("MaximizeProduction", plp.LpMaximize)

# Оголошення змінних рішення
x1 = plp.LpVariable("Lemonade", lowBound=0, cat=plp.LpInteger)
x2 = plp.LpVariable("FruitJuice", lowBound=0, cat=plp.LpInteger)

# Функція максимізації
model += x1 + x2, "TotalProduction"

# Обмеження ресурсів
model += 2 * x1 + x2 <= 100, "WaterConstraint"
model += x1 <= 50, "SugarConstraint"
model += x1 <= 30, "LemonJuiceConstraint"
model += 2 * x2 <= 40, "FruitPureeConstraint"

# Вирішення задачі
model.solve()

# Виведення результатів
print(f"Status: {plp.LpStatus[model.status]}")
print(f"Lemonade units: {plp.value(x1)}")
print(f"Fruit Juice units: {plp.value(x2)}")
print(f"Total Production: {plp.value(model.objective)}")
