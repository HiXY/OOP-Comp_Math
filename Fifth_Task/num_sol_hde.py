import num_diff as nd
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

epsilon, h_const = 0.001, 0.001
figureSizeConst = (13, 6.7)

class RightSideLogisticEquation:
    def set_alpha (self, alpha):
        self._alpha = alpha

    def set_R (self, R):
        self._R = R

    def __call__ (self, u):
        return self._alpha * u * (1. - u / self._R)


class Solution (ABC):
    def __init__ (self, f, val):
        self._f = f
        self._initial_value = val

    def set_right_side_function (self, f):
        self._f = f

    def set_initial_condition (self, val):
        self._initial_value = val

    def set_grid (self, blocks, start, end):
        self._num_blocks = blocks
        self._dt = float (end - start) / float (self._num_blocks)
        self._solutions_array = np.zeros (self._num_blocks + 1)
        self._time_array = np.linspace (start, end, self._num_blocks + 1)
        self._time_start, self._time_end = start, end

    @abstractmethod
    def next_step (self, i):
        pass

    def solve (self):
        print ("Start of timestepping by %s method..." % self.__class__.__name__)
        self._solutions_array[0] = self._initial_value

        for i in range (self._num_blocks):
            self._solutions_array[i + 1] = self.next_step (i)
            if (i + 1) % 20 == 0:
                print ("Step #%d completed." % (i + 1))

        return self._solutions_array, self._time_array

    def make_plot (self):
        plt.figure (figsize = figureSizeConst)
        plt.title ('Soluted by %s method' % self.__class__.__name__)
        plt.plot (self._time_array, self._solutions_array, '-', linewidth = 4,  markersize = 10)
        plt.grid (True)
        plt.xlabel ('Time, s')
        plt.ylabel ('Population')
        plt.show ()


class EulerFirstAccuracy (Solution):
    def next_step (self, i):
        u_old, dt, f = self._solutions_array[i], self._dt, self._f
        return u_old + dt * f (u_old)


class EulerSecondAccuracy (Solution):
    def next_step (self, i):
        u_old, dt, f = self._solutions_array[i], self._dt, self._f
        u_new = u_old + dt * f (u_old)
        return u_old + dt / 2. * (f (u_old) + f (u_new))


class RungeKuttaThirdAccuracy (Solution):
    def next_step (self, i):
        u_old, dt, f = self._solutions_array[i], self._dt, self._f
        k1 = f(u_old)
        k2 = f(u_old + dt / 2. * k1)
        k3 = f(u_old - dt * k1 + dt * 2. * k2)
        return u_old + dt / 6. * (k1 + 4 * k2 + k3)


class RungeKuttaFourthAccuracy (Solution):
    def next_step (self, i):
        u_old, dt, f = self._solutions_array[i], self._dt, self._f
        k1 = f (u_old)
        k2 = f (u_old + dt / 2. * k1)
        k3 = f (u_old + dt / 2. * k2)
        k4 = f (u_old + dt * k3)
        return u_old + dt / 6. * (k1 + 2. * k2 + 2. * k3 + k4)


class TrapezSecondAccuracy (Solution):
    def next_step (self, i):
        u_old, dt, f = self._solutions_array[i], self._dt, self._f
        F = lambda g: g - dt / 2 * f (g) - u_old - dt / 2 * f (u_old)
        derivative = nd.DerivativeCentrDiff (f = F, h = h_const )
        u_init = u_old + dt * f (u_old)
        u_k = u_init
        u_k_next = u_k - F (u_k) / derivative (u_k)
        while abs (u_k - u_k_next) > epsilon:
            u_k = u_k_next
            u_k_next = u_k - F (u_k) / derivative (u_k)
        return u_k_next
