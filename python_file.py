print("Тест триггера запуска пайплайна")

# tests_calculator_unittest.py

import unittest 


class Calculator: 
    def add(self, a, b):  # Метод сложения двух чисел
        return a + b  

    def subtract(self, a, b):  # Метод вычитания
        return a - b  

    def multiply(self, a, b):  # Метод умножения
        return a * b 

    def divide(self, a, b):  # Метод деления
        if b == 0: 
            raise ZeroDivisionError("Division by zero is forbidden")  
        return a / b  


class TestCalculator(unittest.TestCase): 

    def setUp(self): 
        self.calc = Calculator()  

    def test_add(self):  # Тестируем сложение
        self.assertEqual(self.calc.add(2, 3), 5)  # Проверяем, что 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # Проверяем, что -1 + 1 = 0
        self.assertEqual(self.calc.add(0, 0), 0)  # Проверяем, что 0 + 0 = 0

    def test_subtract(self):  # Тестируем вычитание
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Проверяем, что 5 - 3 = 2
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Проверяем, что 0 - 5 = -5
        self.assertEqual(self.calc.subtract(-3, -3), 0)  # Проверяем, что -3 - (-3) = 0

    def test_multiply(self):  # Тестируем умножение
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Проверяем, что 2 * 3 = 6
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Проверяем, что -2 * 3 = -6
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Проверяем, что 0 * 10 = 0

    def test_divide_ok(self):  # Тестируем корректное деление
        self.assertEqual(self.calc.divide(10, 2), 5)  # Проверяем, что 10 / 2 = 5

    def test_divide_by_zero(self):  # Тестируем, что деление на ноль вызывает ошибку
        with self.assertRaises(ZeroDivisionError):  # Ожидаем ZeroDivisionError
            self.calc.divide(10, 0)  # Делим на ноль и проверяем, что упали


if __name__ == "__main__": 
    unittest.main(verbosity=2)
