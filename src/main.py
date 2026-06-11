"""Christofides approximation algorithm"""
from graph import build_distance_matrix
from mst import prim_mst
from matching import odd_degree_vertices, greedy_matching
from multigraph import build_multigraph
from euler import eulerian_circuit
from hamilton import hamiltonian_circuit
from visualize import draw, mst_edges, circuit_edges

# Finland's 20 largest cities as (longitude, latitude)
nodes = [
    (24.94, 60.17),  # 0  Helsinki
    (24.66, 60.25),  # 1  Espoo
    (23.77, 61.50),  # 2  Tampere
    (25.04, 60.29),  # 3  Vantaa
    (25.47, 65.01),  # 4  Oulu
    (22.27, 60.45),  # 5  Turku
    (25.75, 62.24),  # 6  Jyväskylä
    (25.66, 60.98),  # 7  Lahti
    (27.68, 62.89),  # 8  Kuopio
    (21.80, 61.48),  # 9  Pori
    (26.70, 60.87),  # 10 Kouvola
    (29.76, 62.60),  # 11 Joensuu
    (28.19, 61.06),  # 12 Lappeenranta
    (24.46, 60.99),  # 13 Hämeenlinna
    (21.61, 63.10),  # 14 Vaasa
    (22.83, 62.79),  # 15 Seinäjoki
    (25.73, 66.50),  # 16 Rovaniemi
    (27.27, 61.69),  # 17 Mikkeli
    (26.94, 60.47),  # 18 Kotka
    (23.13, 60.38),  # 19 Salo
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


circuit = eulerian_circuit(multigraph)
draw(nodes, edges=circuit_edges(circuit), title="Euler-kierros")

tour = hamiltonian_circuit(circuit, dist)
draw(nodes, edges=circuit_edges(tour), title="Hamiltonin kierros")