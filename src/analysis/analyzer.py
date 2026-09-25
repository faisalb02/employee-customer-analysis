import pandas as pd
import numpy as np


class DataAnalyzer:
    def analyze(self, df):
        result = {}

        result["total_employees"] = int(len(df))
        result["average_salary"] = float(df["Salary"].mean())
        result["maximum_salary"] = float(df["Salary"].max())
        result["minimum_salary"] = float(df["Salary"].min())
        result["average_experience"] = float(
            df["Experience_Years"].mean()
        )

        result["department_salary"] = (
            df.groupby("Department")["Salary"]
            .mean()
            .sort_values(ascending=False)
            .to_dict()
        )

        result["department_count"] = (
            df["Department"]
            .value_counts()
            .to_dict()
        )

        return result