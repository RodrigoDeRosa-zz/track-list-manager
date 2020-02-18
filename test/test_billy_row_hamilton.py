import unittest

from raver.billy_row_hamilton import BillyRowHamilton
from raver.model.graph.graph import Graph
from raver.model.graph.node import Node


class TestBillyRowHamilton(unittest.TestCase):

    def setUp(self) -> None:
        self.node_a = Node('a')
        self.node_b = Node('b')
        self.node_c = Node('c')
        self.node_d = Node('d')

    def test_basic_graph(self):
        graph = Graph()
        graph.connect(self.node_a, self.node_b)
        graph.connect(self.node_b, self.node_c)
        graph.connect(self.node_a, self.node_c)
        graph.connect(self.node_c, self.node_d)
        graph.connect(self.node_a, self.node_d)
        paths = BillyRowHamilton().find_paths(graph, 1)
        self.assertEqual(12, len(paths))
        paths = BillyRowHamilton().find_paths(graph, 0.75)
        self.assertEqual(12 + 16, len(paths))
        self.assertEqual(16, len([path for path in paths if len(path) == 3]))
        self.assertEqual(12, len([path for path in paths if len(path) == 4]))
        paths = BillyRowHamilton().find_paths(graph, 0.5)
        self.assertEqual(12 + 16 + 10, len(paths))
        self.assertEqual(10, len([path for path in paths if len(path) == 2]))
        self.assertEqual(16, len([path for path in paths if len(path) == 3]))
        self.assertEqual(12, len([path for path in paths if len(path) == 4]))

    def test_no_possible_hamiltonian_path(self):
        graph = Graph()
        graph.connect(self.node_a, self.node_b)
        graph.connect(self.node_a, self.node_c)
        graph.connect(self.node_a, self.node_d)
        paths = BillyRowHamilton().find_paths(graph, 1)
        self.assertEqual(0, len(paths))
        paths = BillyRowHamilton().find_paths(graph, 0.75)
        self.assertEqual(6, len(paths))


if __name__ == '__main__':
    unittest.main()
