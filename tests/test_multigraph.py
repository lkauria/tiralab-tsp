import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.multigraph import build_multigraph


class TestBuildMultigraph(unittest.TestCase):
    def test_multigraph_has_more_edges_than_mst(self):
        # chain 0--1--2, matching adds edge (0, 2)
        mst = [
            [(1, 1.0)],
            [(0, 1.0), (2, 1.0)],
            [(1, 1.0)],
        ]
        dist = [
            [0, 1, 2],
            [1, 0, 1],
            [2, 1, 0],
        ]
        matching = [(0, 2)]
        multigraph = build_multigraph(mst, matching, dist)

        mst_edge_count = sum(len(n) for n in mst) // 2
        mg_edge_count = sum(len(n) for n in multigraph) // 2
        self.assertGreater(mg_edge_count, mst_edge_count)

    def test_all_nodes_have_even_degree(self):
        # Euler circuit requires every node to have even degree
        mst = [
            [(1, 1.0)],
            [(0, 1.0), (2, 1.0)],
            [(1, 1.0)],
        ]
        dist = [
            [0, 1, 2],
            [1, 0, 1],
            [2, 1, 0],
        ]
        matching = [(0, 2)]
        multigraph = build_multigraph(mst, matching, dist)

        for i, neighbors in enumerate(multigraph):
            self.assertEqual(len(neighbors) % 2, 0, f"node {i} has odd degree")


if __name__ == "__main__":
    unittest.main()
