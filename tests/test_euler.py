import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.euler import eulerian_circuit


class TestEulerianCircuit(unittest.TestCase):
    def test_starts_and_ends_at_same_node(self):
        # triangle 0--1--2--0, each node has degree 2 (even)
        multigraph = [
            [(1, 1.0), (2, 1.0)],
            [(0, 1.0), (2, 1.0)],
            [(1, 1.0), (0, 1.0)],
        ]
        circuit = eulerian_circuit(multigraph)
        self.assertEqual(circuit[0], circuit[-1])  # first and last node must be the same

    def test_all_nodes_visited(self):
        # triangle 0--1--2--0
        multigraph = [
            [(1, 1.0), (2, 1.0)],
            [(0, 1.0), (2, 1.0)],
            [(1, 1.0), (0, 1.0)],
        ]
        circuit = eulerian_circuit(multigraph)
        self.assertEqual(set(circuit), {0, 1, 2})

    def test_empty_graph(self):
        self.assertEqual(eulerian_circuit([]), [])

    def test_single_node(self):
        # one node with no edges, circuit is just that node
        self.assertEqual(eulerian_circuit([[]]), [0])


if __name__ == "__main__":
    unittest.main()
