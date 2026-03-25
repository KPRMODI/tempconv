# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit.
    Formula: (c * 9/5) + 32
    Example: 0°C → 32.0°F,  100°C → 212.0°F
    """
    # TODO: implement
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius.
    Formula: (f - 32) * 5/9
    Example: 32°F → 0.0°C,  212°F → 100.0°C
    """
    # TODO: implement
    return (f - 32) * 5/9

def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin.
    Formula: c + 273.15
    Raises: ValueError if c < ABSOLUTE_ZERO_C
    Example: 0°C → 273.15K,  -273.15°C → 0.0K
    """
    # TODO: implement (remember to guard against below absolute zero)
    if c < ABSOLUTE_ZERO_C:
        raise ValueError(f"Temperature {c}°C is below absolute zero")
    return c + 273.15

def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius.
    Formula: k - 273.15
    Raises: ValueError if k < 0
    Example: 273.15K → 0.0°C,  0K → -273.15°C
    """
    # TODO: implement (remember: Kelvin cannot be negative)
    if k < 0:
        raise ValueError(f"Kelvin cannot be negative: {k}")
    return k - 273.15

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between any supported units.

    Units: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    Raises: ValueError for unknown units or invalid temperatures.

    Examples:
        convert(100, 'C', 'F')  →  212.0
        convert(32,  'F', 'C')  →  0.0
        convert(0,   'C', 'K')  →  273.15
    """
    # Normalize to uppercase so 'c' and 'C' both work
    from_unit = from_unit.upper()
    to_unit   = to_unit.upper()

    # If same unit, return as-is
    if from_unit == to_unit:
        return float(value)

    # TODO: implement the conversion routing.
    # Hint: convert via Celsius as the intermediate unit.
    # C → F, C → K, F → C, F → K (via C), K → C, K → F (via C)
    # Raise ValueError for unknown units.
    
    # First: convert input to Celsius
    if from_unit == "C":
        celsius = float(value)
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown unit: {from_unit}")

    # Then: convert Celsius to the target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown unit: {to_unit}")