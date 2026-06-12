"""Building a graph from coordinates."""
import math


def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def build_distance_matrix(nodes):
    """Build a distance matrix from a list of (x, y) coordinates."""
    n = len(nodes)
    print(f"Rakennetaan etäisyysmatriisi {n} solmulle.")
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = euclidean_distance(nodes[i], nodes[j])
    return dist
