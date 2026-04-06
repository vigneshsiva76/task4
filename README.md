# 🌡️ Temperature Converter
**Cognifyz Internship — Task 4**

---

## Overview

A clean, interactive command-line program that converts temperatures between
**Celsius** and **Fahrenheit**. Built in Python with a complete automated test
suite covering 18 test cases.

---

## Project Structure

```
temperature_converter/
├── temperature_converter.py      # Main program
├── test_temperature_converter.py # Automated test suite (18 tests)
└── README.md                     # This file
```

---

## How to Run

### Requirements
- Python 3.7 or higher (no external libraries needed)

### Start the program
```bash
python temperature_converter.py
```

### Sample session
```
====================================================
      🌡️   TEMPERATURE CONVERTER  🌡️
           Cognifyz Internship — Task 4
====================================================

  Choose conversion direction:
    [1]  Celsius  →  Fahrenheit
    [2]  Fahrenheit  →  Celsius
    [Q]  Quit

  Your choice: 1

  Enter temperature in Celsius: 100

  ──────────────────────────────────────────────
  Input  :    100.0000 °C
  Result :    212.0000 °F
  ──────────────────────────────────────────────

  Convert another temperature? [Y / N]:
```

---

## Conversion Formulas

| Direction | Formula |
|-----------|---------|
| Celsius → Fahrenheit | `F = (C × 9/5) + 32` |
| Fahrenheit → Celsius | `C = (F − 32) × 5/9` |

---

## Key Temperature References

| Celsius | Fahrenheit | Description |
|---------|------------|-------------|
| −273.15 | −459.67 | Absolute zero |
| −40 | −40 | Crossover point |
| 0 | 32 | Water freezing point |
| 25 | 77 | Comfortable room temperature |
| 37 | 98.6 | Normal body temperature |
| 100 | 212 | Water boiling point (sea level) |

---

## Running Tests

```bash
python test_temperature_converter.py
```

The test suite includes **18 tests** across 3 categories:
- `TestCelsiusToFahrenheit` — 7 tests (freezing, boiling, body temp, absolute zero, room temp, negatives, fractions)
- `TestFahrenheitToCelsius` — 7 tests (same reference points in reverse)
- `TestRoundTrip` — 4 tests (convert C→F→C and F→C→F and verify identity)

Expected output:
```
====================================================
   Running Temperature Converter Test Suite
====================================================
test_absolute_zero ... ok
test_body_temperature ... ok
...
----------------------------------------------------------------------
Ran 18 tests in 0.001s

OK
```

---

## Features

- ✅ Accepts any numeric temperature (integers, decimals, negatives)
- ✅ User chooses conversion direction from a clear menu
- ✅ Validates input — gracefully handles non-numeric entries
- ✅ Loop — convert multiple temperatures in one session
- ✅ Clean, formatted result display
- ✅ 18-test automated test suite with round-trip verification

---

## Author
Vicky | Cognifyz Internship Program
