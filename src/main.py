"""Christofides approximation algorithm"""
from graph import build_distance_matrix
from mst import prim_mst
from matching import odd_degree_vertices, greedy_matching
from multigraph import build_multigraph
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

odd = odd_degree_vertices(mst)
matching = greedy_matching(odd, dist)
print("\nPariton-asteiset solmut:", odd)
print("Paritus:", matching)

multigraph = build_multigraph(mst, matching, dist)

draw(nodes, title="Solmut")
draw(nodes, edges=mst_edges(mst), title="Minimivirityspuu (MST)")
draw(nodes, edges=mst_edges(mst), highlight_edges=matching, title="MST + paritus")

print("Solmun 13 aste MST:ssä:", len(mst[13])) 