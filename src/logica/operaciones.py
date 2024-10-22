class NoSePuedeCalcular(Exception):
    pass

class Calculadora:
    def media(self, elementos):
        if not elementos:
            raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía")
