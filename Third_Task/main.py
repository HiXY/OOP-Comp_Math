import matplotlib.pyplot as plt
import numpy as np
import sympy as smp
from scipy import integrate
import num_integr as ni

figure_size_const = (13, 6.7)
a = 0
x0 = 2

def make_plot (name, steps, errors):
    plt.figure (figsize = figure_size_const)
    plt.title (name)
    plt.loglog (steps, errors, '-o', linewidth = 2, markersize = 4)
    plt.grid (True)
    plt.xlabel ('Number of Blocks')
    plt.ylabel ('Error')
    plt.show ()

x_sym = smp.Symbol ('x')

list_of_symbolic_functions = [5 / (2 + 3 * x_sym * x_sym), 2 / (5 + smp.cos (x_sym)),
       (3 + 4 * x_sym * x_sym)**1/3, smp.exp (-x_sym * x_sym) * 2 / (np.pi**(1/2)),
       smp.log (x_sym + 2) / (x_sym + 2)]

functions = [smp.lambdify(x_sym, f) for f in list_of_symbolic_functions]

list_of_analytical_integrals = [smp.lambdify (x_sym, smp.integrate (f, x_sym))(x0) for f in list_of_symbolic_functions]


number_of_blocks = [2**(n + 1) for n in range(15)]

list_of_function_names = ["5 / (2 + 3 * x^2)","2 / (5 + cos (x))", "(3 + 4 * x^2)^(1/3)",
                  "2 / sqrt (pi) * exp (-x^2)", "ln (x + 2) / (x + 2)"]

list_of_integrals = [ni.IntegrateRightRect, ni.IntegrateLeftRect, ni.IntegrateMidRect, ni.IntegrateTrapez, ni.IntegrateSimpson]

for i, function in enumerate (functions):
    for Constr in list_of_integrals:
        list_of_errors = list ()
        for blocks in number_of_blocks:
            numerical_integral = Constr (a = a, f = function, num_blocks = blocks)
            list_of_errors.append (abs (numerical_integral (x0) - list_of_analytical_integrals[i]))
        make_plot (list_of_function_names[i], number_of_blocks, list_of_errors)
