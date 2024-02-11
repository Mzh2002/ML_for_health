def get_affordability_index(housing_cost, transportation_cost, total_income):
    """
    :param (float) housing_cost: the total cost of housing in an area
    :param (float) transportation_cost: the total cost of transportation in an area
    :param (float) total_income: the total income in an area

    :return (float): affordability index, used to measure the proportion of income spent on housing
and transportation
    """
    return (housing_cost + transportation_cost) / total_income
