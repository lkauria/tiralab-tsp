import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.hamilton import hamiltonian_circuit


class TestHamiltonianCircuit(unittest.TestCase):
    def test_each_node_visited_once(self):
        # Euler circuit visits node 0 twice, shortcutting should remove the duplicate
        circuit = [0, 1, 2, 0, 3, 0]
        dist = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ]
        tour = hamiltonian_circuit(circuit, dist)
        self.assertEqual(sorted(tour[:-1]), [0, 1, 2, 3])

    def test_tour_length_is_n_plus_one(self):
        # 4 nodes -> tour has 5 entries (last = first)
        circuit = [0, 1, 2, 0, 3, 0]
        dist = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ]
        tour = hamiltonian_circuit(circuit, dist)
        self.assertEqual(len(tour), 5)

    def test_tour_length_is_n_plus_one(self):
        # node 1 appears twice in the Euler circuit, shortcutting gives 4 unique nodes + closing node
        circuit = [0, 1, 2, 1, 3, 0]
        dist = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
        ]
        tour = hamiltonian_circuit(circuit, dist)
        self.assertEqual(len(tour), 5)

    def test_tour_starts_and_ends_at_same_node(self):
        circuit = [0, 1, 2, 0]
        dist = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ]
        tour = hamiltonian_circuit(circuit, dist)
        self.assertEqual(tour[0], tour[-1])


if __name__ == "__main__":
    unittest.main()
