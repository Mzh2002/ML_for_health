def get_affordability_index(housing_cost, transportation_cost, total_income):
    """
    :param housing_cost: (float) the total cost of housing in an area
    :param transportation_cost: (float) the total cost of transportation in an area
    :param total_income: (float) the total income in an area

    :return (float) affordability index, used to measure the proportion of income spent on housing
and transportation
    """
    return (housing_cost + transportation_cost) / total_income
