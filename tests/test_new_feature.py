import sys
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from sp211 import new_feature

def test_calculate_fuel_cost_default():
    # 6.5 L/100km consumption and 44.90 TL/L fuel price for 100 km
    cost = new_feature.calculate_fuel_cost(100)
    expected = 6.5 * 44.90
    assert round(cost, 2) == round(expected, 2)

def test_calculate_fuel_cost_custom():
    cost = new_feature.calculate_fuel_cost(200, consumption_l_per_100km=5.0, fuel_price_per_liter=40.0)
    expected = (200 / 100) * 5.0 * 40.0
    assert round(cost, 2) == round(expected, 2)

def test_calculate_total_distance_from_gpkg():
    gpkg_path = Path(__file__).resolve().parent.parent / "examples" / "output" / "shortest_path.gpkg"
    distance = new_feature.calculate_total_distance(gpkg_path)
    
    # This test checks that no exception is raised
    assert distance > 0