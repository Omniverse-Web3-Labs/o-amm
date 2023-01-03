import solving
import math

initX = 10;
initY = 20;
initC = initX * initY;
initb = math.sqrt(initC) * 2;

def getPriceY_X(initC, x, y):
    dx = 0.0001;
    dy = y - solving.solve_symmetry_const_gradient(x + dx, initb, initC);
    print(dy / dx);

    dy_dx_expr = solving.diff_o_amm_dy_dx(initb, initC)
    return solving.price_o_amm(x, y, dy_dx_expr);

def testSwapX2Y(initC, x, y, dx):
    C= initC;
    b = math.sqrt(C) * 2;

    y_sub_dy = solving.solve_symmetry_const_gradient(x + dx, b, C);
    dy = y - y_sub_dy;
    return dy

def testSolving():
    x = 1;
    dx = 0.0001;
    y = solving.solve_symmetry_const_gradient(x, initb, initC);
    
    print(testSwapX2Y(initC, x, y, dx))

    print(getPriceY_X(initC, x, y));

testSolving();
