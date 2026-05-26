"""Minimum spanning tree using Prim's algorithm."""


def prim_mst(dist):
    """
    Prim's algorithm for minimum spanning tree.

    Returns the MST as an adjacency list: mst[i] = list of (j, weight) neighbors.
    dist is a complete n x n -distance matrix.
    """
    n = len(dist)
    in_tree = [False] * n
    min_edge_cost = [float("inf")] * n
    parent = [-1] * n

    # Start from node 0
    min_edge_cost[0] = 0.0

    for _ in range(n):
        # Pick the cheapest node that is not yet picked up
        u = _pick_min(min_edge_cost, in_tree, n)
        in_tree[u] = True

        # Update costs for neighbors of u
        for v in range(n):
            if not in_tree[v] and dist[u][v] < min_edge_cost[v]:
                min_edge_cost[v] = dist[u][v]
                parent[v] = u

    mst = _build_adjacency_list(parent, dist, n)
    _print_mst(mst)
    return mst


def _print_mst(mst):
    print("\nMST vierekkäisyyslista:")
    for i, neighbors in enumerate(mst):
        naapurit = ", ".join(f"{j} (paino: {w:.1f})" for j, w in neighbors)
        print(f"  solmu {i}: [{naapurit}]")


def _pick_min(cost, in_tree, n):
    best = -1
    for i in range(n):
        if not in_tree[i]:
            if best == -1 or cost[i] < cost[best]:
                best = i
    return best


def _build_adjacency_list(parent, dist, n):
    mst = [[] for _ in range(n)]
    for v in range(1, n):
        u = parent[v]
        weight = dist[u][v]
        mst[u].append((v, weight))
        mst[v].append((u, weight))
    return mst
