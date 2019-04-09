class Derivative:
    def __init__ (self, f = 0, h = 0):
        self.__f = f
        self.__h = h

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def get_function (self):
        return self.__f

    def get_step (self):
        return self.__h


class DerivativeRightDiff (Derivative):
    def __init__ (self, f = 0, h = 0):
        Derivative.__init__ (self, f, h)

    def __call__ (self, x):
        f, h = self.get_function (), self.get_step ()
        return ((f (x + h) - f (x)) / h)


class DerivativeLeftDiff (Derivative):
    def __init__ (self, f = 0, h = 0):
       Derivative.__init__ (self, f, h)

    def __call__ (self, x):
        f, h = self.get_function (), self.get_step ()
        return ((f (x) - f (x - h)) / h)


class DerivativeCentrDiff (Derivative):
    def __init__ (self, f = 0, h = 0):
        Derivative.__init__ (self, f, h)

    def __call__ (self, x):
        f, h = self.get_function (),self.get_step ()
        return ((f (x + h) - f (x - h)) / (2. * h))


class DerivativeSecAccDiff (Derivative):
    def __init__ (self, f = 0, h = 0):
        Derivative.__init__ (self, f, h)

    def __call__ (self, x):
        f, h = self.get_function (), self.get_step ()
        return (((4./ (3. * 2. * h)) * (f (x + h) -  f (x - h))) - \
                ((1. / (3. * 4. * h)) * (f (x + (2. * h)) - f (x - (2. * h)))))


class DerivativeThirdAccDiff (Derivative):
    def __init__ (self, f = 0, h = 0):
        Derivative.__init__ (self, f, h)

    def __call__ (self, x):
        f, h = self.get_function (), self.get_step ()
        return (((3. / (2. * 2. * h)) * (f (x + h) - f (x - h))) - \
                ((3. / (5. * 4. * h)) * (f (x + (2. * h)) - f (x - (2. * h)))) + \
                ((1. / (10. * 6. * h)) * (f (x + (3. * h)) - f (x - (3. * h)))))
