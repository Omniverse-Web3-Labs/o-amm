from sympy import symbols, Eq, solve

# `alpha` is the quotient of the geometric mean over arithmetic mean,
# which is a way to quantify the degree of difference between x and y
def alpha(x, y):
    return (x*y) / (((x+y)/2)**2)

# This is used for reserve `y`` > reserve `x`
def solve_with_gradient(k, b, i, C):
    r = symbols('r', real=True)

    _alpha = alpha(i, r)

    eq = Eq(r - (_alpha * (k*i+b) + (1-_alpha)*C/i), 0)
    s = solve(eq)
    return s[0]
