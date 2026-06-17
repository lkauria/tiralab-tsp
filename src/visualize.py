"""Visualization with matplotlib."""
import matplotlib.pyplot as plt


TOTAL_STEPS = 5
MANUAL = False  # set True to step through images manually by closing each window

STEP_TITLES = {
    1: "Syöte",
    2: "Minimivirityspuu (MST)",
    3: "MST + paritus",
    4: "Euler-kierros",
    5: "Hamiltonin kierros",
}


def _plot_normal_edges(ax, nodes, edges):
    for i, j in edges:
        ax.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]],
                color="gray", linewidth=1.5, zorder=1)


def _plot_highlight_edges(ax, nodes, edges):
    for i, j in edges:
        ax.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]],
                color="crimson", linewidth=2, linestyle="--", zorder=1)


def _plot_nodes(ax, nodes):
    xs = [n[0] for n in nodes]
    ys = [n[1] for n in nodes]
    ax.scatter(xs, ys, color="steelblue", s=40, zorder=2)
    for i, (x, y) in enumerate(nodes):
        ax.annotate(str(i), (x, y), textcoords="offset points", xytext=(6, 6), fontsize=9)


class Visualizer:
    """Draws algorithm steps with matplotlib."""

    def __init__(self, nodes, crs=None):
        self.nodes = nodes
        self.crs = crs

    def draw(self, step, edges=None, highlight_edges=None):
        """
        Draw one step of the algorithm.

        step: int 1-5 for a numbered step, or "done" for the final Valmis! view
        edges: list of (i, j) index pairs to draw as lines
        highlight_edges: list of (i, j) pairs drawn in crimson (e.g. matching edges)
        """
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.set_aspect("equal")

        fig.suptitle("Christofidesin algoritmi", fontsize=13, fontweight="bold")

        if step == "done":
            ax.set_title("Valmis!", fontsize=13, color="green", fontweight="bold")
        else:
            ax.set_title(f"{STEP_TITLES[step]}  {step}/{TOTAL_STEPS}", fontsize=11)

        if self.crs:
            ax.annotate(
                self.crs, xy=(0.01, 0.01), xycoords="axes fraction",
                fontsize=8, color="gray"
            )

        if edges:
            _plot_normal_edges(ax, self.nodes, edges)

        if highlight_edges:
            _plot_highlight_edges(ax, self.nodes, highlight_edges)

        _plot_nodes(ax, self.nodes)

        plt.tight_layout()
        if step == "done" or MANUAL:
            plt.show()
        else:
            plt.pause(2)
            plt.close()

    @staticmethod
    def circuit_edges(circuit):
        """Return circuit as (i, j) pairs from consecutive nodes."""
        return [(circuit[k], circuit[k + 1]) for k in range(len(circuit) - 1)]

    @staticmethod
    def mst_edges(mst):
        """Return MST edges as (i, j) pairs, each edge only once."""
        edges = []
        for i, neighbors in enumerate(mst):
            for j, _ in neighbors:
                if i < j:
                    edges.append((i, j))
        return edges
