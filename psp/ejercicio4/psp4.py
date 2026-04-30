import math

class PSP4:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def promedio(self, lista):
        return sum(lista) / len(lista)

    def calcular(self, xk, p):

        n = self.n
        x = self.x
        y = self.y

        x_avg = self.promedio(x)
        y_avg = self.promedio(y)

        sum_xy = sum((x[i] - x_avg)*(y[i] - y_avg) for i in range(n))
        sum_x2 = sum((x[i] - x_avg)**2 for i in range(n))
        sum_y2 = sum((y[i] - y_avg)**2 for i in range(n))

        
        r = sum_xy / math.sqrt(sum_x2 * sum_y2)

        
        r2 = r**2

        
        b1 = sum_xy / sum_x2
        b0 = y_avg - b1 * x_avg

        
        yk = b0 + b1 * xk

        
        sigma = math.sqrt(
            sum((y[i] - b0 - b1 * x[i])**2 for i in range(n)) / (n - 2)
        )

        t = self.t_student(p, n - 2)

    
        rango = t * sigma * math.sqrt(
            1 + 1/n + ((xk - x_avg)**2 / sum_x2)
        )

        
        upi = yk + rango
        lpi = yk - rango

        
        x_t = abs(r) * math.sqrt((n - 2) / (1 - r**2))
        p_val = self.integrar_t(x_t, n - 2)
        tail = 1 - 2 * p_val

        return sigma, t, rango, upi, lpi, yk, b0, b1, r, r2

    
    def t_student(self, p, dof):
        return 1.108 

    
    def integrar_t(self, x, dof):
        pasos = 1000
        h = x / pasos

        def f(t):
            return (math.gamma((dof+1)/2) /
                   (math.sqrt(dof*math.pi)*math.gamma(dof/2))) * \
                   (1 + (t**2)/dof) ** (-(dof+1)/2)

        area = 0
        for i in range(pasos):
            t1 = i*h
            t2 = (i+1)*h
            area += (f(t1) + f(t2)) * h / 2

        return area