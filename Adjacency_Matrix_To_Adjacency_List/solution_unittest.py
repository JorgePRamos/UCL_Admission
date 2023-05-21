import unittest
import numpy as np
from solution import adMatrixToAdList

class TestAdMatrixToAdList(unittest.TestCase):

    def test_adjacency_matrix(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        expected = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(adMatrixToAdList(adj_mat), expected)

    def test_all_zeros_matrix(self):
        adj_mat = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        expected = [[], [], [], [], [], []]
        self.assertEqual(adMatrixToAdList(adj_mat), expected)

    def test_identity_matrix(self):
        adj_mat = [[1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1]]
        expected = [[0], [1], [2], [3], [4], [5]]
        self.assertEqual(adMatrixToAdList(adj_mat), expected)
        
    def test_empty_matrix(self):
        adj_mat = []
        expected = []
        self.assertEqual(adMatrixToAdList(adj_mat), expected)

if __name__ == "__main__":
    unittest.main()
