from typing import Set, Tuple

from raver.model.graph.node import Node


class Graph:

    def __init__(self, nodes: Set[Node] = None, edges: Set[Tuple[Node, Node]] = None):
        self.nodes: Set[Node] = nodes if nodes else set()
        self.edges: Set[Tuple[Node, Node]] = set() if not edges else self.__sorted_edges(edges)

    def add_edge(self, one: Node, another: Node):
        # Add nodes if they were not already in the graph
        self.nodes.add(one)
        self.nodes.add(another)
        # Add edge
        self.edges.add(self.__make_edge(one, another))

    def add_node(self, node: Node):
        self.nodes.add(node)

    def are_connected(self, one: Node, another: Node):
        """ Check if there is an edge that connects these two nodes. """
        return self.__make_edge(one, another) in self.edges

    @classmethod
    def __sorted_edges(cls, edges: Set[Tuple[Node, Node]]):
        # Make sure all edges are sorted when creating Graph through constructor
        return {cls.__make_edge(edge[0], edge[1]) for edge in edges}

    @classmethod
    def __make_edge(cls, one: Node, another: Node) -> Tuple[Node, Node]:
        # Sort tuple to avoid adding an edge more than once as this is an undirected graph
        return (one, another) if one > another else (another, one)
