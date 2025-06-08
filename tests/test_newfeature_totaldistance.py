import unittest
from pathlib import Path
from sp211.new_feature import calculate_total_distance

class TestCalculateTotalDistance(unittest.TestCase):
    def test_distance_is_positive(self):
        # Path to the example GPKG file
        gpkg_path = Path(__file__).resolve().parent.parent / "examples" / "output" / "shortest_path.gpkg"
        distance = calculate_total_distance(gpkg_path)
        self.assertGreater(distance, 0, "Distance should be greater than zero")

if __name__ == '__main__':
    unittest.main()