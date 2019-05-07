import numpy as np
import num_diff as diff
import num_integr as integr

class Norm ():
    def __init__ (self, h = 0, n = 0, a = 0, b = 0, f = 0):
        self._h = 0.001
        self._n = 1000

    def set_left_border (self, a):
        self._a = a

    def set_right_border (self, b):
        self._b = b

    def set_function (self, f):
        self._f = f


class FirstNorm (Norm):
    def __init__ (self, a = 0, b = 0, f = 0):
        Norm.__init__ (self, a, b, f)

    def norm (self, a, b, f):
        self.set_left_border (a)
        self.set_right_border (b)
        self.set_function (f)
        arr = np.linspace (self._a, self._b, self._n)
        return np.amax (np.fabs (self._f (arr)))


class SecondNorm (Norm):
    def __init__ (self, a = 0, b = 0, f = 0):
        Norm.__init__ (self, a, b, f)

    def norm (self, a, b, f):
        self.set_left_border (a)
        self.set_right_border (b)
        self.set_function (f)
        arr = np.linspace (self._a, self._b, self._n)

        diff_func = diff.DerivativeCentrDiff ()
        diff_func.set_function (self._f)
        diff_func.set_step (self._h)

        return np.amax ((np.fabs (self._f (arr))) + np.amax (np.fabs (diff_func (arr))))


class ThirdNorm (Norm):
    def __init__ (self, a = 0, b = 0, f = 0):
        Norm.__init__ (self, a, b, f)

    def norm (self, a, b, f):
        self.set_left_border (a)
        self.set_right_border (b)
        self.set_function (f)
        arr = np.linspace (self._a, self._b, self._n)

        diff_func = diff.DerivativeCentrDiff ()
        diff_func.set_function (self._f)
        diff_func.set_step (self._h)

        sec_diff_func = diff.DerivativeCentrDiff ()
        sec_diff_func.set_function (diff_func)
        sec_diff_func.set_step (self._h)

        return np.amax (np.fabs (self._f (arr))) + np.amax (np.fabs (diff_func (arr))) + np.amax (np.fabs (sec_diff_func (arr)))


class FirstMetric (FirstNorm):
    def metric (self, a, b, f, g):
        res = lambda x: f (x) - g (x)
        first_norm = FirstNorm ()
        return first_norm.norm (a, b, res)

class SecondMetric (SecondNorm):
    def metric (self, a, b, f, g):
        res = lambda x: f (x) - g (x)
        second_norm = SecondNorm ()
        return second_norm.norm (a, b, res)

class ThirdMetric (ThirdNorm):
    def metric (self, a, b, f, g):
        res = lambda x: f (x) - g (x)
        third_norm = ThirdNorm ()
        return third_norm.norm (a, b, res)


class PreHilberSpace:
    def __call__ (self, a, b, f, g):
        res = lambda x: f (x) * g (x)
        integral = integr.IntegrateTrapez (a, res, 1000)

        #integral.set_left_border (a)
        #integral.set_num (1000)

        #integral.set_function (res)
        return integral (b)


class NormalSpace (PreHilberSpace):
    def __call__ (self, a, b, f):
        return super ().__call__(a, b, f, f) ** 0.5


class MetricSpace (NormalSpace):
    def __call__ (self, a, b, f, g):
        res = lambda x: f (x) - g (x)
        return super ().__call__ (a, b, res)
