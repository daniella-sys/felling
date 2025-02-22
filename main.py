from sympy import symbols, Eq, solve
def solve_quadratic(a, b, c):
    x = symbols('x')
    equation = Eq(a*x**2 + b * x + c, 0)
    solutions = solve(equation, x)
    return solutions
#запускаємо
a = 1
b = 3
c = -9

roots = solve_quadratic(a, b, c)
print(f"Корені рівняння {a}x^2 + {b}x + {c} = 0: {roots}")