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
