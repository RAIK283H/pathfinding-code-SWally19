import math
import unittest

import pathing


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_dfs(self):
        graph = [
            [
                [(900, 45), [17, 21, 22]],
                [(70, 350), [2, 7, 19, 20]],
                [(140, 420), [1, 5, 9, 10, 20]],
                [(210, 70), [6, 8, 11, 22]],
                [(210, 210), [6, 7, 11, 12, 20]],
                [(210, 490), [2, 10, 21]],
                [(280, 140), [3, 4, 11, 20]],
                [(280, 280), [1, 4, 9, 12, 20]],
                [(350, 70), [3, 11]],
                [(350, 350), [2, 7, 10, 12, 13, 15]],
                [(350, 490), [2, 5, 9, 13, 14, 15]],
                [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
                [(420, 280), [4, 7, 9, 11, 15, 17]],
                [(420, 420), [9, 10, 15]],
                [(490, 490), [10, 18, 15]],
                [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
                [(630, 70), [11, 17]],
                [(630, 210), [11, 12, 15, 16, 18, 0]],
                [(700, 420), [14, 15, 17, 23]],
                [(70, 500), [1, 21]],
                [(70, 210), [1, 2, 4, 6, 7, 22]],
                [(450, 700), [5, 19, 0, 23]],
                [(45, 45), [0, 3, 20]],
                [(1225, 700), [18, 21]]
            ]
        ]
        actual = pathing.dfs_helper(0, 23, graph[0])
        expected = [0, 22, 20, 7, 12, 15, 18, 23]
        self.assertEqual(actual, expected)

    def test_bfs(self):
        graph = [
            [
                [(900, 45), [17, 21, 22]],
                [(70, 350), [2, 7, 19, 20]],
                [(140, 420), [1, 5, 9, 10, 20]],
                [(210, 70), [6, 8, 11, 22]],
                [(210, 210), [6, 7, 11, 12, 20]],
                [(210, 490), [2, 10, 21]],
                [(280, 140), [3, 4, 11, 20]],
                [(280, 280), [1, 4, 9, 12, 20]],
                [(350, 70), [3, 11]],
                [(350, 350), [2, 7, 10, 12, 13, 15]],
                [(350, 490), [2, 5, 9, 13, 14, 15]],
                [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
                [(420, 280), [4, 7, 9, 11, 15, 17]],
                [(420, 420), [9, 10, 15]],
                [(490, 490), [10, 18, 15]],
                [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
                [(630, 70), [11, 17]],
                [(630, 210), [11, 12, 15, 16, 18, 0]],
                [(700, 420), [14, 15, 17, 23]],
                [(70, 500), [1, 21]],
                [(70, 210), [1, 2, 4, 6, 7, 22]],
                [(450, 700), [5, 19, 0, 23]],
                [(45, 45), [0, 3, 20]],
                [(1225, 700), [18, 21]]
            ]
        ]
        actual = pathing.bfs_helper(0, 23, graph[0])
        expected = [0, 21, 23]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
