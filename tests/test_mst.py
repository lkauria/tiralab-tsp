import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.mst import prim_mst


class TestPrimMst(unittest.TestCase):
    def test_edge_count(self):
        # MST with n nodes has n-1 edges
        dist = [
            [0, 1, 2],
            [1, 0, 1],
            [2, 1, 0],
        ]
        mst = prim_mst(dist)
        edge_count = sum(len(neighbors) for neighbors in mst) // 2
        self.assertEqual(edge_count, 2)

    def test_cheapest_edge_chosen(self):
        # Node 0 should connect to node 2 (weight 1), not node 1 (weight 10)
        dist = [
            [0, 10, 1],
            [10, 0, 1],
            [1,  1, 0],
        ]
        mst = prim_mst(dist)
        print("mst[0]:", mst[0])
        neighbors_of_node_0 = [j for j, _ in mst[0]]
        self.assertIn(2, neighbors_of_node_0)
        self.assertNotIn(1, neighbors_of_node_0)


    def test_empty_graph(self):
        self.assertEqual(prim_mst([]), [])


if __name__ == "__main__":
    unittest.main()
