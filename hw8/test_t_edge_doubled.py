import unittest

from cs6515_t_edge_doubled import TEdgeDoubled

from graph.graph import Graph


class TestTEdgeDoubled(unittest.TestCase):
    def test_base_case_1(self):
        graph = Graph([("a", "b"), ("b", "c"), ("a", "c")])
        tree = Graph([("a", "b"), ("b", "c")])

        weights = {
            ("a", "b"): 1,
            ("b", "a"): 1,
            ("b", "c"): 1,
            ("c", "b"): 1,
            ("a", "c"): 4,
            ("c", "a"): 4,
        }

        edge = ("a", "b")

        weights[edge] *= 2
        weights[(edge[1], edge[0])] *= 2

        mst = TEdgeDoubled(graph, tree, weights, edge)

        expected = Graph([("a", "b"), ("b", "c")])

        self.assertEqual(set(mst.edges()), set(expected.edges()))

    def test_base_case_2(self):
        graph = Graph([("a", "b"), ("b", "c"), ("a", "c")])
        tree = Graph([("a", "b"), ("b", "c")])

        weights = {
            ("a", "b"): 1,
            ("b", "a"): 1,
            ("b", "c"): 1,
            ("c", "b"): 1,
            ("a", "c"): 1,
            ("c", "a"): 1,
        }

        edge = ("a", "b")

        weights[edge] *= 2
        weights[(edge[1], edge[0])] *= 2

        mst = TEdgeDoubled(graph, tree, weights, edge)

        expected = Graph([("a", "c"), ("b", "c")])

        self.assertEqual(set(mst.edges()), set(expected.edges()))


if __name__ == "__main__":
    unittest.main()
