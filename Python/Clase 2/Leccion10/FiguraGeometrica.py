#Copia de la clase 1 para clases abstractas clase 2
from abc import ABC, abstractmethod
class FiguraGeometrica (ABC): #Clase padre 1
    def __init__(self,ancho,alto):
        if self.validar_valores(ancho): #Sintaxis simplificada para preguntar un rango
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'valor erroneo para el ancho:{ancho}')
        if self.validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto:{alto}')
#TAREA: encapsular los atributos de la clase Figura Geometrica.Agregar getters y setters y dunder str
    @property
    def ancho(self): #Getter ancho
        return self._ancho
    @ancho.setter
    def ancho(self,ancho): #Setter ancho
        if self.validar_valores(ancho):
           self._ancho=ancho
        else:
            print(f'Valor erroneo:{ancho}')
    @property
    def alto(self): #Getter alto
        return self._alto
    @alto.setter
    def alto(self,alto): #Setter alto
        if self.validar_valores(alto):
            self._alto=alto
        else:
            print(f'Valor erroneo:{alto}')

    @abstractmethod
    def calcular_area(self):
        pass
    #Metodo Dunder str
    def __str__(self):
        return f'Figura Geometrica[ancho = {self._ancho},alto = {self._alto}]'

    def validar_valores(self,valor): #Metodo encapsulado
        return True if 0<valor<10 else False #sintaxis simplificada de if else