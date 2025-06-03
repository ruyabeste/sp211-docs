def shortest_path(graph, base_node):
    """
    Implements Dijkstra's algorithm to compute shortest paths
    from the base_node to all other nodes in the graph.

    Parameters:
        graph (Graph): The graph object containing nodes and edges.
        base_node (str): The ID of the starting node.

    Returns:
        tuple: (costs, previous) where:
            costs (dict): node_id -> total cost from base_node
            previous (dict): node_id -> previous node on the shortest path
    """
    visited = {}
    costs = {}
    previous = {}

    for node_id in graph.nodes:
        visited[node_id] = False
        costs[node_id] = float('inf')
        previous[node_id] = None

    costs[base_node] = 0
    previous[base_node] = "Origin"

    current_node = base_node

    while current_node is not None:
        visited[current_node] = True
        neighbours = graph.get_neighbours(current_node)

        for i in range(len(neighbours)):
            neighbour_node = neighbours[i][0]
            edge_cost = neighbours[i][1]
            new_cost = costs[current_node] + edge_cost

            if new_cost < costs[neighbour_node]:
                costs[neighbour_node] = new_cost
                previous[neighbour_node] = current_node

        min_cost = float('inf')
        current_node = None

        for node_id in graph.nodes:
            if not visited[node_id] and costs[node_id] < min_cost:
                min_cost = costs[node_id]
                current_node = node_id

    return costs, previous