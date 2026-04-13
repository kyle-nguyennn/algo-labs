from graph.graph import Graph
from graph.types import Edge
from graph.dfs import DFS

"""
You are given a graph G=(V, E) and an MST T of G.
The weight of an edge e, which is part of T, is doubled. All other edges keep their original weight.
Design an algorithm that outputs an MST in adjacency list format for the graph G with the updated weights.
Notes:
    - The final MST need not be distinct from T.
    - Building an MST from scratch will receive little credit!
"""
def TEdgeDoubled(
    G: Graph, T: Graph, weights: dict[Edge, int | float], e: Edge
) -> Graph:
    # Construct T' = T - {e}
    T.remove_edge(*e)

    # Run DFS to identify the two components of T', called A and B
    result = DFS(T)
    comp_a = result.ccnum[e[0]]
    A = {v for v in T.nodes() if result.ccnum[v] == comp_a}

    # Find the minimum weight crossing edge f in G that connects A and B with respect to w'
    min_edge = None
    min_weight = float('inf')
    for (u, v) in G.edges():
        if (u in A) != (v in A):  # crosses the cut
            if weights[(u, v)] < min_weight:
                min_weight = weights[(u, v)]
                min_edge = (u, v)

    # T'' = T' U {f} is the desired MST for G with the updated weights
    T.add_edge(*min_edge)
    return T
    
