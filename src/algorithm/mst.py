"""Minimum spanning tree using Prim's algorithm."""


def prim_mst(dist):
    """
    Prim's algorithm for minimum spanning tree.

    Returns the MST as an adjacency list: mst[i] = list of (j, weight) neighbors.
    dist is a complete n x n -distance matrix.
    """
    n = len(dist)
    if n == 0:
        return []

    # tracks which nodes are already in the tree
    in_tree = [False] * n
    # cheapest known edge to reach each node; infinity means not yet reachable
    min_edge_cost = [float("inf")] * n
    # remembers which node each node was connected from when added to the tree
    parent = [-1] * n

    # node 0 is the starting point, costs nothing to add
    min_edge_cost[0] = 0.0

    for _ in range(n):
        # pick the cheapest node not yet in the tree
        u = _pick_min(min_edge_cost, in_tree, n)
        in_tree[u] = True

        # check if adding u reveals a cheaper path to any other node
        for v in range(n):
            if not in_tree[v] and dist[u][v] < min_edge_cost[v]:
                # found a cheaper way to reach v, update cost and remember the connection
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
    # -1 means no candidate found yet
    best = -1
    for i in range(n):
        if not in_tree[i]:
            # accept the first candidate unconditionally, then keep the cheaper one
            if best == -1 or cost[i] < cost[best]:
                print(f"  solmu {i} on halvempi (hinta: {cost[i]:.1f}) kuin aiempi paras solmu {best}")
                best = i
    print(f"  valitaan solmu {best} puuhun")
    return best


def _build_adjacency_list(parent, dist, n):
    # one empty list per node
    mst = [[] for _ in range(n)]
    # start from 1 because node 0 is the root and has no parent
    for v in range(1, n):
        u = parent[v]
        weight = dist[u][v]
        # add edge in both directions since the graph is undirected
        mst[u].append((v, weight))
        mst[v].append((u, weight))
    return mst
