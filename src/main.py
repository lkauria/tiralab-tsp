"""Christofides approximation algorithm"""
from graph import build_distance_matrix
from mst import prim_mst
from matching import odd_degree_vertices, greedy_matching
from multigraph import build_multigraph
from euler import eulerian_circuit
from hamilton import hamiltonian_circuit
from visualize import draw, mst_edges, circuit_edges

# Finland's 20 largest cities in ETRS-TM35FIN (EPSG:3067), unit: meters
nodes = [
    (385700, 6672127),  # 0  Helsinki
    (370484, 6681550),  # 1  Espoo
    (328105, 6822741),  # 2  Tampere
    (391645, 6685318),  # 3  Vantaa
    (427883, 7210442),  # 4  Oulu
    (239915, 6710875),  # 5  Turku
    (435047, 6901544),  # 6  Jyväskylä
    (427483, 6761301),  # 7  Lahti
    (534573, 6973516),  # 8  Kuopio
    (223215, 6827301),  # 9  Pori
    (483708, 6748345),  # 10 Kouvola
    (641679, 6944054),  # 11 Joensuu
    (564238, 6770054),  # 12 Lappeenranta
    (362603, 6764338),  # 13 Hämeenlinna
    (228154, 7008146),  # 14 Vaasa
    (287372, 6969078),  # 15 Seinäjoki
    (443493, 7376218),  # 16 Rovaniemi
    (514285, 6839676),  # 17 Mikkeli
    (496701, 6703757),  # 18 Kotka
    (286704, 6699998),  # 19 Salo
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