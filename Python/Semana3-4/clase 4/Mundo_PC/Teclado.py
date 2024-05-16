from Mundo_PC.Dispositivo_Entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_Teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_Teclados += 1
        self._id_teclados = Teclado.contador_Teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_teclados}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'



if __name__ == "__main__":
    teclado1 = Teclado('ACER', 'USB')
    print(teclado1)
    teclado2 = Teclado('TIME', 'Bluetooth')
    print(teclado2)
