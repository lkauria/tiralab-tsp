"""Combine MST and matching into a multigraph."""
import copy


def build_multigraph(mst, matching, dist):
    """
    Combine MST edges and matching edges into a multigraph.

    Returns an adjacency list where each node can have multiple edges
    to the same neighbor (hence multigraph).
    """
    # deep copy so we don't modify the original MST
    multigraph = copy.deepcopy(mst)

    # add each matching edge to both endpoints
    for u, v in matching:
        multigraph[u].append((v, dist[u][v]))
        multigraph[v].append((u, dist[u][v]))

    _print_multigraph(multigraph)
    return multigraph


def _print_multigraph(multigraph):
    print("\nMultigraafi (vierekkäisyyslista):")
    for i, neighbors in enumerate(multigraph):
        naapurit = ", ".join(f"{j} (paino: {w:.1f})" for j, w in neighbors)
        print(f"  solmu {i}: [{naapurit}]")
