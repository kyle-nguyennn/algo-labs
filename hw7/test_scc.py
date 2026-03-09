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

if __name__ == "__main__":
    unittest.main()
