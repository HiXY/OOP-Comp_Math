import sympy as smp
import func_spaces as fc

a = 0
b = 2
x_sym = smp.Symbol ('x')

list_of_symbolic_functions = [ 5 / ( 2 + (3 * x_sym) ** 2), 2 / ( 5 + smp.cos (x_sym)),
    (3 + (4 * x_sym) ** 2) ** (1 / 3), (2 / smp.sqrt (smp.pi)) * smp.exp (-x_sym ** 2)]

list_of_function_names = ["5 / ( 2 + (3 * x) ** 2)", "2 / ( 5 + cos (x))",
    "(3 + (4 * x) ** 2) ** (1 / 3)", "(2 / sqrt (pi)) * exp (-x ** 2)"]

functions = list (map (lambda f: smp.lambdify (x_sym, f, 'numpy'), list_of_symbolic_functions))

norms = [fc.FirstNorm (), fc.SecondNorm (), fc.ThirdNorm ()]
metrics = [fc.FirstMetric (), fc.SecondMetric (), fc.ThirdMetric ()]

for count, n in enumerate (norms):
    print ("Norm", count + 1)
    for k, f in enumerate (functions):
        print ("For function", list_of_function_names[k],"is", n.norm (a, b, f))

for count, metr in enumerate (metrics):
    print("Metric", count + 1)
    for i in range (len (functions)):
        for j in range (i):
            print ("Functions", list_of_function_names[i], "and", list_of_function_names[j], ":",
                  metr.metric (a, b, functions[i], functions[j]))

pre_hilbert = fc.PreHilberSpace ()
normal_space = fc.NormalSpace ()

print ("Scalar compositions")
for i in range (len (functions)):
    for j in range (i):
        print ("For functions", list_of_function_names[i], "and", list_of_function_names[j], "is",
              pre_hilbert (a, b, functions[i], functions[j]))

print ("Cosines")
for i in range (len (functions)):
    for j in range (i):
        print ("For functions", list_of_function_names[i], "and", list_of_function_names[j], "is",
        pre_hilbert (a, b, functions[i], functions[j]) / (normal_space (a, b, functions[i])\
        * normal_space(a, b, functions[j])))
