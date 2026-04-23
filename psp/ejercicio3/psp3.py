import math

class SimpsonInverso:
    def __init__(self, xi, dof):
        self.xi = xi
        self.dof = dof

        self.x = 0
        self.num_seg = 10
        self.E = 0.00001

    def f(self, x):
        num = math.gamma((self.dof + 1) / 2)
        den = math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2)
        return (num / den) * (1 + (x**2 / self.dof)) ** (-(self.dof + 1) / 2)

    def integrar(self):
        w = (self.x - self.xi) / self.num_seg

        suma = self.f(self.xi) + self.f(self.x)

        for i in range(1, self.num_seg, 2):
            suma += 4 * self.f(self.xi + i * w)

        for i in range(2, self.num_seg - 1, 2):
            suma += 2 * self.f(self.xi + i * w)

        return (w / 3) * suma

    def calcular_p(self):
        p_old = 0

        while True:
            p = self.integrar()
            error = abs(p - p_old)

            if error < self.E:
                return p

            p_old = p
            self.num_seg *= 2

    def encontrar_x(self, p_objetivo):
        x = 0.5
        d = 0.5

        error_anterior = 1

        while True:
            self.x = x
            p_calc = self.calcular_p()

            error = p_objetivo - p_calc

            if abs(error) < self.E:
                return x

            if error * error_anterior < 0:
                d = d / 2

            if p_calc < p_objetivo:
                x = x + d
            else:
                x = x - d

            error_anterior = error