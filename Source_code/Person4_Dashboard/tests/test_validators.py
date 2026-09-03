import unittest

import pandas as pd

from src.processing.validators import validate_scan_df, validate_object_df


class TestValidators(unittest.TestCase):
    def test_validate_scan_df_success(self):
        df = pd.DataFrame(
            [
                {
                    "scan_id": 1,
                    "timestamp": 1710000000,
                    "angle_deg": 30,
                    "distance_cm": 120,
                }
            ]
        )

        is_valid, errors = validate_scan_df(df)

        self.assertTrue(is_valid)
        self.assertEqual(errors, [])

    def test_validate_scan_df_missing_column(self):
        df = pd.DataFrame(
            [
                {
                    "scan_id": 1,
                    "timestamp": 1710000000,
                    "angle_deg": 30,
                }
            ]
        )

        is_valid, errors = validate_scan_df(df)

        self.assertFalse(is_valid)
        self.assertTrue(any("Missing scan columns" in err for err in errors))

    def test_validate_object_df_success(self):
        df = pd.DataFrame(
            [
                {
                    "timestamp": 1710000002,
                    "label": "person",
                    "confidence": 0.93,
                    "angle_deg": 90,
                    "distance_cm": 80,
                    "x": 0,
                    "y": 80,
                }
            ]
        )

        is_valid, errors = validate_object_df(df)

        self.assertTrue(is_valid)
        self.assertEqual(errors, [])

    def test_validate_object_df_missing_column(self):
        df = pd.DataFrame(
            [
                {
                    "timestamp": 1710000002,
                    "label": "person",
                    "confidence": 0.93,
                    "angle_deg": 90,
                    "distance_cm": 80,
                    "x": 0,
                }
            ]
        )

        is_valid, errors = validate_object_df(df)

        self.assertFalse(is_valid)
        self.assertTrue(any("Missing object columns" in err for err in errors))


if __name__ == "__main__":
    unittest.main()