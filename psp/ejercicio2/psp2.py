import math

class Simpson:
    def __init__(self, xi, x, dof):
        self.xi = xi
        self.x = x
        self.dof = dof

        self.num_seg = 10  # debe ser par
        self.E = 0.00001

    def f(self, x):
        num = math.gamma((self.dof + 1) / 2)
        den = math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2)
        return (num / den) * (1 + (x**2 / self.dof)) ** (-(self.dof + 1) / 2)

    def integrar(self):
        w = (self.x - self.xi) / self.num_seg

        suma = self.f(self.xi) + self.f(self.x)

        # impares (4)
        for i in range(1, self.num_seg, 2):
            suma += 4 * self.f(self.xi + i * w)

        # pares (2)
        for i in range(2, self.num_seg - 1, 2):
            suma += 2 * self.f(self.xi + i * w)

        return (w / 3) * suma, w

    def calcular(self):
        p_old = 0

        while True:
            p, w = self.integrar()
            error = abs(p - p_old)

            if error < self.E:
                return p, w, self.num_seg

            p_old = p
            self.num_seg *= 2