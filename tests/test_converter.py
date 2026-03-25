import pytest
from src.converter import celsius_to_fahrenheit, celsius_to_kelvin, convert, kelvin_to_celsius, fahrenheit_to_celsius

# ── Basic tests using fixtures ──────────────────────────────────
@pytest.fixture
def test_freezing_c_to_f(freezing_point):
    # freezing_point is injected from conftest.py
    assert celsius_to_fahrenheit(freezing_point["C"]) == freezing_point["F"]

@pytest.fixture
def test_boiling_c_to_f(boiling_point):
    assert celsius_to_fahrenheit(boiling_point["C"]) == boiling_point["F"]

# ── Parametrize for multiple conversion cases ───────────────────

@pytest.mark.parametrize("c, expected_f", [
    (0,    32.0),   # freezing
    (100,  212.0),  # boiling
    (-40,  -40.0),  # where C and F are equal
    (37,   98.6),   # body temperature
])
def test_c_to_f_cases(c, expected_f):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected_f, rel=1e-3)

@pytest.mark.parametrize("value, from_u, to_u, expected", [
    (0,      "C", "F", 32.0),      # C → F
    (32,     "F", "C", 0.0),       # F → C
    (0,      "C", "K", 273.15),   # C → K
    (273.15, "K", "C", 0.0),       # K → C
    (32,     "F", "K", 273.15),   # F → K
    (273.15, "K", "F", 32.0),      # K → F
])
def test_convert_all_pairs(value, from_u, to_u, expected):
    assert convert(value, from_u, to_u) == pytest.approx(expected, rel=1e-3)

# ── Edge cases ──────────────────────────────────────────────────

@pytest.mark.edge
def test_absolute_zero_kelvin():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)

@pytest.mark.edge
def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)

@pytest.mark.edge
def test_negative_kelvin_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)   # this should raise ValueError

@pytest.mark.edge
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)

@pytest.mark.edge
def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)
    assert kelvin_to_celsius(0) == pytest.approx(-273.15)

@pytest.mark.edge
def test_unknown_unit_raises():
    with pytest.raises(ValueError):
        convert(100, 'C', 'X')  # 'X' is not a valid unit


@pytest.mark.edge
def test_same_unit_input():
    assert convert(100, 'C', 'C') == pytest.approx(100.0)
    assert convert(32, 'F', 'F') == pytest.approx(32.0)
    assert convert(273.15, 'K', 'K') == pytest.approx(273.15)
    
# TODO: add more tests to reach ≥ 80% coverage!
# Suggestions:
