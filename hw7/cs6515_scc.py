from typing import NamedTuple

from graph.digraph import DiGraph, Node


class DFSOutput(NamedTuple):
    ccnum: dict[Node, int]
    prev: dict[Node, Node | None]
    pre: dict[Node, int]
    post: dict[Node, int]


class SCCOutput(NamedTuple):
    dfs: DFSOutput
    metagraph: DiGraph


def DFS(G: DiGraph, s: Node = None) -> DFSOutput:
    nodes = G.nodes()
    ccnum = {node: -1 for node in nodes}
    prev = {node: None for node in nodes}
    pre = {node: -1 for node in nodes}
    post = {node: -1 for node in nodes}
    pre_n = post_n = 0

    def explore(node):
        neighbors = sorted(list(G[node]))
        for v in neighbors:
            if pre[v] == -1:
                pre[v] = pre_n
                pre_n += 1
                prev[v] = node
                explore(v)
                post[v] = post_n
                post_n += 1

    for node in nodes:
        if pre[node] == -1: # not explored yet
            pre[node] = pre_n
            pre_n += 1
            explore(node)
            post[node] = post_n
            post_n += 1
    
    return DFSOutput(ccnum, prev, pre, post)


def SCC(G: DiGraph) -> SCCOutput:
    nodes = G.nodes()
    n = len(nodes)
    reversed = G.reverse()
    dfs_output = DFS(reversed)
    # largest  post-order number -> source
    # source in revsered -> sink in original graph
    # O(n) sort of post. Since we know the post-order number is in range 0 -> n-1
    sorted_post = [None] * n
    for node, post_order in dfs_output.post.items():
        sorted_post[post_order] = node

    meta_g = DiGraph()
    scc = {node: -1 for node in nodes}
    for node, _ in sorted_post:
        if scc[node] == -1: # not explored, representative of this scc
            meta_g.add_node(node)
            sub_dfs_output = DFS(G, node)
            for sub_node, _ in sub_dfs_output.ccnum.items():
                scc[sub_node] = node

