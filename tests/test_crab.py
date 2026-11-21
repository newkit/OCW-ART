"""The no-token day's ASCII crab (ocwart/crab.py, ART-PROJECT §4.1)."""

import unittest

from ocwart import crab


class CrabTest(unittest.TestCase):
    def test_every_pose_lines_up(self):
        for name in ("_UP", "_DOWN", "_OUT", "_SHRUG"):
            rows = crab.pose(getattr(crab, name))
            self.assertEqual(len(rows), 11, name)
            self.assertEqual({len(r) for r in rows}, {30}, name)

    def test_the_pockets_turn_white(self):
        out = crab.pose(crab._OUT)
        self.assertTrue(any(c == crab.LINING for row in out for _, c in row))
        self.assertFalse(any(c == crab.LINING for row in crab.pose(crab._UP) for _, c in row))

    def test_layers_hold_no_tag_inside_a_line(self):
        """A colour tag right after a backslash would be escaped by libass."""
        for t in (1.0, 9.6, 12.4, 18.0):
            g, alpha = crab.scene(t)
            for tags, text in crab.ass_layers(g, alpha):
                self.assertNotIn("{", text)
                lines = text.split("\\N")
                self.assertEqual(len(lines), crab.ROWS)

    def test_the_counter_runs_down_to_zero(self):
        self.assertEqual(crab.counter_value(0.0, 1_590_924_433), 1_590_924_433)
        self.assertLess(crab.counter_value(3.0, 1_590_924_433), 1_590_924_433)
        self.assertEqual(crab.counter_value(5.0, 1_590_924_433), 0)
        self.assertEqual(crab.counter_value(20.0, 1_590_924_433), 0)

    def test_deterministic_with_moth_and_dust(self):
        a, _ = crab.scene(10.0)
        b, _ = crab.scene(10.0)
        self.assertEqual(a, b)
        chars = {c for row in a for _, c in row}
        self.assertIn(crab.MOTH, chars)
        self.assertIn(crab.DUST, chars)


if __name__ == "__main__":
    unittest.main()
