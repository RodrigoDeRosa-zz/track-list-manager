import unittest

from raver.model.track import Track
from raver.track_graph_generator import TrackGraphGenerator


class TestTrackGraphGenerator(unittest.TestCase):

    def test_graph_creation(self):
        tracks = [
            Track('Jumanji', '4B'),
            Track('Day Of Light', '4A'),
            Track('Sender', '3B'),
            Track('Atlas', '3A'),
            Track('Hear Me Out', '5A'),
            Track('The Space In Between', '4A')
        ]
        graph = TrackGraphGenerator.generate_graph(tracks)
        for node in graph.nodes:
            if node.id == 'Jumanji':
                self.assert_connections(node.edges, 3, ['Day Of Light', 'Sender', 'The Space In Between'])
            elif node.id == 'Day Of Light':
                self.assert_connections(node.edges, 4, ['Jumanji', 'Atlas', 'Hear Me Out', 'The Space In Between'])
            elif node.id == 'Sender':
                self.assert_connections(node.edges, 2, ['Jumanji', 'Atlas'])
            elif node.id == 'Atlas':
                self.assert_connections(node.edges, 3, ['Day Of Light', 'Sender', 'The Space In Between'])
            elif node.id == 'Hear Me Out':
                self.assert_connections(node.edges, 2, ['Day Of Light', 'The Space In Between'])
            elif node.id == 'The Space In Between':
                self.assert_connections(node.edges, 4, ['Day Of Light', 'Hear Me Out', 'Atlas', 'Jumanji'])

    def assert_connections(self, edges, expected_edges_len, expected_neighbors_ids):
        self.assertEqual(expected_edges_len, len(edges))
        for neighbor in edges:
            self.assertTrue(neighbor.id in expected_neighbors_ids)


if __name__ == '__main__':
    unittest.main()
