"""Eulerian circuit using Hierholzer's algorithm."""
import copy


def eulerian_circuit(multigraph):
    """
    Find an Eulerian circuit in the multigraph (usinng Hierholzer's algorithm).
    Returns a list of node indices representing the circuit.
    """
    if not multigraph:
        return []

    # deep copy so we can remove edges as we traverse without changing the original
    graph = copy.deepcopy(multigraph)

    # stack keeps track of where we currently are, start from node 0
    stack = [0]
    # circuit will hold the final order of visited nodes
    circuit = []

    # keep going as long as there are nodes in the stack
    while stack:
        # look at the top of the stack without removing it
        v = stack[-1]

        if graph[v]:
            # node v still has unused edges — pick one
            u, _ = graph[v].pop()
            # remove the same edge from the other direction (undirected graph)
            graph[u].remove((v, _))
            # move to node u by pushing it onto the stack
            stack.append(u)
            print(f"  Siirrytään: {v} -> {u},  pino: {stack}")
        else:
            # node v has no more edges, it is done, add it to the circuit
            circuit.append(stack.pop())
            print(f"  Solmu {v} valmis, lisätään kierrokseen, kierros tähän asti: {circuit}")

    print("\nEuler-kierros:", circuit)
    return circuit
