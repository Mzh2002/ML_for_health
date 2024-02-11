import numpy as np


def get_townsend_deprivation_index(unemployment, non_car_ownership, non_home_ownership, overcrowding,
                                   m_unemployment=.05, m_non_car_ownership=.3, m_non_home_ownership=.4,
                                   m_overcrowding=.1,
                                   s_unemployment=.02, s_non_car_ownership=.15, s_non_home_ownership=.2,
                                   s_overcrowding=.05):
    """
    :param (float) unemployment: percentage of economically active residents aged 16-59/64 who are unemployed
    :param (float) non_car_ownership: percentage of private households who do no possess a car
    :param (float) non_home_ownership: percentage of private households who do no possess a house
    :param (float) overcrowding: percentage of private households with more than one person per room
    :param (float) m_unemployment: mean of unemployment
    :param (float) m_non_car_ownership: mean of non_car_ownership
    :param (float) m_non_home_ownership: mean of non_home_ownership
    :param (float) m_overcrowding: mean of overcrowding
    :param (float) s_unemployment: standard deviation of unemployment
    :param (float) s_non_car_ownership: standard deviation of non_car_ownership
    :param (float) s_non_home_ownership: standard deviation of non_home_ownership
    :param (float) s_overcrowding: standard deviation of overcrowding

    :return: Townsend deprivation index, a measure of material deprivation
    """
    return np.log((unemployment - m_unemployment) / s_unemployment +
                  (non_car_ownership - m_non_car_ownership) / s_non_car_ownership +
                  (non_home_ownership - m_non_home_ownership) / s_non_home_ownership +
                  (overcrowding - m_overcrowding) / s_overcrowding)


print(get_townsend_deprivation_index(.2, .3, .4, .1))
