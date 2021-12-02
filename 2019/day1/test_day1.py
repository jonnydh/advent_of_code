import pytest
from part1 import floor_divide_by_three, subtract_two, calculate_module_fuel, calculate_fuel_for_fuel

@pytest.mark.parametrize("num, expected_result", [
    (12, 4), 
    (14, 4)
])
def test_floor_divide_by_three(num, expected_result):
    assert floor_divide_by_three(num) == expected_result

@pytest.mark.parametrize("num, expected_result", [
    (4, 2),
    (5, 3)
])
def test_subtract_two(num, expected_result):
    assert subtract_two(num == expected_result)

@pytest.mark.parametrize("input, expected_result", [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583)
])
def test_calculate_module_fuel(input, expected_result):
    assert calculate_module_fuel(input) == expected_result

@pytest.mark.parametrize("input, expected_result", [
    (14, 2),
    (1969, 966),
    (100756, 50346)
])
def test_calculate_fuel_for_fuel(input, expected_result):
    assert calculate_fuel_for_fuel(input) == expected_result
