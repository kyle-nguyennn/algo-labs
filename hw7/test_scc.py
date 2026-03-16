import unittest

from cs6515_scc import SCC

from graph.digraph import DiGraph


class TestSCC(unittest.TestCase):
    def test_base_case_1(self):
        input = DiGraph()

        input.add_node(1)

        output = SCC(input)

        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    def test_base_case_2(self):
        input = DiGraph()

        input.add_node(1)
        input.add_node(2)

        input.add_edge(1, 2)
        input.add_edge(2, 1)

        output = SCC(input)

        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    def test_scc(self):
        input = DiGraph()

        input.add_edge('A', 'B')

        input.add_edge('B', 'D')

        input.add_edge('B', 'C')
        input.add_edge('B', 'E')
        input.add_edge('E', 'B')
        input.add_edge('E', 'L')

        input.add_edge('C', 'F')
        input.add_edge('F', 'G')
        input.add_edge('G', 'F')
        input.add_edge('G', 'C')
        input.add_edge('F', 'I')

        input.add_edge('H', 'I')
        input.add_edge('H', 'J')
        input.add_edge('J', 'H')
        input.add_edge('I', 'J')
        input.add_edge('J', 'K')
        input.add_edge('K', 'L')
        input.add_edge('L', 'I')


        output = SCC(input)

        self.assertEqual(len(output.metagraph.nodes()), 5)
        self.assertEqual(len(output.metagraph.edges()), 5)

    # 1.06 - triangle graph: 3-node cycle = 1 SCC
    def test_scc_triangle(self):
        g = DiGraph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    # 1.08 - single source, single sink (DAG chain)
    def test_scc_single_source_single_sink(self):
        g = DiGraph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 3)
        self.assertEqual(len(output.metagraph.edges()), 2)

    # 1.10 - single source, many sinks
    def test_scc_single_source_many_sinks(self):
        g = DiGraph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 4)
        self.assertEqual(len(output.metagraph.edges()), 3)

    # 1.12 - many sources, single sink
    def test_scc_many_sources_single_sink(self):
        g = DiGraph()
        g.add_edge(1, 4)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 4)
        self.assertEqual(len(output.metagraph.edges()), 3)

    # 1.14 - gr1.7 graph (DPV Figure 3.9 style: two SCCs connected by a bridge)
    def test_scc_gr1_7(self):
        g = DiGraph()
        # SCC1: {1,2,3}
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        # SCC2: {4,5,6}
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 4)
        # bridge
        g.add_edge(3, 4)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 2)
        self.assertEqual(len(output.metagraph.edges()), 1)

    # 1.16 - gr1.11 graph (larger SCC structure)
    def test_scc_gr1_11(self):
        g = DiGraph()
        # SCC1: {A,B}
        g.add_edge('A', 'B')
        g.add_edge('B', 'A')
        # SCC2: {C,D}
        g.add_edge('C', 'D')
        g.add_edge('D', 'C')
        # SCC3: {E,F}
        g.add_edge('E', 'F')
        g.add_edge('F', 'E')
        # cross edges
        g.add_edge('B', 'C')
        g.add_edge('B', 'E')
        g.add_edge('D', 'F')
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 3)
        self.assertEqual(len(output.metagraph.edges()), 3)

    # 1.18 - gr1.15 graph (mix of SCCs and singletons)
    def test_scc_gr1_15(self):
        g = DiGraph()
        # SCC: {1,2,3,4,5}
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 1)
        # singletons reachable from the SCC
        g.add_edge(3, 6)
        g.add_edge(4, 7)
        g.add_edge(6, 7)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 3)
        self.assertEqual(len(output.metagraph.edges()), 3)

    # 1.19 - complete directed graph (all nodes in one SCC)
    def test_scc_complete_graph(self):
        g = DiGraph()
        n = 6
        for i in range(n):
            for j in range(n):
                if i != j:
                    g.add_edge(i, j)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    # 1.20 - balanced tree (directed DAG, each node is its own SCC)
    def test_scc_balanced_tree(self):
        g = DiGraph()
        # Binary tree: 1->{2,3}, 2->{4,5}, 3->{6,7}
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        g.add_edge(3, 7)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 7)
        self.assertEqual(len(output.metagraph.edges()), 6)

    # 1.21 - barbell graph (two cliques connected by a bridge)
    def test_scc_barbell(self):
        g = DiGraph()
        # Clique 1: {1,2,3} fully connected
        for i in [1, 2, 3]:
            for j in [1, 2, 3]:
                if i != j:
                    g.add_edge(i, j)
        # Clique 2: {4,5,6} fully connected
        for i in [4, 5, 6]:
            for j in [4, 5, 6]:
                if i != j:
                    g.add_edge(i, j)
        # Bridge (directed: only 3->4)
        g.add_edge(3, 4)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 2)
        self.assertEqual(len(output.metagraph.edges()), 1)

    # 1.22 - cycle graph (single directed cycle = 1 SCC)
    def test_scc_cycle(self):
        g = DiGraph()
        n = 10
        for i in range(n):
            g.add_edge(i, (i + 1) % n)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    # 1.23 - larger cycle graph
    def test_scc_cycle_large(self):
        g = DiGraph()
        n = 100
        for i in range(n):
            g.add_edge(i, (i + 1) % n)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

    # 1.24 - performance: large graph
    def test_scc_performance(self):
        g = DiGraph()
        n = 5000
        for i in range(n - 1):
            g.add_edge(i, i + 1)
        g.add_edge(n - 1, 0)
        output = SCC(g)
        self.assertEqual(len(output.metagraph.nodes()), 1)
        self.assertEqual(len(output.metagraph.edges()), 0)

if __name__ == "__main__":
    unittest.main()
