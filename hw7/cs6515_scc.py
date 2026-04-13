from typing import NamedTuple

from graph.digraph import DiGraph, Node

"""
Build-A-Box: Strongly Connected Components
To make the ideas presented in the lectures more concrete, your task is to implement the Depth First Search
(DFS)-based Strongly Connected Components (SCC) algorithm.
To ensure the implementation matches the algorithm presented in the course, both DFS and SCC functions
may be independently tested to ensure completeness and correctness.
Your input will come in the form of a directed graph in adjacency list format. The interface available for
interacting with the adjacency list is provided as source code.
Notes:
    - While edges are stored unordered, your DFS implementation must process them deterministically in
the same fashion as the lectures present.
    - Named Tuples have been provided to help manage the multiple outputs of these algorithms. Their
definitions must not be modified.
Provide your code for implementing this algorithm in cs6515_scc.py
"""
class DFSOutput(NamedTuple):
    ccnum: dict[Node, int]
    prev: dict[Node, Node | None]
    pre: dict[Node, int]
    post: dict[Node, int]


class SCCOutput(NamedTuple):
    dfs: DFSOutput
    metagraph: DiGraph


def _dfs_internal(G: DiGraph, node_order: list[Node]) -> DFSOutput:
    cc = 0
    ccnum = {node: -1 for node in node_order}
    prev = {node: None for node in node_order}
    pre = {node: -1 for node in node_order}
    post = {node: -1 for node in node_order}
    clock = 1

    for node in node_order:
        if pre[node] == -1:  # not explored yet
            cc += 1  # new connected component
            ccnum[node] = cc
            pre[node] = clock
            clock += 1
            stack = [(node, iter(sorted(G[node])))]
            while stack:
                v, neighbors = stack[-1]
                try:
                    w = next(neighbors)
                    if pre[w] == -1:
                        prev[w] = v
                        ccnum[w] = cc
                        pre[w] = clock
                        clock += 1
                        stack.append((w, iter(sorted(G[w]))))
                except StopIteration:
                    stack.pop()
                    post[v] = clock
                    clock += 1

    return DFSOutput(ccnum, prev, pre, post)


def DFS(G: DiGraph, s: Node = None) -> DFSOutput:
    nodes = sorted(G.nodes())

    # If a start node is specified, process it first
    if s is not None:
        nodes = [s] + [n for n in nodes if n != s]

    return _dfs_internal(G, nodes)


def SCC(G: DiGraph) -> SCCOutput:
    nodes = G.nodes()
    n = len(nodes)

    if n == 0:
        empty_dfs = DFSOutput({}, {}, {}, {})
        return SCCOutput(empty_dfs, DiGraph())

    reversed_g = G.reverse()
    dfs_reversed = DFS(reversed_g)
    # Sort nodes by decreasing post-order number from DFS on reversed graph
    sorted_post = sorted(nodes, key=lambda v: dfs_reversed.post[v], reverse=True)

    dfs_output = _dfs_internal(G, sorted_post)

    # construct meta graph
    max_cc = max(dfs_output.ccnum.values())
    cc = [list() for _ in range(max_cc + 1)]
    for node, ccnum in dfs_output.ccnum.items():
        cc[ccnum].append(node)
    
    meta_g_nodes = [ccnum[0] for ccnum in cc[1:]]
    meta_g = DiGraph()
    meta_g.add_nodes(meta_g_nodes)
    for u, v in G.edges():
        cu = dfs_output.ccnum[u]
        cv = dfs_output.ccnum[v]
        if cu != cv:
            cu_node = cc[cu][0]
            cv_node = cc[cv][0]
            meta_g.add_edge(cu_node, cv_node)
    
    # print(f"meta graph: node = {meta_g.nodes()}, edge = {meta_g.edges()}")

    return SCCOutput(dfs_output, meta_g)
