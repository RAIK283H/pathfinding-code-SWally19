import math
import sys
import unittest

import pathing
import permutation
import f_w


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

    # Pathing tests

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

    def test_find_min_middle(self):
        expected = 2
        actual = pathing.find_min([0, 45, 2, 3, 70], [True, False, False, False, False])
        self.assertEqual(actual, expected)

    def test_find_min_first(self):
        expected = 0
        actual = pathing.find_min([0, 45, 2, 3, 70], [False, False, False, False, False])
        self.assertEqual(actual, expected)

    def test_find_min_last(self):
        expected = 4
        actual = pathing.find_min([60, 45, 2, 3, 1], [False, False, True, False, False])
        self.assertEqual(actual, expected)

    def test_dijkstra(self):
        graph = [
            [(45, 45), [1]],
            [(45, 500), [0, 2]],
            [(45, 100), [1, 3]],
            [(45, 10), [2]],
        ]
        
        expected = [0, 1, 2, 3]
        actual = pathing.dijkstra_helper(0, 3, graph, False)
        self.assertEqual(actual, expected)

    def test_a_star(self):
        graph = [
            [(45, 200), [1]],
            [(45, 45), [0, 2]],
            [(45, 500), [1, 3]],
            [(45, 100), [2]],
        ]
        
        expected = [0, 1, 2, 3]
        actual = pathing.dijkstra_helper(0, 3, graph, True)
        self.assertEqual(actual, expected)

    def test_get_path_from_parents(self):
        parents = [0, 0, 1, 2]
        expected = [0, 1, 2, 3]
        actual = pathing.get_path_from_parents(parents, 0, 3)
        self.assertEqual(actual, expected)

    # Permutation tests    
    
    def test_initialize_one(self):
        expected = [-1]
        actual = permutation.initialize(1)
        self.assertEqual(actual, expected)

    def test_initialize_four(self):
        expected = [-1, -2, -3, -4]
        actual = permutation.initialize(4)
        self.assertEqual(actual, expected)

    def test_find_largest_mobile_none(self):
        sequence = [-4, -3, -2, -1]
        expected = 0
        actual = permutation.find_largest_mobile(sequence)
        self.assertEqual(actual, expected)
    
    def test_find_largest_mobile_left(self):
        sequence = [3, -4, -2, -1]
        expected = -4
        actual = permutation.find_largest_mobile(sequence)
        self.assertEqual(actual, expected)

    def test_find_largest_mobile_right(self):
        sequence = [3, 4, -2, -1]
        expected = 4
        actual = permutation.find_largest_mobile(sequence)
        self.assertEqual(actual, expected)

    def test_swap_elements_left_edge(self):
        sequence = [1, 2, 3, -4]
        expected = [1, 2, -4, 3]
        actual = permutation.swap_elements(sequence, 3)
        self.assertEqual(actual, expected)

    def test_swap_elements_right_edge(self):
        sequence = [4, 2, 3, -1]
        expected = [2, 4, 3, -1]
        actual = permutation.swap_elements(sequence, 0)
        self.assertEqual(actual, expected)

    def test_swap_elements_middle(self):
        sequence = [-1, 2, -3, 4]
        expected = [-1, -3, 2, 4]
        actual = permutation.swap_elements(sequence, 2)
        self.assertEqual(actual, expected)

    def test_swap_direction_negative_all(self):
        sequence = [2, -1, -3, 4]
        expected = [-2, -1, 3, -4]
        actual = permutation.swap_direction(sequence, -1)
        self.assertEqual(actual, expected)
    
    def test_swap_direction_positive_one(self):
        sequence = [2, -1, 3, 4]
        expected = [2, -1, 3, -4]
        actual = permutation.swap_direction(sequence, 3)
        self.assertEqual(actual, expected)

    def test_sequence_to_store_all(self):
        sequence = [-1, -2, -3, -4]
        expected = [1, 2, 3, 4]
        actual = permutation.sequence_to_store(sequence)
        self.assertEqual(actual, expected)

    def test_sequence_to_store_none(self):
        sequence = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        actual = permutation.sequence_to_store(sequence)
        self.assertEqual(actual, expected)

    def test_sequence_to_store_one(self):
        sequence = [1, 2, -3, 4]
        expected = [1, 2, 3, 4]
        actual = permutation.sequence_to_store(sequence)
        self.assertEqual(actual, expected)

    def test_get_permutations(self):
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual = permutation.get_permutations(3)
        self.assertEqual(actual, expected)

    def test_is_valid_path_false(self):
        graph = [
                [(900, 45), [1, 2]],
                [(100, 45), [0]],
                [(600, 45), [0]],
            ]
            
        path = [2, 1, 0]
        self.assertFalse(permutation.is_valid_path(path, graph))

    def test_is_valid_path_true(self):
        graph = [
                [(900, 45), [1, 2]],
                [(100, 45), [0, 2]],
                [(600, 45), [0, 1]],
            ]
            
        path = [2, 0, 1]
        self.assertTrue(permutation.is_valid_path(path, graph))

    def test_get_cycles_none(self):
        graph = [
                [(900, 45), [1, 2]],
                [(100, 45), [0]],
                [(600, 45), [0]],
            ]
            
        self.assertFalse(permutation.get_cycles(graph))

    def test_get_cycles_true(self):
        graph = [
            # start
                [(900, 45), [1]],
                [(900, 45), [0, 2, 3]],
                [(100, 45), [1, 3]],
                [(600, 45), [1, 2, 4]],
            # end
                [(600, 45), [3]],
            ]
            
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual = permutation.get_cycles(graph)
        self.assertEqual(actual, expected)

    # Floyd Warshall tests
    def test_create_matrix(self):
        graph = [ [(0, 0),[1, 2]],
                 [(0, 50), [0]],
                 [(0, 100), [0]]
        ]
        expected = [[math.inf, 50, 100],
                    [50, math.inf, math.inf],
                    [100, math.inf, math.inf]]
        actual = f_w.create_matrix(graph)
        self.assertEqual(actual, expected)

    def test_get_path_from_parent_matrix(self):
        parent = [[math.inf, math.inf, 1, 2, 3],
                  [math.inf, math.inf, math.inf, 2, 3],
                  [math.inf, math.inf, math.inf, math.inf, 3]]
        actual = f_w.get_path_from_parent_matrix(parent, 0, 4)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)

    def test_get_parents(self):
        matrix = [[math.inf, 2, math.inf, math.inf, 10],
                  [math.inf, math.inf, 1, math.inf, 6],
                  [math.inf, math.inf, math.inf, 1, 3],
                  [math.inf, math.inf, math.inf, math.inf, 1],
                  [math.inf, math.inf, math.inf, math.inf, math.inf]]
        actual = f_w.get_parents(matrix, 5)
        expected = [[math.inf, math.inf, 1, 2, 3],
                    [math.inf, math.inf, math.inf, 2, 3],
                    [math.inf, math.inf, math.inf, math.inf, 3],
                    [math.inf, math.inf, math.inf, math.inf, math.inf],
                    [math.inf, math.inf, math.inf, math.inf, math.inf]]
        self.assertEqual(actual, expected)

    def test_fw(self):
        graph = [
            [(45, 45), [1]],
            [(45, 500), [0, 2]],
            [(45, 100), [1, 3]],
            [(45, 10), [2]],
        ]
        
        expected = [0, 1, 2, 3]
        actual = f_w.floyd_warshall_helper(0, 3, graph)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
