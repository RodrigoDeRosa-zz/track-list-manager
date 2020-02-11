from math import ceil
from typing import Set, List

from raver.model.graph.graph import Graph
from raver.model.graph.node import Node


class BillyRowHamilton:
    """
    Class designed to solve the William Rowan Hamilton's problem adapted to our current need. The difference is that we
     want the best possible result, that being all the paths that walk through as many nodes as possible without
     repeating vertices, instead of those that walk through every node of the graph.
    """

    @classmethod
    def find_paths(cls, graph: Graph, coverage_proportion: float) -> Set[List[Node]]:
        """
        Returns a set of paths that go through at least the `coverage_proportion` of the graph's nodes. If we
        had a graph with 10 nodes, and `coverage_proportion` was 0.7, then we would return all the pseudo hamiltonian
        paths with at least 7 nodes.
        """
        # Minimal number of nodes that a path should visit to be acceptable
        accepted_length: int = ceil(len(graph.nodes)*coverage_proportion)
        visited: Set[Node] = set()
        return set()
