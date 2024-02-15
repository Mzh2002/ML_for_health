def get_education_index(education_attainment_levels,years_of_schooling, max_ays):
    """
    :param (List[str]) education_attainment_levels: proportion of population with a certain level of schooling (p_i) 
    :param (List[float]) years_of_schooling: corresponding years of schooling (y_i).
    :param (float) max_ays: The maximum average years of schooling (AYS) for normalization.

    :return: The average years of schooling (AYS) for the concerned population.
    """
    average_year_of_schooling = 0
    
    for p_i, y_i in zip(education_attainment_levels, years_of_schooling):
        average_year_of_schooling += p_i * y_i

    # this part has not revealed in the documentation
    education_index = average_year_of_schooling / max_ays

    return education_index

# dummy variable test
education_attainment_levels = [0.1, 0.2, 0.3]  # Replace with actual proportions
years_of_schooling = [0, 2.5, 5.5]             # Replace with actual years of schooling
max_ays = 20  # Assuming the maximum AYS is 20 years.

education_index = get_education_index(education_attainment_levels, years_of_schooling, max_ays)
print(f"The Education Index is: {education_index}")
