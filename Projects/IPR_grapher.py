import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

''' This project uses a modified Vogel's method to plot Inflow Performance Relationship
using matplotlib. Currently the project is accurate for measurement taken at Pb < Pwf.
Case 2 will determine the data taken at Pwf < Pb. '''





inputs = False
print("Input unknowns")
while not inputs:
    try:
        p_avg = float(input("Average reservoir pressure(psi): "))
        p_wf = float(input("Bottom hole pressure(psi): "))
        q_o = float(input("Flow rate (STB/d): "))
        p_b = float(input("Bubble point pressure(psi): "))

        if p_wf > p_avg:
            raise Exception("Bottom Hole pressure can not be higher than average reservoir pressure!")

        if p_wf > p_b:
            case = 1
        else:
            case = 2

        inputs = True
    except Exception as e:
        print(e)

def case_1():
    print("Running case 1")
    j = q_o/(p_avg-p_wf)

    p = p_avg
    y, x = [], []
    while p > p_b:
        q = j*(p_avg-p)

        y.append(p)
        x.append(q)
        p-=20

    q_b = j * (p_avg - p_b)
    x.append(q_b)
    y.append(p_b)
    p = p_b
    
    x2, y2 = [], []
    while p <= p_b and p > 0:
        q = q_b + (j*p_b/1.8)*(1 - 0.2*(p/p_b) - 0.8*(p/p_b)**2)

        y2.append(p)
        x2.append(q)

        p -= 20

    plt.plot(x, y, x2, y2)
    plt.show()

def case_2():
    #Case 2 must be completed
    print("Running case 2!")


case_1()
