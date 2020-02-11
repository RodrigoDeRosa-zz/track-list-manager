import unittest

from raver.model.graph.node import Node


class TestNode(unittest.TestCase):

    def test_connect(self):
        node1 = Node('1')
        node2 = Node('2')
        node3 = Node('3')

        self.assertFalse(node1.is_connected(node2))
        node2.connect_to(node1)
        self.assertFalse(node1.is_connected(node2))
        self.assertTrue(node2.is_connected(node1))
        node1.connect_to(node2)
        self.assertTrue(node1.is_connected(node2))

        self.assertFalse(node1.is_connected(node3))
        self.assertFalse(node3.is_connected(node1))
        self.assertFalse(node2.is_connected(node3))


if __name__ == '__main__':
    unittest.main()
