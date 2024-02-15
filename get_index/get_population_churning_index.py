def calculate_population_churning_rate(in_migration, out_migration, total_population):
    """
    Calculate the Population Churning Rate.

    :param (int) in_migration: The number of individuals who have migrated into the area.
    :param (int) out_migration: The number of individuals who have migrated out of the area.
    :param (int) total_population: The total number of individuals in the population.

    :return: The Population Churning Rate, which is a measure of population movement.
    """
    return (in_migration + out_migration) / total_population

# Example usage:
in_migration = 500  # Example number of people who moved in
out_migration = 300  # Example number of people who moved out
total_population = 10000  # Example total population

churning_rate = calculate_population_churning_rate(in_migration, out_migration, total_population)
print(f"The Population Churning Rate is: {churning_rate}")
