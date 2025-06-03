import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

import pytest
from sp211.graph import Graph

def test_graph_node_count(small_test_graph):
    assert len(small_test_graph.nodes) > 0

def test_graph_edge_count(small_test_graph):
    assert len(small_test_graph.edges) == 13

def test_node_existence(small_test_graph):
    assert small_test_graph.exists_node('A')
    assert not small_test_graph.exists_node('Z')