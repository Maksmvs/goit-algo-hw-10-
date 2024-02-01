import pulp

R = pulp.LpProblem("MaximizeProduction", pulp.LpMaximize)
Limo = pulp.LpVariable('Limo', lowBound=0, cat='Integer')  
Frut_juce = pulp.LpVariable('Frut_juce', lowBound=0, cat='Integer')

R += Limo + Frut_juce, "Total Production"

R += 2 * Limo + Frut_juce <= 100, "Води"
R += Limo <= 50, "Цукру"
R += Limo <= 30, "Лимонного соку"
R += 2 * Frut_juce <= 40, "Фруктового пюре"

R.solve()

print("Кількість 'Лимонаду':", Limo.value())
print("Кількість 'Фруктового соку':", Frut_juce.value())
