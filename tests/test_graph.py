import unittest
from pathlib import Path
import sys

# src klasörünü path'e ekle
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from sp211.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        # Test verileri içeren CSV dosyalarının yolu
        self.graph = Graph()
        data_dir = Path(__file__).resolve().parent.parent / "data" / "test"
        self.graph.load_nodes(data_dir / "nodes.csv")
        self.graph.load_edges(data_dir / "edges.csv")

    def test_nodes_loaded(self):
        self.assertGreater(len(self.graph.nodes), 0, "Node verisi yüklenemedi")

    def test_edges_loaded(self):
        self.assertGreater(len(self.graph.edges), 0, "Edge verisi yüklenemedi")

    def test_graph_structure(self):
        node = list(self.graph.nodes.keys())[0]
        self.assertIn(node, self.graph.nodes, "Node grafikte mevcut değil")

if __name__ == '__main__':
    unittest.main()