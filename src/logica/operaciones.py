class NoSePuedeCalcular(Exception):
    pass

class Calculadora:
    def validar_elementos(self, elementos):
        if not elementos:
            raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía")

        if not all(isinstance(elemento, (int, float)) for elemento in elementos):
            raise TypeError("Todos los elementos deben ser numéricos")

    def desviacion_estandar(self, elementos):
        self.validar_elementos(elementos)
        if len(elementos) == 1:
            return 0

    def _calcular_promedio(self, elementos):
        return sum(elementos) / len(elementos)

    def media(self, elementos):
        self.validar_elementos(elementos)
        return self._calcular_promedio(elementos)
