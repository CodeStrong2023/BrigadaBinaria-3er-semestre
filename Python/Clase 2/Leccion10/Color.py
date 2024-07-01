#Copia de la clase 1 para clases abstractas clase 2
class Color:
    def __init__(self,color):
        self._color = color
#TAREA: Encapsular el atributo color.Agregar getters y setters y dunder str
    @property
    def color(self): #Getter color
        return self._color
    @color.setter
    def color(self,color): #Setter color
        self._color=color
    #Metodo Dunder str
    def __str__(self):
        return f'Color[color = {self._color}]'