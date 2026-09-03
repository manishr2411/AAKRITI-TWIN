import unittest

import pandas as pd

from src.processing.coordinate_converter import polar_to_cartesian, convert_scan_to_xy


class TestCoordinateConverter(unittest.TestCase):
    def test_polar_to_cartesian_90_deg(self):
        x, y = polar_to_cartesian(90, 80)
        self.assertAlmostEqual(x, 0, places=1)
        self.assertAlmostEqual(y, 80, places=1)

    def test_polar_to_cartesian_0_deg(self):
        x, y = polar_to_cartesian(0, 100)
        self.assertAlmostEqual(x, 100, places=1)
        self.assertAlmostEqual(y, 0, places=1)

    def test_convert_scan_to_xy_adds_columns(self):
        df = pd.DataFrame(
            [
                {"scan_id": 1, "timestamp": 1, "angle_deg": 30, "distance_cm": 120},
                {"scan_id": 1, "timestamp": 2, "angle_deg": 90, "distance_cm": 80},
            ]
        )

        result = convert_scan_to_xy(df)

        self.assertIn("x", result.columns)
        self.assertIn("y", result.columns)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()