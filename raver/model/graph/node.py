class Node:

    def __init__(self, node_id: str):
        self.id = node_id

    def __gt__(self, other):
        return self.id > other.id

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f'<Node[id={self.id}]>'


