import numpy as np

def get_food_accessibility_index(distances: list[float], area_types: list[str], total_population: int) -> float:
    """
    :param distances: (list[float]) List of distances of individuals from the nearest supermarket.
    :param area_types: (list[str]) List indicating whether each individual lives in an 'urban' or 'rural' area.
    :param total_population: (int) Total population for calculating the proportion with low access.

    :return: (float) Food Accessibility Index as a proportion of the population with low access.
    """
    urban_criteria = 1
    rural_criteria = 10

    low_access = np.array([
        distance > urban_criteria if area_type.lower() == 'urban' else distance > rural_criteria
        for distance, area_type in zip(distances, area_types)
    ])


    food_accessibility_index = np.sum(low_access) / total_population

    return food_accessibility_index


distances = [0.5, 1.5, 5, 11]
area_types = ['urban', 'urban', 'rural', 'rural']
total_population = 4

index = get_food_accessibility_index(distances, area_types, total_population)
print(f"Food Accessibility Index: {index:.4f}")
