class Figura():
    def __init__(self,color, nombre):
        self.color = color
        self.nombre = nombre
        
    def mostrar_info(self):
        print(f"El nombre es {self.nombre} y el color es {self.color}")
    
    def calcular_area(self):
        return 0
    

class Cuadrado(Figura):
    def __init__(self, color, nombre, lado):
        super().__init__(color, nombre)
        self.lado = lado
        print(f"Cuadrado {nombre} creado. Lado {lado}")
    
    def calcular_area(self):
        area = self.lado*self.lado
        return area
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cuadrado {self.nombre}. Lado {self.lado}")
    
    
class Circulo(Figura):
    def __init__(self, color, nombre, radio):
        super().__init__(color, nombre)
        self.radio = radio
        print(f"Circulo {nombre} creado. Radio {radio}")
    def calcular_area(self):
        area = 3.14*self.radio*self.radio
        return area
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Circulo {self.nombre}. Radio {self.radio}")


class Triangulo(Figura):
    def __init__(self, color, nombre, base, altura):
        super().__init__(color, nombre)
        self.base = base
        self.altura = altura
        print(f"Triangulo {nombre} creado. Base {base}, Altura {altura}")
        
    def calcular_area(self):
        area = (self.base * self.altura)/2
        return area
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Triangulo {self.nombre}. Base {self.base}, Altura {self.altura}")
        
        
fig1 = Cuadrado("rojo","Cuadrado xy", 3)
fig2 = Circulo("Verde", "Circulo abc", 2)
fig3 = Triangulo("Azul", "Triangulo sdf", 3, 4)

"""
fig1.mostrar_info()
fig2.mostrar_info()
fig3.mostrar_info()

print("El area del cuadrado es: ", fig1.calcular_area())
print("El area del circulo es: ", fig2.calcular_area())
print("El area del triangulo es: ", fig3.calcular_area())
"""

def mostrar_area_figura(figura):
    print("Calculando area de", figura.nombre)
    print("Area: ", figura.calcular_area())

mostrar_area_figura(fig1)
mostrar_area_figura(fig2)
mostrar_area_figura(fig3)