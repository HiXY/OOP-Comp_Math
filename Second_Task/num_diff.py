class DerivativeRightDiff:
    def __init__ (self, f = 0, h = 0):
        self.__f = f
        self.__h = h

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def __call__ (self, x):
        f, h = self.__f, self.__h
        return ((f (x + h) - f (x)) / h)


class DerivativeLeftDiff (DerivativeRightDiff):
    def __init__ (self, f = 0, h = 0):
       DerivativeRightDiff.__init__ (self, f, h)

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def __call__ (self, x):
        f, h = self.__f, self.__h
        return ((f (x) - f (x - h)) / h)


class DerivativeCentrDiff (DerivativeLeftDiff):
    def __init__ (self, f = 0, h = 0):
        DerivativeLeftDiff.__init__ (self, f, h)

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def __call__ (self, x):
        f, h = self.__f, self.__h
        return ((f (x + h) - f (x - h)) / (2. * h))


class DerivativeSecAccDiff (DerivativeCentrDiff):
    def __init__ (self, f = 0, h = 0):
        DerivativeCentrDiff.__init__ (self, f, h)

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def __call__ (self, x):
        f, h = self.__f, self.__h
        return (((4./ (3. * 2. * h)) * (f (x + h) -  f (x - h))) - \
                ((1. / (3. * 4. * h)) * (f (x + (2. * h)) - f (x - (2. * h)))))


class DerivativeThirdAccDiff (DerivativeSecAccDiff):
    def __init__ (self, f = 0, h = 0):
        DerivativeSecAccDiff.__init__ (self, f, h)

    def set_function (self, f):
        self.__f = f

    def set_step (self, h):
        self.__h = h

    def __call__ (self, x):
        f, h = self.__f, self.__h
        return (((3. / (2. * 2. * h)) * (f (x + h) - f (x - h))) - \
                ((3. / (5. * 4. * h)) * (f (x + (2. * h)) - f (x - (2. * h)))) + \
                ((1. / (10. * 6. * h)) * (f (x + (3. * h)) - f (x - (3. * h)))))
