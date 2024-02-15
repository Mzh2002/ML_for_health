import numpy as np

def calculate_spatial_dissimilarity_index(CN_ij, CN_i, CN_j, CN, CP_j):
    """
    Calculate the Spatial Dissimilarity Index (SD).

    :param (np.array) CN_ij: 2D array where each element represents the composite population count of ethnic group j in spatial unit i.
    :param (np.array) CN_i: 1D array with the total composite population count in each spatial unit i.
    :param (np.array) CN_j: 1D array with the total composite population count of each ethnic group j.
    :param (int) CN: Total population in the city.
    :param (np.array) CP_j: 1D array with the proportion of population in each ethnic group j.

    :return: The Spatial Dissimilarity Index.
    """
    n, m = CN_ij.shape
    CE_ij = ((CN_i[:, None] - CN_j[None, :]) / CN) * CN
    sum_abs_diff = np.sum(np.abs(CN_ij - CE_ij), axis=0)
    sum_weighted_diff = np.sum(sum_abs_diff * (CN_i[:, None] * CP_j[None, :] * (1 - CP_j[None, :])), axis=0)
    
    SD = 0.5 * np.sum(sum_weighted_diff / CP_j) / CN
    return SD

# Example usage with dummy data:
# Assume we have 2 spatial units and 3 ethnic groups
CN_ij = np.array([[100, 150, 250], [200, 300, 500]])  # Replace with actual data
CN_i = np.array([500, 1000])                          # Total composite population in each spatial unit
CN_j = np.array([300, 450, 750])                      # Total composite population for each ethnic group
CN = 1500                                             # Total population in the city
CP_j = CN_j / CN                                      # Proportion of population in each ethnic group

sd_index = calculate_spatial_dissimilarity_index(CN_ij, CN_i, CN_j, CN, CP_j)
print(f"The Spatial Dissimilarity Index is: {sd_index}")
