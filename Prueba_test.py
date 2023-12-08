import unittest

def sumar(a, b):
    return a + b

class TestSumar(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-2, -7), -9)

    def test_suma_mezclada(self):
        self.assertEqual(sumar(10, -4), 6)

    def test_suma_cero(self):
        self.assertEqual(sumar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
