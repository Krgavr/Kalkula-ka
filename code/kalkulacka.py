import math 

class Kalkulacka:
    def __init__(self):
        self.last_result = 0

    def plus(self, a, b):
        self.last_result = a + b
        return a + b
        

    def posledni_vysledek(self):
        return self.last_result

    def sin(self, x):
        self.last_result = math.sin(x)
        return math.sin(x)
