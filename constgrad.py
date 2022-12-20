import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import solving

def draw():
    initX = 10
    initY = 20
    initC1 = initX * initY

    k = -1
    b = 2 * (initC1 ** 0.5)

    initC0 = b

    x0 = np.linspace(0, initC0, 100)
    y0 = k * x0 + b

    x1 = np.linspace(5, 30, 100)
    y1 = initC1 / x1

    x2 = np.linspace(5, 29.9, 100)
    func2 = np.vectorize(solving.solve_with_gradient)
    y2 = func2(k, b, x2, initC1)

    # y3 = np.linspace(5, 29.9, 100)
    # func3 = np.vectorize(solving.solve_with_gradient)
    # x3 = func3(k, b, y3, initC1)

    fig, axes = plt.subplots(1, 1)

    # axes.set_facecolor(color="black")

    axes.plot(x0, y0, label="x+y=C")
    axes.plot(x1, y1, label="xy=C")
    axes.plot(x2, y2, label="x->y: a(x+y)+(1-a)xy=C")
    axes.plot(y2, x2, label="y->x: a(x+y)+(1-a)xy=C")   # The same as x3, y3 because of the Symmetry
    # axes.plot(x3, y3, label="y->x: a(x+y)+(1-a)xy=C", linestyle = ':', linewidth = 3)

    axes.set_aspect(1)
    axes.legend(loc='upper right')
    # plt.style.use("dark_background")
    plt.show()

draw()