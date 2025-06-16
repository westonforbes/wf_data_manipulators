import pandas as pd
from PIL import Image
import numpy as np


class DataManipulators():
    """
    This class contains methods for data manipulation, including image processing,
    CSV handling, and DataFrame operations.
    """

    @staticmethod
    def image_to_array(filepath):
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

    @staticmethod
    def csv_to_dataframe(filepath):
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
        
    @staticmethod    
    def dicts_to_dataframe(dict_list):
        """
        Converts a list of dictionaries to a pandas DataFrame.
        
        Each dictionary represents a row, and keys are treated as column names.
        Missing values are filled with NaN.
        
        Parameters:
            dict_list (list): A list of dictionaries.
            
        Returns:
            pd.DataFrame: The resulting DataFrame.
            
        Raises:
            ValueError: If input is not a list of dictionaries.
        """
        if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
            raise ValueError("Input must be a list of dictionaries.")
        
        df = pd.DataFrame(dict_list)
        return df

    @staticmethod
    def delete_keys_in_list_dict(data, keys_to_remove):
        """
        Removes specified keys from each dictionary in a list.

        Parameters:
            data (list): List of dictionaries to modify.
            keys_to_remove (list): List of keys to be removed from each dictionary.

        Returns:
            list: The modified list of dictionaries with specified keys removed.
        """
        result = []
        for item in data:
            new_item = {k: v for k, v in item.items() if k not in keys_to_remove}
            result.append(new_item)
        return result
    
    @staticmethod
    def keep_keys_in_list_dict(data, keys_to_keep):
        """
        Keeps only the specified keys in each dictionary in a list,
        removing all other keys.

        Parameters:
            data (list): List of dictionaries to modify.
            keys_to_keep (list): List of keys to retain in each dictionary.

        Returns:
            list: The modified list of dictionaries with only specified keys retained.
        """
        result = []
        for item in data:
            new_item = {k: v for k, v in item.items() if k in keys_to_keep}
            result.append(new_item)
        return result

    @staticmethod
    def extract_column_as_list(df, column_name):
        """
        Extract data from a specified column in a pandas DataFrame and return as a list.
        
        Parameters:
            df (pd.DataFrame): The DataFrame to extract data from.
            column_name (str): The name of the column to extract.
        
        Returns:
            list: A list containing the values from the specified column.

        Raises:
            KeyError: If the column name doesn't exist in the DataFrame.
        """
        if column_name not in df.columns:
            raise KeyError(f"Column '{column_name}' not found in DataFrame")

        return df[column_name].tolist()
