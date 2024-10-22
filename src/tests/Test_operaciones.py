import unittest
from src.logica.operaciones import Calculadora, NoSePuedeCalcular


class PruebaCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def tearDown(self):
        self.calculadora = None

    def test_media_listaVacia_lanzaExcepcion(self):
        elementos = []
        with self.assertRaises(NoSePuedeCalcular):
            self.calculadora.media(elementos)

    def test_media_unElemento_retornaElMismoValor(self):
        elementos = [10]
        resultado = self.calculadora.media(elementos)
        self.assertEqual(resultado, 10)

    def test_media_dosElementos_retornaPromedio(self):
        elementos = [10, 20]
        resultado = self.calculadora.media(elementos)
        self.assertEqual(resultado, 15)

    def test_media_elementosPositivos_retornaPromedio(self):
        elementos = [1, 2, 3, 4, 5]
        resultado = self.calculadora.media(elementos)
        self.assertEqual(resultado, 3)

    def test_media_elementosCero(self):
        elementos = [0, 0, 0, 0]
        resultado = self.calculadora.media(elementos)
        self.assertEqual(resultado, 0)

    def test_media_elementosPositivosYNegativos_retornaPromedio(self):
        elementos = [-1, 1, -2, 2]
        resultado = self.calculadora.media(elementos)
        self.assertEqual(resultado, 0)

    def test_media_elementosNoNumericos_lanzaTypeError(self):
        elementos = [1, 'a', 3]
        with self.assertRaises(TypeError):
            self.calculadora.media(elementos)

    def test_desviacion_elementosVacios_lanzaNoSePuedeCalcular(self):
        elementos = []
        with self.assertRaises(NoSePuedeCalcular):
            self.calculadora.desviacion_estandar(elementos)

    def test_desviacion_unSoloElemento_retornaCero(self):
        elementos = [5]
        resultado = self.calculadora.desviacion_estandar(elementos)
        self.assertEqual(resultado, 0)

    def test_desviacion_dosElementos_retornaDesviacion(self):
        elementos = [5, 9]
        resultado = self.calculadora.desviacion_estandar(elementos)
        self.assertAlmostEqual(resultado, 2)

    def test_desviacion_elementosPositivos_retornaDesviacion(self):
        elementos = [1, 2, 3, 4, 5]
        resultado = self.calculadora.desviacion_estandar(elementos)
        self.assertAlmostEqual(resultado, 1.4142, places=4)

    def test_desviacion_elementosCero_retornaCero(self):
        elementos = [0, 0, 0, 0]
        resultado = self.calculadora.desviacion_estandar(elementos)
        self.assertEqual(resultado, 0)

    def test_desviacion_elementosPositivosYNegativos_retornaDesviacion(self):
        elementos = [-1, 1, -2, 2]
        resultado = self.calculadora.desviacion_estandar(elementos)
        self.assertAlmostEqual(resultado, 1.8257, places=4)



