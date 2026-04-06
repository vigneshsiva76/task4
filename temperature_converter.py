"""
temperature_converter.py
Cognifyz Internship - Task 4
Temperature Converter: Celsius <-> Fahrenheit
"""

# ─────────────────────────────────────────────
#  Conversion formulas
# ─────────────────────────────────────────────

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using: F = (C × 9/5) + 32"""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using: C = (F − 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9


# ─────────────────────────────────────────────
#  Input helpers
# ─────────────────────────────────────────────

def get_temperature_input(prompt: str) -> float:
    """Prompt the user for a numeric temperature value; retry on invalid input."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  ✗  '{raw}' is not a valid number. Please try again.\n")


def get_menu_choice(prompt: str, valid_choices: set) -> str:
    """Prompt the user to choose from a set of valid options."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print(f"  ✗  Invalid choice '{choice}'. Valid options: {', '.join(sorted(valid_choices))}\n")


# ─────────────────────────────────────────────
#  Display helpers
# ─────────────────────────────────────────────

DIVIDER = "=" * 52

def print_header():
    print(f"\n{DIVIDER}")
    print("      🌡️   TEMPERATURE CONVERTER  🌡️")
    print(f"           Cognifyz Internship — Task 4")
    print(DIVIDER)


def print_result(original_value: float, original_unit: str,
                 converted_value: float, converted_unit: str):
    print(f"\n  {'─' * 46}")
    print(f"  Input  : {original_value:>10.4f} °{original_unit}")
    print(f"  Result : {converted_value:>10.4f} °{converted_unit}")
    print(f"  {'─' * 46}")


def print_menu():
    print("\n  Choose conversion direction:")
    print("    [1]  Celsius  →  Fahrenheit")
    print("    [2]  Fahrenheit  →  Celsius")
    print("    [Q]  Quit")


# ─────────────────────────────────────────────
#  Core application loop
# ─────────────────────────────────────────────

def run():
    print_header()

    while True:
        print_menu()
        choice = get_menu_choice("\n  Your choice: ", {"1", "2", "Q"})

        if choice == "Q":
            print("\n  👋  Goodbye! Stay temperature-aware.\n")
            break

        elif choice == "1":
            temp = get_temperature_input("\n  Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(temp)
            print_result(temp, "C", result, "F")

        elif choice == "2":
            temp = get_temperature_input("\n  Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_celsius(temp)
            print_result(temp, "F", result, "C")

        # Offer another conversion
        again = get_menu_choice("\n  Convert another temperature? [Y / N]: ", {"Y", "N"})
        if again == "N":
            print("\n  👋  Goodbye! Stay temperature-aware.\n")
            break
        print()


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    run()
