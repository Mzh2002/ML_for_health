def get_walkability_index(con: float, ent: float, far: float, hdens: float) -> float:
    """
    :param con: (float) Connectivity, reflecting the design of the built environment.
    :param ent: (float) Land use diversity, indicating the mix of different types of land uses.
    :param far: (float) Distance to transit, inversely related to the distance to the nearest public transit.
    :param hdens: (float) Residential and employment density in the area.

    :return: (float) The calculated Walkability Index.
    """
    wai = (2 * con) + ent + far + hdens
    return wai


con = 5.0
ent = 3.0
far = 2.0
hdens = 4.0

walkability_index = get_walkability_index(con, ent, far, hdens)
print(f"Walkability Index: {walkability_index}")
