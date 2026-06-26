"""Hamiltonian circuit by shortcutting the Eulerian circuit."""


def hamiltonian_circuit(circuit, dist):
    """
    Shortcut the Eulerian circuit into a Hamiltonian circuit.

    Skips nodes already visited. Each node appears exactly once.
    The first node is added again at the end to close the tour.
    """
    visited = set()
    tour = []

    for node in circuit:
        if node not in visited:
            # first time seeing this node, add it to the tour
            visited.add(node)
            tour.append(node)
            print(f"  Lisätään solmu {node} kierrokseen")
        else:
            print(f"  Ohitetaan solmu {node} (jo vierailtu)")

    # close the tour by returning to the starting node
    tour.append(tour[0])

    cost = _tour_cost(tour, dist)
    print("\nHamiltonin kierros:", tour)
    print(f"Kierroksen kokonaispituus: {cost:.2f}")
    return tour


def _tour_cost(tour, dist):
    """Calculate total distance of the tour."""
    return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
