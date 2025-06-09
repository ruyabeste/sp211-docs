import geopandas as gpd
import logging

def calculate_total_distance(gpkg_path, layer_name="shortest_path"):
    """
    Calculates the total distance (in kilometers) of the exported shortest path.
    """
    gdf = gpd.read_file(gpkg_path, layer=layer_name)
    gdf = gdf.to_crs(epsg=3857)  # Convert to metric projection
    total_km = gdf.length.sum() / 1000  # Convert from meters to km

    logging.info(f"Total distance calculated: {total_km:.2f} km")
    return total_km

def calculate_fuel_cost(distance_km, consumption_l_per_100km=6.5, fuel_price_per_liter=44.90):
    """
    Estimates fuel cost based on distance, consumption rate and fuel price.
    """
    cost = (distance_km / 100) * consumption_l_per_100km * fuel_price_per_liter
    logging.info(f"Fuel cost estimated: {cost:.2f} TL (distance: {distance_km:.2f} km)")
    return cost