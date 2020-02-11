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

    def add_node(self, node: Node):
        self.nodes.add(node)
