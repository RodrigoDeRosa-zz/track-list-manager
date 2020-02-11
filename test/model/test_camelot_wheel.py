import unittest

from parameterized import parameterized

from raver.model.camelot_wheel import CamelotWheel


class TestCamelotWheel(unittest.TestCase):

    @parameterized.expand(
        [
            ['1A', '1B', True],
            ['1A', '12B', False],
            ['1A', '2A', True],
            ['12A', '1A', True],
            ['7A', '7B', True],
            ['7A', '9B', False],
            ['8B', '9B', True],
            ['8B', '11B', False]
        ]
    )
    def test_harmonic_keys(self, key1, key2, expected_result):
        self.assertEqual(expected_result, CamelotWheel.keys_are_harmonic(key1, key2))


if __name__ == '__main__':
    unittest.main()
