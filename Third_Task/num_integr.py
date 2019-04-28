import numpy as np

class Integral:

    def __init__ (self, a, f, num_blocks):
        self._a = a
        self._f = f
        self._num_blocks = num_blocks

    def set_function (self, f):
        self._f = f

    def set_left_border (self, a):
        self._a = float(a)

    def set_num_blocks (self, num_blocks):
        self._num_blocks = num_blocks


class IntegrateRightRect (Integral):
    def __init__ (self, a, f, num_blocks):
        Integral.__init__ (self, a, f, num_blocks)

    def __call__ (self, x):
        x = float (x)
        gridArray = np.linspace (self._a, x, self._num_blocks + 1)
        gridLength = len (gridArray)
        h = (x - self._a) / self._num_blocks
        value = 0.

        for i in range (1, gridLength):
            tCurrent = gridArray[i]
            value += self._f (tCurrent) * h

        return value


class IntegrateLeftRect (Integral):
    def __init__ (self, a, f, num_blocks):
        Integral.__init__ (self, a, f, num_blocks)

    def __call__ (self, x):
        x = float (x)
        gridArray = np.linspace (self._a, x, self._num_blocks + 1)
        gridLength = len (gridArray)
        h = (x - self._a) / self._num_blocks
        value = 0.

        for i in range (gridLength - 1):
            tCurrent = gridArray[i]
            value += self._f (tCurrent) * h

        return value


class IntegrateMidRect (Integral):
    def __init__ (self, a, f, num_blocks):
        Integral.__init__ (self, a, f, num_blocks)

    def __call__ (self, x):
        x = float (x)
        gridArray = np.linspace (self._a, x, self._num_blocks + 1)
        gridLength = len (gridArray)
        h = (x - self._a) / self._num_blocks
        value = 0.

        for i in range (gridLength - 1):
            tCurrent = gridArray[i] + (h / 2.)
            value += self._f (tCurrent) * h

        return value


class IntegrateTrapez (Integral):
    def __init__ (self, a, f, num_blocks):
        Integral.__init__ (self, a, f, num_blocks)

    def __call__ (self, x):
        x = float (x)
        gridArray = np.linspace (self._a, x, self._num_blocks + 1)
        gridLength = len (gridArray)
        h = (x - self._a) / self._num_blocks
        value = 0.

        for i in range (1, gridLength - 1):
            tCurrent = gridArray[i]
            tNext = gridArray[i + 1]
            value += 0.5 * (self._f (tCurrent) + self._f (tNext)) * h

        return value


class IntegrateSimpson (Integral):
    def __init__ (self, a, f, num_blocks):
        Integral.__init__ (self, a, f, num_blocks)

    def __call__ (self, x):
        x = float (x)
        gridArray = np.linspace (self._a, x, self._num_blocks + 1)
        gridLength = len (gridArray)
        h = (x - self._a) / self._num_blocks
        k = 0.

        for i in range (1, self._num_blocks // 2 + 1):
            t_current = gridArray[i * 2 - 1]
            k = 4 * self._f (t_current)

        for i in range (1, self._num_blocks // 2):
            t_current = gridArray[i * 2]
            k = 2 * self._f (t_current)

        return (h / 3.) * (self._f (self._a) + self._f (self._num_blocks) + k)
