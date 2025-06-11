# WF Data Manipulators

A Python utility library providing static methods for data manipulation and file processing tasks.

## Overview

The `DataManipulators` class contains static utility methods for:
- Converting images to numpy arrays
- Loading CSV files into pandas DataFrames
- Converting dictionaries to DataFrames
- Removing keys from JSON-like data structures
- Extracting columns from DataFrames as lists

## Installation

```bash
pip install pandas pillow numpy
```

## Usage

```python
from wf_data_manipulators import DataManipulators

# All methods are static, so no initialization required
```

## Methods Documentation

### `image_to_array(filepath)`

Loads an image file and converts it to a numpy array.

**Parameters:**
- `filepath` (str): The path to the image file

**Returns:**
- `np.ndarray`: Numpy array containing the image data

**Raises:**
- `RuntimeError`: If there is an error reading the image file

**Example:**
```python
img_array = DataManipulators.image_to_array("path/to/image.jpg")
print(img_array.shape)  # (height, width, channels)
```

---

### `csv_to_dataframe(filepath)`

Loads a CSV file into a pandas DataFrame.

**Parameters:**
- `filepath` (str): The path to the CSV file

**Returns:**
- `pd.DataFrame`: DataFrame containing the CSV data

**Raises:**
- `RuntimeError`: If there is an error reading the CSV file

**Example:**
```python
df = DataManipulators.csv_to_dataframe("data.csv")
print(df.head())
```

---

### `dicts_to_dataframe(dict_list)`

Converts a list of dictionaries to a pandas DataFrame.

Each dictionary represents a row, and keys are treated as column names. Missing values are filled with NaN.

**Parameters:**
- `dict_list` (list): A list of dictionaries

**Returns:**
- `pd.DataFrame`: The resulting DataFrame

**Raises:**
- `ValueError`: If input is not a list of dictionaries

**Example:**
```python
data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
df = DataManipulators.dicts_to_dataframe(data)
print(df)
#    name  age
# 0  John   30
# 1  Jane   25
```

---

### `remove_keys_from_json(data, keys_to_remove)`

Removes specified keys from each dictionary in a list.

**Parameters:**
- `data` (list): List of dictionaries to modify
- `keys_to_remove` (list): List of keys to be removed from each dictionary

**Returns:**
- `list`: The modified list of dictionaries with specified keys removed

**Example:**
```python
data = [{"name": "John", "age": 30, "temp_id": 123}]
cleaned = DataManipulators.remove_keys_from_json(data, ["temp_id"])
# Result: [{"name": "John", "age": 30}]
```

---

### `extract_column_as_list(df, column_name)`

Extract data from a specified column in a pandas DataFrame and return as a list.

**Parameters:**
- `df` (pd.DataFrame): The DataFrame to extract data from
- `column_name` (str): The name of the column to extract

**Returns:**
- `list`: A list containing the values from the specified column

**Raises:**
- `KeyError`: If the column name doesn't exist in the DataFrame

**Example:**
```python
df = pd.DataFrame({"names": ["Alice", "Bob", "Charlie"]})
names_list = DataManipulators.extract_column_as_list(df, "names")
# Result: ["Alice", "Bob", "Charlie"]
```

## Requirements

- pandas
- Pillow (PIL)
- numpy
