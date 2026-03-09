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
    cc = 0
    ccnum = {node: -1 for node in nodes}
    prev = {node: None for node in nodes}
    pre = {node: -1 for node in nodes}
    post = {node: -1 for node in nodes}
    pre_n = post_n = 0

    def explore(node):
        nonlocal pre_n
        nonlocal post_n
        nonlocal cc
        ccnum[node] = cc
        pre[node] = pre_n
        pre_n += 1
        neighbors = sorted(list(G[node]))
        for v in neighbors:
            if pre[v] == -1:
                prev[v] = node
                explore(v)
        post[node] = post_n
        post_n += 1

    for node in nodes:
        if pre[node] == -1: # not explored yet
            cc += 1 # new connected component
            explore(node)
    
    return DFSOutput(ccnum, prev, pre, post)


def SCC(G: DiGraph) -> SCCOutput:
    nodes = G.nodes()
    n = len(nodes)
    reversed = G.reverse()
    dfs_reversed = DFS(reversed)
    # largest  post-order number -> source
    # source in revsered -> sink in original graph
    # O(n) sort of post. Since we know the post-order number is in range 0 -> n-1
    sorted_post = [None] * n
    for node, post_order in dfs_reversed.post.items():
        sorted_post[post_order] = node
    sorted_post.reverse() # largest post-order number first
    ordered_g = DiGraph()
    ordered_g.add_nodes(sorted_post)
    ordered_g.add_edges(G.edges())

    dfs_output = DFS(ordered_g)
    # print(f"Connected components: {dfs_output.ccnum}")
    # print(f"Prev: {dfs_output.prev}")

    # construct meta graph
    cc = [list() for _ in range(max(dfs_output.ccnum.values()) + 1)]
    for node, ccnum in dfs_output.ccnum.items():
        cc[ccnum].append(node)
    # print(f"cc list: {cc}")
    
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
