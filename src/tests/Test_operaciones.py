import unittest
from src.logica.operaciones import Calculadora, NoSePuedeCalcular


class PruebaCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def tearDown(self):
        self.calculadora = None

    # 1.1 Caso sin elementos
    def test_media_listaVacia_lanzaExcepcion(self):
        elementos = []
        with self.assertRaises(NoSePuedeCalcular):
            self.calculadora.media(elementos)
