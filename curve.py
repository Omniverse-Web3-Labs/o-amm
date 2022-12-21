import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import solving

def drawCurve():
    initX = 10
    initY = 20
    D = initX + initY
    A = 10

    x_curve = np.linspace(0.5, 40, 100)
    func_curve = np.vectorize(solving.solve_curve)
    y_curve = func_curve(x_curve, D, A)

    fig, axes = plt.subplots(1, 1)

    # axes.set_facecolor(color="black")

    axes.plot(x_curve, y_curve, label="curve")

    axes.set_aspect(1)
    axes.legend(loc='upper right')
    # plt.style.use("dark_background")
    plt.show()

drawCurve()
