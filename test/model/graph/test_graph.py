import unittest

from parameterized import parameterized

from raver.model.graph.graph import Graph
from raver.model.graph.node import Node


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.nodes = [Node(str(i)) for i in range(1, 11)]

    @parameterized.expand([
        [0, 1, True],
        [0, 2, False],
        [5, 3, True],
        [2, 7, True],
        [7, 5, False]
    ])
    def test_graph_creation(self, node_idx1, node_idx2, expected_result):
        edges = {
            (self.nodes[0], self.nodes[1]),
            (self.nodes[1], self.nodes[5]),
            (self.nodes[5], self.nodes[3]),
            (self.nodes[2], self.nodes[7])
        }
        graph = Graph(set(self.nodes), edges)
        self.assertEqual(expected_result, graph.are_connected(self.nodes[node_idx1], self.nodes[node_idx2]))

    def test_graph_edge_addition(self):
        graph = Graph()
        graph.add_edge(self.nodes[0], self.nodes[1])
        graph.add_edge(self.nodes[2], self.nodes[4])
        graph.add_edge(self.nodes[1], self.nodes[2])
        graph.add_edge(self.nodes[7], self.nodes[8])
        self.assertTrue(graph.are_connected(self.nodes[1], self.nodes[0]))
        self.assertTrue(graph.are_connected(self.nodes[4], self.nodes[2]))
        self.assertTrue(graph.are_connected(self.nodes[2], self.nodes[4]))
        self.assertFalse(graph.are_connected(self.nodes[5], self.nodes[3]))
        self.assertFalse(graph.are_connected(self.nodes[5], self.nodes[7]))


if __name__ == '__main__':
    unittest.main()
