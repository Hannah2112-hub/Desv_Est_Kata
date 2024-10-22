class NoSePuedeCalcular(Exception):
    pass

class Calculadora:
    def validar_elementos(self, elementos):
        if not elementos:
            raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía")

        for elemento in elementos:
            if not isinstance(elemento, (int, float)):
                raise TypeError("Todos los elementos deben ser numéricos")

    def media(self, elementos):
        self.validar_elementos(elementos)
        return sum(elementos) / len(elementos)
