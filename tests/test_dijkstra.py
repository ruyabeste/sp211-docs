import unittest
from pathlib import Path
from sp211.graph import Graph
from sp211.dijkstra import shortest_path

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # Test için örnek .csv verilerini yüklüyoruz
        self.graph = Graph()
        data_dir = Path(__file__).resolve().parent.parent / "data" / "test"
        self.graph.load_nodes(data_dir / "nodes.csv")
        self.graph.load_edges(data_dir / "edges.csv")

    def test_shortest_path_costs(self):
        costs, previous = shortest_path(self.graph, "A")
        self.assertIsInstance(costs, dict)
        self.assertGreaterEqual(len(costs), 1)
        self.assertEqual(costs["A"], 0)

    def test_shortest_path_previous(self):
        _, previous = shortest_path(self.graph, "A")
        self.assertIsInstance(previous, dict)
        self.assertEqual(previous["A"], "Origin")

if __name__ == '__main__':
    unittest.main()