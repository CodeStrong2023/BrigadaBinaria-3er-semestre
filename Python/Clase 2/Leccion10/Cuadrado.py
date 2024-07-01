#Copia de la clase 1 para clases abstractas clase 2
from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):#Aquí se está aplicando la herencia multiple
    def __init__(self, lado,color):
#En herencia multiple no se va a utilizar el super, ya que se podría generar una confucion, tanto como para el programador como para el compilador
        FiguraGeometrica.__init__(self,lado,lado)#Inicializamos figura geometrica lado ancho y alto
        Color.__init__(self,color)#Inicializamos color, el atributo color

    def calcular_area(self):#Metodo que multiplica lado ancho por alto
        return f'Area del cuadrado = {self.alto * self.ancho}'

#TAREA:Sobrescribir el motodo dunder str
    def __str__(self):
        return f'Cuadrado[{FiguraGeometrica.__str__(self)},{Color.__str__(self)}]'