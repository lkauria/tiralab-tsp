"""Christofides approximation algorithm"""
from graph import build_distance_matrix
from mst import prim_mst
from visualize import draw, mst_edges

# Example nodes as x,y-coordinates
nodes = [
    (1, 4), (3, 1), (5, 3), (7, 2), (6, 6),
    (4, 8), (2, 7), (0, 5), (8, 5), (5, 0),
    (9, 1), (10, 6), (7, 9), (3, 10), (0, 9),
    (2, 2), (6, 0), (9, 8), (4, 5), (8, 3),
]

dist = build_distance_matrix(nodes)
mst = prim_mst(dist)

# Let's draw nodes and then MST based on distance matrix.
draw(nodes, title="Solmut")
draw(nodes, edges=mst_edges(mst), title="Minimivirityspuu (MST)")
