import unittest

from raver.model.graph.graph import Graph
from raver.model.graph.node import Node


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.nodes = [Node(str(i)) for i in range(1, 11)]

    def test_graph_edge_addition(self):
        graph = Graph()
        graph.connect(self.nodes[0], self.nodes[1])
        graph.connect(self.nodes[0], self.nodes[3])
        graph.connect(self.nodes[2], self.nodes[5])
        graph.connect(self.nodes[6], self.nodes[7])
        graph.connect(self.nodes[1], self.nodes[2])

        self.assertTrue(self.nodes[0] in graph.nodes)
        self.assertTrue(self.nodes[1] in graph.nodes)
        self.assertTrue(self.nodes[2] in graph.nodes)
        self.assertTrue(self.nodes[3] in graph.nodes)
        self.assertTrue(self.nodes[5] in graph.nodes)
        self.assertTrue(self.nodes[6] in graph.nodes)
        self.assertTrue(self.nodes[7] in graph.nodes)

        self.assertTrue(self.nodes[1].is_connected(self.nodes[0]))
        self.assertTrue(self.nodes[3].is_connected(self.nodes[0]))
        self.assertTrue(self.nodes[2].is_connected(self.nodes[5]))
        self.assertTrue(self.nodes[6].is_connected(self.nodes[7]))
        self.assertTrue(self.nodes[1].is_connected(self.nodes[2]))
        self.assertFalse(self.nodes[3].is_connected(self.nodes[2]))


if __name__ == '__main__':
    unittest.main()
