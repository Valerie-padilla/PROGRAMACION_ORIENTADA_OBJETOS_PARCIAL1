"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

def area_rectangulo(base,altura):
    return base*altura

print(area_rectangulo(5,3))

class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base * self.altura
rect=rectangulo(5,3)
print(rect.area())


#Otro ejemplo
class Rectangulos:
    def area(self, base, altura):
        areaR=base*altura
        return areaR

rectangulo1=Rectangulos()
print(f"El area del rectangulo es {rectangulo1.area(5,6)}")


