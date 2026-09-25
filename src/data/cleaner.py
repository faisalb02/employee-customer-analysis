import pandas as pd


class BaseDataProcessor:
    def process(self, df):
        raise NotImplementedError


class DataCleaner(BaseDataProcessor):

    def process(self, df):
        df = df.copy()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Convert numeric columns
        numeric_columns = [
            "Employee_ID",
            "Age",
            "Salary",
            "Performance_Score",
            "Experience_Years"
        ]

        for column in numeric_columns:
            if column in df.columns:
                df[column] = pd.to_numeric(
                    df[column], errors="coerce"
                )

        # Convert joining date
        if "Joining_Date" in df.columns:
            df["Joining_Date"] = pd.to_datetime(
                df["Joining_Date"], errors="coerce"
            )

        # Fill numeric missing values with median
        for column in numeric_columns:
            if column in df.columns:
                df[column] = df[column].fillna(df[column].median())

        # Fill text missing values
        for column in df.select_dtypes(include="object").columns:
            df[column] = df[column].fillna("Unknown")

        # Remove rows with invalid dates
        if "Joining_Date" in df.columns:
            df = df.dropna(subset=["Joining_Date"])

        return df

    def clean(self, df):
        return self.process(df)
class EmployeeDataProcessor(DataCleaner):

    def __init__(self):
        super().__init__()

    def process(self, df):
        return super().process(df)