import unittest
import numpy as np
from solution import adMatrixToAdList

class TestAdMatrixToAdList(unittest.TestCase):
    def test_empty_matrix(self):
        adj_mat = []
        expected_output = []
        self.assertEqual(adMatrixToAdList(adj_mat), expected_output)

    def test_adjacency_matrix(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        expected_output = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(adMatrixToAdList(adj_mat), expected_output)

    def test_all_zeros_matrix(self):
        adj_mat = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        expected_output = [[], [], [], [], [], []]
        self.assertEqual(adMatrixToAdList(adj_mat), expected_output)

    def test_identity_matrix(self):
        adj_mat = [[1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1]]
        expected_output = [[0], [1], [2], [3], [4], [5]]
        self.assertEqual(adMatrixToAdList(adj_mat), expected_output)

if __name__ == "__main__":
    unittest.main()
