import pandas as pd
import os

data_file_path = os.path.join('..', 'data', 'food_data.csv')
def load_data():
    try:
         data = pd.read_csv(data_file_path)
         print("Data loaded successfully")
         return data
    except FileNotFoundError:
         print(f"File not found at {data_file_path}")
         return None