import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        df = pd.read_csv(self.file_path)
        return df

    def inspect_data(self, df):
        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        print("\nFirst 5 rows:")
        print(df.head())
        return df