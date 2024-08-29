class Quadratic:
    def __init__(self, a: float, b: float, c: float):

        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self) -> str:

        result = f"{self.a}x^2"
        result += f" + {self.b}x" if self.b >= 0 else f" - {-self.b}x"
        result += f" + {self.c}" if self.c >= 0 else f" - {-self.c}"
        return result

    def __add__(self, other: 'Quadratic') -> 'Quadratic':

        return Quadratic(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other: 'Quadratic') -> 'Quadratic':

        return Quadratic(self.a - other.a, self.b - other.b, self.c - other.c)

q1 = Quadratic(1.0, 2.0, 3.0)
q2 = Quadratic(3.0, -4.0, 5.0)

sum_quadratic = q1 + q2
diff_quadratic = q1 - q2

print(f"Tam thức q1: {q1}")
print(f"Tam thức q2: {q2}")
print(f"Tổng của 2 tam thức: {sum_quadratic}")
print(f"Hiệu của 2 tam thức: {diff_quadratic}")
