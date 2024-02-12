import numpy as np

def get_access_to_care_index(supply_locations, demand_locations, threshold_time, population, uninsured_rate):
    """
    :param supply_locations: A list of supply locations, each with 'location' (lat, lon), 'FTE_physicians'.
    :param demand_locations: A list of demand locations, each with 'location' (lat, lon).
    :param threshold_time: Threshold travel time to consider a location accessible.
    :param population: Dictionary mapping supply locations to surrounding population.
    :param uninsured_rate: Dictionary mapping supply locations to % of uninsured population.

    :return: Dictionary of demand locations and their Access to Care Index.
    """
    # Step 1: Calculate physician availability at each supply location
    physician_availability = {}
    for supply in supply_locations:
        loc = tuple(supply['location'])
        FTE_physicians = supply['FTE_physicians']
        surrounding_pop = population[loc]
        uninsured_factor = 1 - uninsured_rate[loc]
        availability = (FTE_physicians * uninsured_factor) / surrounding_pop
        physician_availability[loc] = availability

    # Step 2: Aggregate physician availability for each demand location
    access_to_care_index = {}
    for demand in demand_locations:
        loc = tuple(demand['location'])
        total_availability = 0
        for supply_loc, availability in physician_availability.items():
            if within_threshold(loc, supply_loc, threshold_time):
                total_availability += availability
        access_to_care_index[loc] = total_availability

    return access_to_care_index

def within_threshold(demand_location, supply_location, threshold_time):
    """
    Simplified check if a supply location is within threshold travel time from a demand location.
    """
    # Placeholder for a real distance/travel time calculation
    # Assume 1 unit of distance equals 1 minute of travel time for simplification
    distance = calculate_distance(demand_location, supply_location)
    travel_time = distance  # Simplification
    return travel_time <= threshold_time

def calculate_distance(demand_location, supply_location):
    """
    Dummy distance calculation. In practice, use Haversine or a mapping API.
    """
    # Simplified distance calculation - replace with accurate method for real use
    return np.sqrt((supply_location[0] - demand_location[0])**2 + (supply_location[1] - demand_location[1])**2)

# Example usage with dummy data
supply_locations = [
    {'location': (34.0522, -118.2437), 'FTE_physicians': 10},  # Supply location A
    {'location': (34.0522, -118.2430), 'FTE_physicians': 20},  # Supply location B
]
demand_locations = [
    {'location': (34.0522, -118.2437)},  # Demand location 1
    {'location': (34.0522, -118.2430)},  # Demand location 2
]
threshold_time = 10  # Threshold travel time in minutes
population = {
    (34.0522, -118.2437): 10000,
    (34.0522, -118.2430): 15000,
}
uninsured_rate = {
    (34.0522, -118.2437): 0.1,
    (34.0522, -118.2430): 0.15,
}

access_index = get_access_to_care_index(supply_locations, demand_locations, threshold_time, population, uninsured_rate)
print(access_index)
