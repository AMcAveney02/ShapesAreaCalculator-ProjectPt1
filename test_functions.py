import unittest # imports unittest for me to be able to test my functions for run time errors
from functions import * # imports all the functions created from the functions module


class TestFunctions(unittest.TestCase):

    delta_value = 0.0000001 # sets the delta value to save time typing out the decimal

    def test_circle(self):
        """
        Function to test the output of the area_of_circle function with multiple types of inputs
        :return: All tests passed with no run time errors, meaning the computation functions are working as they should be
        """
        # These three test for integer inputs
        self.assertAlmostEqual(area_of_circle(2), 12.5663706, delta=self.delta_value)
        self.assertAlmostEqual(area_of_circle(5), 78.5398163, delta=self.delta_value)
        self.assertAlmostEqual(area_of_circle(4), 50.2654824, delta=self.delta_value)
        # These three test for floating point inputs
        self.assertAlmostEqual(area_of_circle(2.5), 19.634954, delta=self.delta_value)
        self.assertAlmostEqual(area_of_circle(5.7), 102.0703453, delta=self.delta_value)
        self.assertAlmostEqual(area_of_circle(1.45), 6.6051985, delta=self.delta_value)
        # These three test for type error inputs
        self.assertRaises(TypeError, area_of_circle, 'x')
        self.assertRaises(TypeError, area_of_circle, 'Ythd')
        self.assertRaises(TypeError, area_of_circle, '23fdsf')
        # These three test for value error/negative inputs
        self.assertRaises(ValueError, area_of_circle, -2)
        self.assertRaises(ValueError, area_of_circle, -4536.78)
        self.assertRaises(ValueError, area_of_circle, -2327)


    def test_rectangle(self):
        """
        Function to test the output of the area_of_rectangle function with multiple types of inputs
        :return: All tests passed with no run time errors, meaning the computation functions are working as they should be
        """
        # These three test for integer inputs
        self.assertEqual(area_of_rectangle(2, 4), 8)
        self.assertEqual(area_of_rectangle(8, 5), 40)
        self.assertEqual(area_of_rectangle(10, 6), 60)
        # These three test for floating point inputs
        self.assertAlmostEqual(area_of_rectangle(2.5, 4.3), 10.7500000)
        self.assertAlmostEqual(area_of_rectangle(5.7, 9.2), 52.4400000)
        self.assertAlmostEqual(area_of_rectangle(17.83, 3.456), 61.6204800)
        # These three test for value error/negative inputs
        self.assertRaises(ValueError, area_of_rectangle, 2, -4)
        self.assertRaises(ValueError, area_of_rectangle, -21, 245)
        self.assertRaises(ValueError, area_of_rectangle, 7, -47.8)
        # These three test for type error inputs
        self.assertRaises(TypeError, area_of_rectangle, 'asd', 'afdf')
        self.assertRaises(TypeError, area_of_rectangle, 'ewrwf', 2)
        self.assertRaises(TypeError, area_of_rectangle, 23, 'Yes')

    def test_square(self):
        """
        Function to test the output of the area_of_square function with multiple types of inputs
        :return: All tests passed with no run time errors, meaning the computation functions are working as they should be
        """
        # These three test for integer inputs
        self.assertEqual(area_of_square(2), 4)
        self.assertEqual(area_of_square(8), 64)
        self.assertEqual(area_of_square(25), 625)
        # These three test for floating point inputs
        self.assertAlmostEqual(area_of_square(2.5), 6.2500000)
        self.assertAlmostEqual(area_of_square(4.5632), 20.8227942)
        self.assertAlmostEqual(area_of_square(87.65423), 7683.2640369)
        # These three test for type error inputs
        self.assertRaises(TypeError, area_of_square, 'zxasd')
        self.assertRaises(TypeError, area_of_square, 'How are you?')
        self.assertRaises(TypeError, area_of_square, "I'm good, thanks for asking!")
        # These three test for value error/negative inputs
        self.assertRaises(ValueError, area_of_square, -45)
        self.assertRaises(ValueError, area_of_square, -865.23)
        self.assertRaises(ValueError, area_of_square, -987.2312132)

    def test_triangle(self):
        """
        Function to test the output of the area_of_triangle function with multiple types of inputs
        :return: All tests passed with no run time errors, meaning the computation functions are working as they should be
        """
        # These three test for integer inputs
        self.assertEqual(area_of_triangle(4, 5), 10)
        self.assertEqual(area_of_triangle(8, 8), 32)
        self.assertEqual(area_of_triangle(10, 10), 50)
        # These three test for floating point inputs
        self.assertAlmostEqual(area_of_triangle(2.5, 7.345), 9.1812500)
        self.assertAlmostEqual(area_of_triangle(8.6, 4.56), 19.6080000)
        self.assertAlmostEqual(area_of_triangle(6.387, 45), 143.7075000)
        # These six test for type error inputs
        self.assertRaises(TypeError, area_of_triangle, 'x', 2)
        self.assertRaises(TypeError, area_of_triangle, '4', 6)
        self.assertRaises(TypeError, area_of_triangle, "I've been coding for 6 hours", 9)
        self.assertRaises(TypeError, area_of_triangle, 'adfjbf', 'sdgfg')
        self.assertRaises(TypeError, area_of_triangle, 'Howdy', 'I am tired')
        self.assertRaises(TypeError, area_of_triangle, 'So close to the semester being over', 'So excited')
        # These three test for value error/negative inputs
        self.assertRaises(ValueError, area_of_triangle, -3, 4)
        self.assertRaises(ValueError, area_of_triangle, 45, -7.54)
        self.assertRaises(ValueError, area_of_triangle, -38973, -4.789)

    def test_power(self):
        """
        Function to test the output of the power_of_number function with multiple types of inputs
        :return: All tests passed with no run time errors, meaning the computation functions are working as they should be
        """
        # These three test for integer inputs
        self.assertEqual(power_of_number(4, 2), 16)
        self.assertEqual(power_of_number(10, 3), 1000)
        self.assertEqual(power_of_number(23, 1), 23)
        # These three test for floating point inputs
        self.assertAlmostEqual(power_of_number(4.3, 2.1), 21.3935943)
        self.assertAlmostEqual(power_of_number(5.6, 3.42), 362.0787626)
        self.assertAlmostEqual(power_of_number(2.4, 8.78), 2178.9873161)
        # These six test for type error inputs
        self.assertRaises(TypeError, power_of_number, 'x', 2)
        self.assertRaises(TypeError, power_of_number, 65, 'y')
        self.assertRaises(TypeError, power_of_number, 453.23, 'Hello again')
        self.assertRaises(TypeError, power_of_number, 'x', 'y')
        self.assertRaises(TypeError, power_of_number, 'So close', 'Almost done')
        self.assertRaises(TypeError, power_of_number, 'Top of the morning to ya', 'Howdy once again')

if __name__ == '__main__':
    unittest.main()