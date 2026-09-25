import pandas as pd


class DataCleaner:
    def clean(self, df):
        df = df.copy()

        df = df.drop_duplicates()

        df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
        df["Joining_Date"] = pd.to_datetime(
            df["Joining_Date"], errors="coerce"
        )

        df["Salary"] = df["Salary"].fillna(df["Salary"].median())

        df = df.dropna(
            subset=["Employee_ID", "Department", "Joining_Date"]
        )

        return df