import numpy as np


def get_gini_index(incomes):
    """
    :param incomes: (list[float]) a list of incomes
    :return: gini index, measures inequality of income
    """
    mean = np.mean(incomes)
    n = len(incomes)
    gini = 0
    for i in range(n):
        for j in range(i):
            gini += np.abs(incomes[i] - incomes[j])
    gini = 1 / (mean * n * (n-1)) * gini
    return gini
