# declaramos una variable
try:
    archivo = open("prueba.txt", "w",encoding = "utf8") # la w es de write que significa escribir
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Los acentos son importantes para las palabras\n")
    archivo.write("Por ejemplo: acción, ejecución y producción\n")
    archivo.write("las letras son:\n r read(leer),\n a append(anexa),\n w write(escribe),\n x(crea un archivo)\n")
    archivo.write("t text(texto),\n b binary(archivos binarios),\n w+ (lee y escribe a la vez),\n  r+ (son iguales)\n")
    archivo.write("Saludos a todos los alumnos de la tecnicatura\n")
    archivo.write("Con esto terminamos\n")
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
 # archivo.write("Todo quedo perfecto")  este es un error
