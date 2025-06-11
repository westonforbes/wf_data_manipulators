import pandas as pd
from PIL import Image
import numpy as np


class DataManipulators():
    """
    This class contains methods for file processing, including file dialogs,
    image viewing, and data loading utilities.
    """

    def __init__(self):
        """
        Initialize the FileDataProcessor class.
        Currently, no initialization logic is required.
        """
        pass


    def image_to_array(self, filepath):
        """
        Loads an image file into a numpy array.

        Parameters:
            filepath (str): The path to the image file.

        Returns:
            np.ndarray: Numpy array containing the image data.

        Raises:
            RuntimeError: If there is an error reading the image file.
        """
        try:
            # Open the image file using PIL and convert it to a numpy array.
            img = Image.open(filepath)
            img_array = np.array(img)
            return img_array
        except Exception as e:
            raise RuntimeError(f"an error occurred while reading the image: {e}")


    def csv_to_dataframe(self, filepath):
        """
        Loads a CSV file into a pandas DataFrame.

        Parameters:
            filepath (str): The path to the CSV file.

        Returns:
            pd.DataFrame: DataFrame containing the CSV data.

        Raises:
            RuntimeError: If there is an error reading the CSV file.
        """
        try:
            df = pd.read_csv(filepath)
            return df
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the csv: {e}")
        
        
    def dicts_to_dataframe(dict_list):
        """
        Converts a list of dictionaries to a pandas DataFrame.
        
        Each dictionary represents a row, and keys are treated as column names.
        Missing values are filled with NaN.
        
        Parameters:
            dict_list (list): A list of dictionaries.
            
        Returns:
            pd.DataFrame: The resulting DataFrame.
        """
        if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
            raise ValueError("Input must be a list of dictionaries.")
        
        df = pd.DataFrame(dict_list)
        return df


    def remove_keys_from_json(self, data, keys_to_remove):
        """
        Removes specified keys from each dictionary in a list.

        Parameters:
        - data: list of dictionaries (JSON-like)
        - keys_to_remove: list of keys to be removed from each dictionary

        Returns:
        - The cleaned list of dictionaries
        """
        for item in data:
            for key in keys_to_remove:
                item.pop(key, None)  # Safely remove key if it exists.
        return data
