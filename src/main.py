"""Christofides approximation algorithm"""
from graph import build_distance_matrix
from mst import prim_mst
from matching import odd_degree_vertices, greedy_matching
from multigraph import build_multigraph
from euler import eulerian_circuit
from hamilton import hamiltonian_circuit
from visualize import draw, mst_edges, circuit_edges
from data.nodes import nodes, CRS

dist = build_distance_matrix(nodes)
mst = prim_mst(dist)

odd = odd_degree_vertices(mst)
matching = greedy_matching(odd, dist)
print("\nPariton-asteiset solmut:", odd)
print("Paritus:", matching)

multigraph = build_multigraph(mst, matching, dist)

draw(nodes, crs=CRS, title="Solmut")
draw(nodes, edges=mst_edges(mst), crs=CRS, title="Minimivirityspuu (MST)")
draw(nodes, edges=mst_edges(mst), highlight_edges=matching, crs=CRS, title="MST + paritus")


circuit = eulerian_circuit(multigraph)
draw(nodes, edges=circuit_edges(circuit), crs=CRS, title="Euler-kierros")

tour = hamiltonian_circuit(circuit, dist)
draw(nodes, edges=circuit_edges(tour), crs=CRS, title="Hamiltonin kierros")