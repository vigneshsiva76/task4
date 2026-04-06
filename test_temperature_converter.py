"""
test_temperature_converter.py
Automated tests for temperature_converter.py
Cognifyz Internship — Task 4
"""

import unittest
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

DELTA = 1e-6  # floating-point tolerance


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Tests for celsius_to_fahrenheit()"""

    def test_freezing_point(self):
        """0 °C  →  32 °F  (water freezing point)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, delta=DELTA)

    def test_boiling_point(self):
        """100 °C  →  212 °F  (water boiling point at sea level)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0, delta=DELTA)

    def test_body_temperature(self):
        """37 °C  →  98.6 °F  (normal body temperature)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, delta=DELTA)

    def test_absolute_zero(self):
        """-273.15 °C  →  -459.67 °F  (absolute zero)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, delta=DELTA)

    def test_room_temperature(self):
        """25 °C  →  77 °F  (comfortable room temp)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0, delta=DELTA)

    def test_negative_value(self):
        """-40 °C  →  -40 °F  (the crossover point)"""
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0, delta=DELTA)

    def test_fractional_value(self):
        """36.6 °C  →  97.88 °F"""
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, delta=DELTA)


class TestFahrenheitToCelsius(unittest.TestCase):
    """Tests for fahrenheit_to_celsius()"""

    def test_freezing_point(self):
        """32 °F  →  0 °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0, delta=DELTA)

    def test_boiling_point(self):
        """212 °F  →  100 °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0, delta=DELTA)

    def test_body_temperature(self):
        """98.6 °F  →  37 °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, delta=DELTA)

    def test_room_temperature(self):
        """77 °F  →  25 °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(77), 25.0, delta=DELTA)

    def test_negative_value(self):
        """-40 °F  →  -40 °C  (the crossover point)"""
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0, delta=DELTA)

    def test_absolute_zero(self):
        """-459.67 °F  →  -273.15 °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(-459.67), -273.15, places=2)

    def test_fractional_value(self):
        """98.0 °F  →  36.666... °C"""
        self.assertAlmostEqual(fahrenheit_to_celsius(98.0), 36.6666666, delta=1e-4)


class TestRoundTrip(unittest.TestCase):
    """Round-trip tests: convert back and forth and check identity."""

    def test_roundtrip_zero(self):
        self.assertAlmostEqual(
            fahrenheit_to_celsius(celsius_to_fahrenheit(0)), 0, delta=DELTA)

    def test_roundtrip_100(self):
        self.assertAlmostEqual(
            fahrenheit_to_celsius(celsius_to_fahrenheit(100)), 100, delta=DELTA)

    def test_roundtrip_negative(self):
        self.assertAlmostEqual(
            celsius_to_fahrenheit(fahrenheit_to_celsius(-40)), -40, delta=DELTA)

    def test_roundtrip_float(self):
        original = 36.6
        self.assertAlmostEqual(
            fahrenheit_to_celsius(celsius_to_fahrenheit(original)),
            original, delta=DELTA)


if __name__ == "__main__":
    print("=" * 52)
    print("   Running Temperature Converter Test Suite")
    print("=" * 52)
    unittest.main(verbosity=2)
