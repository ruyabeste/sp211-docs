import sys
import logging
from pathlib import Path
import geopandas as gpd

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from sp211 import graph, dijkstra, new_feature

# Logging Setup 
log_path = Path(__file__).resolve().parent / "output" / "logfile.log"
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

# Path to production data
DATA_DIR = Path(__file__).parent.parent / "data" / "production"

# Initialize graph and load data
graph = graph.Graph()
graph.load_nodes(DATA_DIR / "nodes_ilceler.csv")
graph.load_edges(DATA_DIR / "edges_ilceler.csv")
logging.info("Graph data loaded successfully.")

# Load GeoPackage file
gdf = gpd.read_file(DATA_DIR / "DT_ilceler.gpkg", layer="edges")

# Define start and end nodes
start_node = '265'
end_node = '302'
logging.info(f"Start: {start_node}, End: {end_node}")

# Compute shortest path
costs, previous = dijkstra.shortest_path(graph, start_node)

# Output cost dictionary
print(costs)

# Export shortest path as GeoPackage
graph.export_shortest_path(previous, start_node, end_node, gdf)
logging.info("Shortest path exported successfully.")

# Fuel Cost Estimation
gpkg_path = Path(__file__).parent / "output" / "shortest_path.gpkg"
distance = new_feature.calculate_total_distance(gpkg_path)
cost = new_feature.calculate_fuel_cost(distance)

print(f"\n📍 Total Distance: {distance:.2f} km")
print(f"⛽ Estimated Fuel Cost: {cost:.2f} TL")

logging.info(f"Total distance: {distance:.2f} km")
logging.info(f"Estimated fuel cost: {cost:.2f} TL")