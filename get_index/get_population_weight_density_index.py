def get_population_weighted_density_index(population_density, population, area, max_density):
    """
    Calculate the normalized Population-Weighted Density Index.

    :param (List[float]) population_density: A list of population densities for each area.
    :param (List[int]) population: A list of populations for each area.
    :param (List[float]) area: A list of area sizes for each corresponding population.
    :param (float) max_density: The maximum observed or possible density for normalization.

    :return: The normalized Population-Weighted Density Index, a value between 0 and 1.
    """
    weighted_density_sum = 0
    total_population = sum(population)
    
    for pd, pop, a in zip(population_density, population, area):
        weighted_density_sum += (pd / a) * pop
    
    # This part has not been revealed
    # Normalizing the index to be between 0 and 1 by dividing by maximum possible density
    population_weighted_density_index = (weighted_density_sum / total_population) / max_density

    return population_weighted_density_index

# dummy usage:
population_density = [240.3, 1053.3, 539.6, 341.2]  # Population density per square mile for each area
population = [901, 790, 599, 604]                   # Population for each area
area = [3.75, 0.75, 1.1, 1.77]                      # Area size in square miles for each area
max_density = 2000  # This is an illustrative example. Use the actual max density for your context.

pw_density_index = get_population_weighted_density_index(population_density, population, area, max_density)
print(f"The Normalized Population-Weighted Density Index is: {pw_density_index}")
