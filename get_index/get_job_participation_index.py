def get_job_participation_index(civilian_employed, civilian_unemployed, total_population):
    """
    :param civilian_employed: the number of people between 16 and 64 employed
    :param civilian_unemployed: the number of people between 16 and 64 unemployed
    :param total_population: total population between 16 and 64

    :return: Job Participation Index, an indicator for economic development and growth
    """
    return (civilian_employed + civilian_employed) / total_population