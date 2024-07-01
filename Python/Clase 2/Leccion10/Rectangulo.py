#Copia de la clase 1 para clases abstractas clase 2
from Color import Color #importamos las clases
from FiguraGeometrica import FiguraGeometrica #importamos las clases

class Rectangulo(FiguraGeometrica,Color):#Se aplica la herencia multiple
    def __init__(self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto)#Inicializamos figura geometrica lado ancho y alto
        Color.__init__(self,color)#Inicializamos color, el atributo color

    def calcular_area(self):#metodo para calcular el area del rectangulo
        return f'Area del rectangulo = {self.ancho * self.alto}'

    #Sobrescribimos el metodo dunder str
    def __str__(self):
        return f'Rectangulo[{FiguraGeometrica.__str__(self)},{Color.__str__(self)}]'