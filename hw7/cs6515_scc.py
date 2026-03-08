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
    pass


def SCC(G: DiGraph) -> SCCOutput:
    pass
