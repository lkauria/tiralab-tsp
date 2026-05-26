"""Visualization with matplotlib."""
import matplotlib.pyplot as plt


def draw(nodes, edges=None, title="TSP", node_color="steelblue", edge_color="gray"):
    """
    Draw nodes and optional edges.

    nodes: list of (x, y) tuples
    edges: list of (i, j) index pairs to draw as lines
    """
    _, ax = plt.subplots(figsize=(7, 7))
    ax.set_title(title)
    ax.set_aspect("equal")

    if edges:
        for i, j in edges:
            x_vals = [nodes[i][0], nodes[j][0]]
            y_vals = [nodes[i][1], nodes[j][1]]
            ax.plot(x_vals, y_vals, color=edge_color, linewidth=1.5, zorder=1)

    xs = [n[0] for n in nodes]
    ys = [n[1] for n in nodes]
    ax.scatter(xs, ys, color=node_color, s=80, zorder=2)

    for i, (x, y) in enumerate(nodes):
        ax.annotate(str(i), (x, y), textcoords="offset points",
                    xytext=(6, 6), fontsize=9)

    plt.tight_layout()
    plt.show()


def mst_edges(mst):
    """Return MST edges as (i, j) pairs, each edge only once."""
    edges = []
    for i, neighbors in enumerate(mst):
        for j, _ in neighbors:
            if i < j:
                edges.append((i, j))
    return edges
