import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.s = math.sqrt(radius**2 + height**2)
        self.volume = (1/3) * math.pi * radius**2 * height
        self.base_area = math.pi * radius**2
        self.lateral_area = math.pi * radius * self.s
        self.total_area = self.lateral_area + self.base_area

    def __str__(self):
        return (
            f"Raadius: {self.radius}\n"
            f"Kõrgus: {self.height}\n"
            f"Külgpindala: {self.lateral_area:.2f}\n"
            f"Põhja pindala: {self.base_area:.2f}\n"
            f"Täispindala: {self.total_area:.2f}\n"
            f"Maht: {self.volume:.2f}"
        )

