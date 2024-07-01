class Persona:
    # Contexto static
    contador_personas = 0 # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls): # Método de clase
        cls.contador_personas += 1 # Vamos incrementando, el contador_personas se relaciona con la clase y no con el objeto, por eso no se reinicia
        return cls.contador_personas

    # Contexto dinamic
    def __init__(self, nombre ,edad): # Método Dunder init (Método Constructor)
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # Método str (toString)
         return f'Persona [ID: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}]'


persona1 = Persona('Matias',19)
print(persona1)
persona2 = Persona('Nadia', 34)
print(persona2)
persona3 = Persona('Marta', 26)
print(persona3)
#Persona.generar_siguiente_valor()
persona4 = Persona('Carlos', 62)
print(persona4)

print(f'Valor contador de personas: {Persona.contador_personas}')