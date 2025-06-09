Develop a New Feature
=====================

This project is a Python package developed to calculate the **shortest path between two points** using **Dijkstra's algorithm**.

It reads spatial and tabular data representing nodes and edges, builds a graph structure, and computes the shortest route between a selected origin and destination. The output includes:

- The optimal path (as node IDs)
- The cost (total distance)
- A visualization exported as a GeoPackage

New Feature: Fuel Cost Estimation
---------------------------------

In this branch, a **new feature** was developed to estimate **fuel consumption** and **fuel cost** based on the total travel distance.

**Assumptions**:
- Fuel consumption rate: 6.5 liters per 100 km
- Fuel price: 44.90 TL per liter

The additional output includes:
- 🔴 Total distance in kilometers
- ⛽ Estimated fuel cost (in TL)

Logging has also been integrated to record key process events.

Usage Example (from main.py):
-----------------------------

.. code-block:: python

    from sp211.dijkstra import shortest_path
    from sp211.graph import Graph
    from sp211.new_feature import estimate_fuel_cost

    G = Graph()
    G.load_nodes("data/production/nodes_ilceler.csv")
    G.load_edges("data/production/edges_ilceler.csv")

    costs, previous = shortest_path(G, start_node="265")
    distance = G.calculate_total_distance(previous, "265", "302")
    cost = estimate_fuel_cost(distance)

    print(f"Total Distance: {distance:.2f} km")
    print(f"Estimated Fuel Cost: {cost:.2f} TL")

Modules
=======

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
