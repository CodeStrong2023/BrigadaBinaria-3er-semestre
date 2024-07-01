#Copia de la clase 1 para clases abstractas clase 2
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
#Creamos un objeto cuadrado
cuadrado1 = Cuadrado(5,'Violeta')#pasamos los argumentos, uno es el lado y el otro color
print(cuadrado1.ancho)#Imprimos el ancho
print(cuadrado1.alto)#Imprimimos el alto
print(f'Calcular area el cuadrado:{cuadrado1.calcular_area()}')

#Metodo Method Resolution Order (MRO)
#Permite cnoocer las jerarquias de las clases frente a la clase en la que estamos llamando un metodo.
#Ej: si queremos saber el orden en que se llaman o devuelven los metodos es utilizar el metodo MRO.
print(Cuadrado.mro())
#TAREA: Crear varios objetos de tipo cuadrado y rectangulo
#Objetos cuadrado
cuadrado2 = Cuadrado(10,'Azul')
cuadrado3 = Cuadrado(5,'Amarillo')
cuadrado4 = Cuadrado(6,'Rojo')
#Llamamos al metodo calcular_area y dunder str
print('Cuadrado'.center(50,' '))
print(cuadrado2.calcular_area()) #metodo calcular_area
print(cuadrado2) #metodo dunder str
print(cuadrado3.calcular_area()) #metodo calcular_area
print(cuadrado3) #metodo dunder str
print(cuadrado4.calcular_area()) #metodo calcular_area
print(cuadrado4) #metodo dunder str
#Objetos rectangulo
rectangulo1 = Rectangulo(3,6,'Naranja')
rectangulo2 = Rectangulo(10,20,'Negro')
rectangulo3 = Rectangulo(6,10,'Blanco')
#Llamamos al metodo calcular_aerea y dunder str
print('Rectangulo'.center(50,' '))
print(rectangulo1.calcular_area())#metodo calcular_aerea
print(rectangulo1)#metodo dunder str
print(rectangulo2.calcular_area())#metodo calcular_aerea
print(rectangulo2)#metodo dunder str
print(rectangulo3.calcular_area())#metodo calcular_aerea
print(rectangulo3)#metodo dunder str