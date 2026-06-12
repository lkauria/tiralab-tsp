import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from algorithm.graph import euclidean_distance, build_distance_matrix


class TestEuclideanDistance(unittest.TestCase):
    def test_diagonal_is_zero(self):
        self.assertEqual(euclidean_distance((3, 4), (3, 4)), 0.0)

    def test_known_distance(self):
        # test hypotenuse of a triangle
        self.assertAlmostEqual(euclidean_distance((0, 0), (3, 4)), 5.0)


class TestBuildDistanceMatrix(unittest.TestCase):
    def test_diagonal_is_zero(self):
        nodes = [(0, 0), (1, 0), (0, 1)]
        dist = build_distance_matrix(nodes)
        for i in range(len(nodes)):
            self.assertEqual(dist[i][i], 0.0)


if __name__ == "__main__":
    unittest.main()