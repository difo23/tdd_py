# Cargamos el módulo unittest
import unittest  

#Primer error resuelto importar clase Calculadora
from calculator import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):  

    def setUp(self):
        self.calc = Calculator()

    # Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        #ejecutamos el metodo
        self.calc.add(1,3)
        #Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    def test_rest_method(self):
        self.calc.rest(1, 2)
        self.assertEqual(-1, self.calc.value);