import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy import symbols, Eq, solve

def fn_x_add_y(x, C):
    return C - x

def fn_x_plus_y(x, C):
    return C / x

def fn_squared(x, C):
    y = symbols('y', real=True)
    eq = Eq(x**(2/3)+y**(2/3), C)
    s = solve(eq)
    return s[0]

def fn_x_y_complex(x, C):
    y = symbols('y', real = True)
    alpha = 4 * x * y / (x+y) ** 2
    eq1 = Eq((x+y)*alpha + (1 - alpha) * x * y, C)
    s = solve(eq1)
    # for ele in s:
    #     fv = ele.evalf()
    #     if fv > 0:
    #         return fv
    return s[0]


def draw():
    initX = 10
    initY = 20
    initC0 = initX + initY
    initC1 = initX * initY
    alpha = initX * initY * 4 / (initX + initY) ** 2
    print(alpha)
    initC2 = alpha * initC0 + (1- alpha) * initC1

    x0 = np.linspace(0, 30, 100)
    y0 = fn_x_add_y(x0, initC0)

    x1 = np.linspace(5, 40, 100)
    y1 = fn_x_plus_y(x1, initC1)

    # x2 = np.linspace(1, 15, 100)
    # func = np.vectorize(fn_x_y_complex)
    # y2 = func(x2, initC2)

    x3 = np.linspace(0, 29.9, 100)
    func3 = np.vectorize(fn_squared)
    y3 = func3(x3, initC0**2)

    fig, axes = plt.subplots(1, 1)

    # axes.set_facecolor(color="black")

    # axes.plot(x0, y0, label="x+y=C")
    # axes.plot(x1, y1, label="xy=C")
    # axes.plot(x2, y2, label="a(x+y)+(1-a)xy=C")
    axes.plot(x3, y3, label="(x+y)**2=C")

    # axes.set_aspect(1)
    axes.legend(loc='upper right')
    # plt.style.use("dark_background")
    plt.show()


def test_solve():
    x0 = 2
    y0 = 10
    C = x0 + y0 + x0 * y0

    x = np.linspace(0., 3, 10)
    func = np.vectorize(fn_x_y_complex)
    y = func(x, C)
    print(y)


def fn_calc_combinationY(k, b, x, C):
    y = symbols('y', real=True)
    alpha = 4 * x * y / (x+y) ** 2
    eq = Eq(y - (alpha * (k*x+b) + (1-alpha)*C/x), 0)
    s = solve(eq)
    return s[0]
    # return (alpha * (k*x+b) + (1-alpha)*C/x)


def fn_calc_combinationX(k1, b1, y, C):
    x = symbols('x', real=True)
    alpha = 4 * x * y / (x+y) ** 2
    eq = Eq(x - (alpha * (k1*y+b1) + (1-alpha)*C/y), 0)
    s = solve(eq)
    return s[0]
    # return (alpha * (k1*y+b1) + (1-alpha)*C/y)


def fn_calc_combinationY_fix(k, b, alpha, x, C):
    y = alpha * (k*x+b) + (1-alpha)*C/x
    return y


def fn_calc_variation(k0, b0, k1, b1, x):
    y = symbols('y', real=True)
    eq = Eq(k0*(x**2) + b0*x - (k1*(y**2)+b1*y), 0)
    s = solve(eq)
    return s[0]


def draw2():
    initX = 10
    initY = 20
    initC0 = initX + initY
    initC1 = initX * initY
    k = -initC1 / (initX**2)
    b = initY - k * initX

    x0 = np.linspace(0, initC0, 100)
    y0 = k * x0 + b

    x1 = np.linspace(2.5, 30, 100)
    y1 = fn_x_plus_y(x1, initC1)

    x2 = np.linspace(2.5, 29.9, 100)
    func2 = np.vectorize(fn_calc_combinationY)
    y2 = func2(k, b, x2, initC1)

    # x3 = np.linspace(1, 30, 100)
    # alpha = 4*initX*initY/((initX + initY)**2)
    # y3 = fn_calc_combinationY_fix(k, b, alpha, x3, initC1)

    # x4 = np.linspace(2.5, 25, 100)
    k1 = -initC1 / (initY**2)
    b1 = initX - k1 * initY
    # print(k1, b1)
    # func4 = np.vectorize(fn_calc_variation)
    # y4 = func4(k, b, k1, b1, x4)

    y5 = np.linspace(2.5, 29.9, 100)
    func5 = np.vectorize(fn_calc_combinationX)
    x5 = func5(k1, b1, y5, initC1)

    fig, axes = plt.subplots(1, 1)

    # axes.set_facecolor(color="black")

    axes.plot(x0, y0, label="x+y=C")
    axes.plot(x1, y1, label="xy=C")
    axes.plot(x2, y2, label="Derive from X: a(x+y)+(1-a)xy=C")
    # axes.plot(x3, y3, label="Fix: a(x+y)+(1-a)xy=C")
    # axes.plot(x4, y4, label="Variation")
    axes.plot(x5, y5, label="Derive from Y: a(x+y)+(1-a)xy=C")

    axes.set_aspect(1)
    axes.legend(loc='upper right')
    # plt.style.use("dark_background")
    plt.show()


draw2()
# test_solve()
