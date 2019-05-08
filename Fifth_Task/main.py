import num_sol_hde as nsh

alpha = 0.2
R = 1.
start_time, end_time, blocks_q = 0, 40, 200
u_init = 0.1

solution = nsh.RightSideLogisticEquation ()
solution.set_alpha (alpha)
solution.set_R(R)
list_of_methods = [nsh.EulerFirstAccuracy, nsh.EulerSecondAccuracy, nsh.RungeKuttaThirdAccuracy,
    nsh.RungeKuttaThirdAccuracy, nsh.TrapezSecondAccuracy]

for method in list_of_methods:
    method = method (f = solution, val = u_init)
    method.set_grid (blocks = blocks_q, start = start_time, end = end_time)
    method.solve ()
    method.make_plot ()
