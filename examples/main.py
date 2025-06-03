import sys
from pathlib import Path
import geopandas as gpd

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from sp211 import graph, dijkstra

# Path to production data
DATA_DIR = Path(__file__).parent.parent / "data" / "production"

# Initialize graph and load data
graph = graph.Graph()
graph.load_nodes(DATA_DIR / "nodes_ilceler.csv")
graph.load_edges(DATA_DIR / "edges_ilceler.csv")

# Load GeoPackage file
gdf = gpd.read_file(DATA_DIR / "DT_ilceler.gpkg", layer="edges")

# Define start and end nodes
start_node = '265'
end_node = '302'

# Compute shortest path
costs, previous = dijkstra.shortest_path(graph, start_node)

# Output cost dictionary
print(costs)

# Export shortest path as GeoPackage
graph.export_shortest_path(previous, start_node, end_node, gdf)


