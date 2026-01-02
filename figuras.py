class Figura():
    def __init__(self,color, nombre):
        self.color = color
        self.nombre = nombre
        
    def mostrar_info(self, color, nombre):
        print(f"El nombre es {self.nombre} y el color es {self.color}")
    
    def calcular_area():
        return 0
    

class Cuadrado(Figura):
    def __init__(self, color, nombre, lado):
        super().__init__(color, nombre)
        self.lado = lado
        print(f"Cuadrado {nombre} creado. Lado {lado}")
    
    def calcular_area(self, lado):
        area = self.lado*self.lado
        return area
    
    

    