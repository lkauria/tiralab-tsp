import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.matching import odd_degree_vertices, greedy_matching


class TestOddDegreeVertices(unittest.TestCase):
    def test_correct_nodes_returned(self):
        # chain 0--1--2: node 1 connects to two others (even), nodes 0 and 2 connect to one (odd)
        mst = [
            [(1, 1.0)],           # node 0: degree 1
            [(0, 1.0), (2, 1.0)], # node 1: degree 2
            [(1, 1.0)],           # node 2: degree 1
        ]
        self.assertEqual(odd_degree_vertices(mst), [0, 2])

    def test_empty_graph(self):
        self.assertEqual(odd_degree_vertices([]), [])

    def test_single_node(self):
        # one node with no edges has degree 0 (even), so no odd-degree vertices
        self.assertEqual(odd_degree_vertices([[]]), [])

    def test_count_is_even(self):
        # odd-degree vertex count is always even (mathematical fact)
        mst = [
            [(1, 1.0)],
            [(0, 1.0), (2, 1.0)],
            [(1, 1.0)],
        ]
        odd = odd_degree_vertices(mst)
        self.assertEqual(len(odd) % 2, 0)


class TestGreedyMatching(unittest.TestCase):
    def test_each_node_appears_once(self):
        # nodes 0 and 2 are closest, 1 and 3 are closest
        dist = [
            [0, 10, 1, 10],
            [10, 0, 10, 1],
            [1, 10, 0, 10],
            [10, 1, 10, 0],
        ]
        odd = [0, 1, 2, 3]
        matching = greedy_matching(odd, dist)
        paired = [node for pair in matching for node in pair]
        self.assertEqual(sorted(paired), [0, 1, 2, 3])

    def test_closest_pair_chosen(self):
        # node 0 is very close to node 2, so they should be paired
        dist = [
            [0, 100, 1, 100],
            [100, 0, 100, 1],
            [1, 100, 0, 100],
            [100, 1, 100, 0],
        ]
        odd = [0, 1, 2, 3]
        matching = greedy_matching(odd, dist)
        self.assertIn((0, 2), matching)


if __name__ == "__main__":
    unittest.main()
