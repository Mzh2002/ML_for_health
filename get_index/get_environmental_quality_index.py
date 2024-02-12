import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def get_environmental_quality_index(data_frame):
    """
    Calculate the Environmental Quality Index (EQI) using Principal Component Analysis (PCA).

    :param data_frame: Pandas DataFrame with rows as observations and columns as environmental indicators.
    :return: Pandas Series representing the EQI for each observation.
    """
    # Standardize the data (mean=0, std=1)
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_frame)

    # Initialize PCA - for simplicity, we reduce the data to 1 principal component
    pca = PCA(n_components=1)

    # Fit PCA on the standardized data and transform the data
    principal_components = pca.fit_transform(standardized_data)

    # Convert the first principal component to a Pandas Series
    eqi_series = pd.Series(principal_components.flatten(), index=data_frame.index)

    return eqi_series

# Example usage:
# Load your data into a DataFrame (replace 'your_data.csv' with your actual data file)
# data = pd.read_csv('your_data.csv')
# eqi = calculate_EQI(data)
# print(eqi)
