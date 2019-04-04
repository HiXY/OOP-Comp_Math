import num_diff as nd
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

figureSizeConst = (13, 6.7)

def make_plot (name, steps, errors):
    plt.figure (figsize = figureSizeConst)
    plt.title (name)
    plt.loglog (steps, errors, '-o', linewidth = 4, markersize = 10)
    plt.grid (True)
    plt.xlabel ('Step')
    plt.ylabel ('Error')
    plt.show ()

x_sym = smp.Symbol ('x')

list_of_symbolic_functions = [smp.sin (x_sym * x_sym), smp.cos (smp.sin (x_sym)), \
        smp.exp (smp.sin (smp.cos (x_sym))), smp.log (x_sym + 3), smp.sqrt (x_sym + 3)]
list_of_functions = [smp.lambdify (x_sym, f) for f in list_of_symbolic_functions]

h0 = 1
list_of_numerical_derivatives = []

for f in list_of_functions:
    list_of_numerical_derivatives.append (nd.DerivativeCentrDiff ())
    list_of_numerical_derivatives[-1].set_function (f)
    list_of_numerical_derivatives[-1].set_step (h0)

list_of_analytical_derivatives = [smp.lambdify (x_sym, smp.diff (f, x_sym)) \
        for f in list_of_symbolic_functions]

x0 = 5
list_of_steps = [2**(-(n - 1)) for n in range(1, 21)]
functions_name = ["sin (x^2)","cos (sin (x))", "exp (sin (cos (x)))", "ln (x + 3)", "sqtr (x + 3)"]

for function, analytical_derivative, functions_name in zip (list_of_functions, list_of_analytical_derivatives, functions_name):

    numerical_derivative = nd.DerivativeCentrDiff()
    numerical_derivative.set_function (function)

    numerical_derivative.set_step (np.array (list_of_steps))

    list_of_errors = np.fabs (numerical_derivative (x0) - analytical_derivative (x0))

    make_plot (functions_name, list_of_steps, list_of_errors)
