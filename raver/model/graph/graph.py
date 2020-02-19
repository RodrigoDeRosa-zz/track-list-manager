from typing import Set

from raver.model.graph.node import Node


class Graph:

    def __init__(self, nodes: Set[Node] = None):
        self.nodes: Set[Node] = nodes if nodes else set()

    def connect(self, one: Node, another: Node):
        # Connect nodes between them (this is a non directed graph)
        one.connect_to(another)
        another.connect_to(one)
        # Add nodes if they were not already in the graph
        self.nodes.add(one)
        self.nodes.add(another)

    def are_connected(self, one: Node, another: Node):
        # Two way checking is not really necessary because it is a non directed graph but it could be useful.
        return one in self.nodes and another in self.nodes and one.is_connected(another) and another.is_connected(one)

    def add_node(self, node: Node):
        self.nodes.add(node)
