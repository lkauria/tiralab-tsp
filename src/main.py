"""Christofides approximation algorithm"""
from algorithm.graph import build_distance_matrix
from algorithm.mst import prim_mst
from algorithm.matching import odd_degree_vertices, greedy_matching
from algorithm.multigraph import build_multigraph
from algorithm.euler import eulerian_circuit
from algorithm.hamilton import hamiltonian_circuit
from visualize import Visualizer
from data.nodes import nodes, CRS

dist = build_distance_matrix(nodes)
mst = prim_mst(dist)

odd = odd_degree_vertices(mst)
matching = greedy_matching(odd, dist)
print("\nPariton-asteiset solmut:", odd)
print("Paritus:", matching)

multigraph = build_multigraph(mst, matching, dist)

vis = Visualizer(nodes, crs=CRS)
vis.draw(1)
vis.draw(2, edges=vis.mst_edges(mst))
vis.draw(3, edges=vis.mst_edges(mst), highlight_edges=matching)

circuit = eulerian_circuit(multigraph)
vis.draw(4, edges=vis.circuit_edges(circuit))

tour = hamiltonian_circuit(circuit, dist)
vis.draw(5, edges=vis.circuit_edges(tour))
vis.draw("done", edges=vis.circuit_edges(tour))
