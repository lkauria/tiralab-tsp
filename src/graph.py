import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def build_distance_matrix(nodes):
    # Build a distance matrix from a list of x,y-coordinates.
    n = len(nodes)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = euclidean_distance(nodes[i], nodes[j])
    _print_distance_matrix(dist, n)
    return dist


def _print_distance_matrix(dist, n):
    # For testing purposes (delete this later)
    print("Etäisyysmatriisi:")
    header = "     " + "  ".join(f"{j:5}" for j in range(n))
    print(header)
    for i in range(n):
        row = "  ".join(f"{dist[i][j]:5.1f}" for j in range(n))
        print(f"{i:3}  {row}")
