from __future__ import annotations

from typing import Set


class Node:

    def __init__(self, node_id: str):
        self.id = node_id
        self.edges: Set[Node] = set()

    def connect_to(self, another: Node):
        self.edges.add(another)

    def is_connected(self, another: Node):
        return another in self.edges

    def __gt__(self, other: Node) -> bool:
        return self.id > other.id

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f'<Node[id={self.id}]>'


