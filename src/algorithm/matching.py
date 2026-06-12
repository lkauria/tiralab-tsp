"""Minimum weight perfect matching on odd-degree vertices."""


def odd_degree_vertices(mst):
    """Return list of vertex indices that have odd degree in the MST."""
    # mst[i] is the list of neighbors of node i
    # if the number of neighbors is odd, the node has odd degree
    return [i for i, neighbors in enumerate(mst) if len(neighbors) % 2 == 1]


def greedy_matching(odd_vertices, dist):
    """
    Greedy minimum weight perfect matching.

    Repeatedly picks the two closest unmatched vertices.
    Returns a list of (i, j) pairs.
    """
    # start with all odd-degree nodes unmatched
    unmatched = list(odd_vertices)
    matching = []

    while unmatched:
        # pick the first unmatched node
        u = unmatched.pop(0)
        # find the closest node to u among the remaining unmatched nodes
        best = min(unmatched, key=lambda v: dist[u][v])
        # remove best from unmatched — it is now paired with u
        unmatched.remove(best)
        # save the pair
        matching.append((u, best))
        print(f"  Valittu pari: solmu {u} ↔ solmu {best} (etäisyys: {dist[u][best]:.1f})")
        print(f"  Jäljellä parittomia: {unmatched}")

    return matching
