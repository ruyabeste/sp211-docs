import csv
import geopandas as gpd
from pathlib import Path

# Define the Node class
class Node:
    def __init__(self, node_id, lat, lon, name):
        self.id = node_id
        self.name = name

        try:
            self.latitude = float(lat) if lat != '' else None
            self.longitude = float(lon) if lon != '' else None
        except ValueError:
            self.latitude = None
            self.longitude = None

    def __repr__(self):
        return f"Node({self.id}, {self.name})"


# Define the Edge class
class Edge:
    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = float(cost)

    def __repr__(self):
        return f"Edge({self.from_node.id} -> {self.to_node.id}, cost={self.cost})"


# Define the Graph class
class Graph:
    def __init__(self):
        self.nodes = {}  # id -> Node
        self.edges = []  # list of Edge

    def load_nodes(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                node = Node(row['id'], row['latitude'], row['longitude'], row['name'])
                self.nodes[node.id] = node

                if node.latitude is None or node.longitude is None:
                    print(f"[INFO] Node {node.id} loaded without coordinates.")

    def load_edges(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                from_node = self.nodes.get(row['poi1'])
                to_node = self.nodes.get(row['poi2'])
                if from_node and to_node:
                    edge = Edge(from_node, to_node, row['cost'])
                    self.edges.append(edge)
                else:
                    print(f"[INFO] Skipped edge ({row['poi1']} - {row['poi2']}) due to missing node(s).")

    def get_neighbours(self, node_id):
        neighbours = []
        for edge in self.edges:
            if edge.from_node.id == node_id:
                neighbours.append((edge.to_node.id, edge.cost))
            elif edge.to_node.id == node_id:
                neighbours.append((edge.from_node.id, edge.cost))
        return neighbours

    def exists_node(self, node_id):
        return node_id in self.nodes

    def __repr__(self):
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"

    def export_shortest_path(self, previous, start_node, end_node, gdf):
        output_path = Path(__file__).resolve().parent.parent.parent / "examples" / "output" / "shortest_path.gpkg"
        output_path.parent.mkdir(parents=True, exist_ok=True)  # Create output folder if it doesn't exist

        layer_name = "shortest_path"

        if not self.exists_node(start_node) or not self.exists_node(end_node):
            print("Node IDs not present in the graph!")
            return

        # keep track of the nodes visited
        visited_nodes = []

        current_node = end_node
        while current_node != start_node:
            visited_nodes.append(current_node)
            current_node = previous.get(current_node)
            if current_node == "Origin":
                visited_nodes.append(start_node)
                break
        visited_nodes.append(start_node)
        print("PATH: ", visited_nodes)

        matched_rows = []
        for p in range(len(visited_nodes) - 1):
            node1 = visited_nodes[p]
            node2 = visited_nodes[p + 1]

            for _, row in gdf.iterrows():
                if (
                    (str(row["poi_id1"]) == str(node1) and str(row["poi_id2"]) == str(node2)) or
                    (str(row["poi_id2"]) == str(node1) and str(row["poi_id1"]) == str(node2))
                ):
                    matched_rows.append(row)
                    break

        if matched_rows:
            result_gdf = gpd.GeoDataFrame(matched_rows, crs=gdf.crs)
            result_gdf.to_file(output_path, layer=layer_name, driver="GPKG")
            print(f"Saved {len(result_gdf)} path segments to: {output_path.name}")
        else:
            print("No edges matched the visited path.")