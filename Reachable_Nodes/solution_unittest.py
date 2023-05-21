import unittest
from solution import reachableNodes

class ReachableNodesTestCase(unittest.TestCase):
    def test_reachable_nodes(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        start_node = 2
        expected = {0, 1, 2, 3, 4}
        self.assertEqual(reachableNodes(adj_list, start_node), expected)
    
    def test_reachable_nodes_alt(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        start_node = 3
        expected = {3, 4}
        self.assertEqual(reachableNodes(adj_list, start_node), expected)

    def test_reachable_nodes_empty_adj_list(self):
        adj_list = []
        start_node = 0
        expected = set()
        self.assertEqual(reachableNodes(adj_list, start_node), expected)

if __name__ == "__main__":
    unittest.main()
