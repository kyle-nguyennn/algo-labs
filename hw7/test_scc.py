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


if __name__ == "__main__":
    unittest.main()
