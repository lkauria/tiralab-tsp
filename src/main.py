"""Christofides approximation algorithm"""
from algorithm.graph import build_distance_matrix
from algorithm.mst import prim_mst
from algorithm.matching import odd_degree_vertices, greedy_matching
from algorithm.multigraph import build_multigraph
from algorithm.euler import eulerian_circuit
from algorithm.hamilton import hamiltonian_circuit
from visualize import draw, mst_edges, circuit_edges
from data.nodes import nodes, CRS

dist = build_distance_matrix(nodes)
mst = prim_mst(dist)

odd = odd_degree_vertices(mst)
matching = greedy_matching(odd, dist)
print("\nPariton-asteiset solmut:", odd)
print("Paritus:", matching)

multigraph = build_multigraph(mst, matching, dist)

draw(nodes, crs=CRS, title="Syöte", step=1)
draw(nodes, edges=mst_edges(mst), crs=CRS, title="Minimivirityspuu (MST)", step=2)
draw(nodes, edges=mst_edges(mst), highlight_edges=matching, crs=CRS, title="MST + paritus", step=3)

circuit = eulerian_circuit(multigraph)
draw(nodes, edges=circuit_edges(circuit), crs=CRS, title="Euler-kierros", step=4)

tour = hamiltonian_circuit(circuit, dist)
draw(nodes, edges=circuit_edges(tour), crs=CRS, title="Hamiltonin kierros", step=5)
draw(nodes, edges=circuit_edges(tour), crs=CRS, title="Hamiltonin kierros", done=True, last=True)
