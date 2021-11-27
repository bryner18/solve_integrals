import matplotlib
from sympy.utilities.lambdify import lambdify
from sympy import *
from numpy import *
from scipy.integrate import *
import math
import scipy
from scipy import integrate
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import warnings
warnings.filterwarnings("ignore")

matplotlib.rcParams["toolbar"] = "None"


def integrate_with_graph():
    def g(x):
        func = eval(parse)
        return func

    print("Ingresa la funcion que quieres ver graficada e integrada")
    integral = input()
    parse = integral.replace("^", "**")
    l_inferior = float(input("Limite inferior -> "))
    l_superior = float(input("Limite superior -> "))

    if(("1/x" in integral or integral == "x^-1") and (l_inferior <= 0 or l_superior <= l_inferior+1)):
        return("Esta integral es divergente. No puede ser procesada (por ahora).")
    x = np.linspace(int(floor(l_inferior))-8, int(ceil(l_superior))+8, 20000)

    if("ln" in integral or "log" in integral):
        x = np.linspace(int(floor(l_inferior))+1,
                        int(ceil(l_superior))+8, 20000)

    y = [g(a) for a in x]
    fig, ax = plt.subplots()

    font1 = {'family': 'gidole', 'color': 'black', 'size': 15}
    font2 = {'family': 'gidole', 'color': 'darkred', 'size': 15}

    plt.grid()
    plt.plot(x, y, color='orange')
    plt.title("""Grafica de una Integral Definida - Grupo 6
Integral a graficar: """ + integral, loc="left", fontdict=font1)

    ix = np.linspace(l_inferior, l_superior)
    iy = [g(i) for i in ix]
    verts = [(l_inferior, 0)] + list(zip(ix, iy)) + [(l_superior, 0)]
    poly = Polygon(verts, facecolor='cyan')
    ax.add_patch(poly)

    ab, bc = quad(g, l_inferior, l_superior)
    plt.xlabel("Resultado de la integracion: " + str(ab), fontdict=font2)
    plt.show()


if __name__ == "__main__":
    integrate_with_graph()
