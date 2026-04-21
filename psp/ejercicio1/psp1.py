import math

class PSP1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

        self.sumx = 0
        self.sumy = 0
        self.sumxy = 0
        self.sumx2 = 0
        self.sumy2 = 0

        self.xavg = 0
        self.yavg = 0

        self.B0 = 0
        self.B1 = 0
        self.r = 0
        self.r2 = 0

    def procesar(self):
        for i in range(self.n):
            self.sumx += self.x[i]
            self.sumy += self.y[i]
            self.sumxy += self.x[i] * self.y[i]
            self.sumx2 += self.x[i] ** 2
            self.sumy2 += self.y[i] ** 2

        self.xavg = self.sumx / self.n
        self.yavg = self.sumy / self.n

    def calcular_b1(self):
        num = self.sumxy - (self.n * self.xavg * self.yavg)
        den = self.sumx2 - (self.n * self.xavg ** 2)

        if den == 0:
            raise Exception("Error en B1 (división por cero)")

        self.B1 = num / den

    def calcular_b0(self):
        self.B0 = self.yavg - (self.B1 * self.xavg)

    def calcular_r(self):
        num = (self.n * self.sumxy) - (self.sumx * self.sumy)
        den = math.sqrt(
            (self.n * self.sumx2 - self.sumx ** 2) *
            (self.n * self.sumy2 - self.sumy ** 2)
        )

        if den == 0:
            raise Exception("Error en r (división por cero)")

        self.r = num / den

    def calcular_r2(self):
        self.r2 = self.r ** 2

    def calcular_todo(self):
        self.procesar()
        self.calcular_b1()
        self.calcular_b0()
        self.calcular_r()
        self.calcular_r2()

    def predecir(self, xk):
        return self.B0 + self.B1 * xk