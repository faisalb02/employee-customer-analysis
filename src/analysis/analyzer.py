import pandas as pd
import numpy as np


class DataAnalyzer:

    def __init__(self, df):
        self.df = df.copy()

    def department_summary(self):
        summary = (
            self.df.groupby("Department")
            .agg(
                employee_count=("Employee_ID", "count"),
                average_salary=("Salary", "mean"),
                total_salary=("Salary", "sum")
            )
            .reset_index()
        )

        return summary

    def salary_statistics(self):
        salary = self.df["Salary"].dropna()

        return {
            "mean": np.mean(salary),
            "sum": np.sum(salary),
            "std": np.std(salary),
            "min": np.min(salary),
            "max": np.max(salary)
        }

    def experience_salary_correlation(self):
        return self.df["Experience_Years"].corr(
            self.df["Salary"]
        )

    def joining_trend(self):
        data = self.df.copy()

        data["Joining_Date"] = pd.to_datetime(
            data["Joining_Date"],
            errors="coerce"
        )

        data["Joining_Year"] = data["Joining_Date"].dt.year

        return (
            data.groupby("Joining_Year")
            .size()
            .reset_index(name="Employee_Count")
        )

    def findings(self):
        summary = self.department_summary()

        highest_salary = summary.loc[
            summary["average_salary"].idxmax(),
            "Department"
        ]

        largest_department = summary.loc[
            summary["employee_count"].idxmax(),
            "Department"
        ]

        stats = self.salary_statistics()

        correlation = self.experience_salary_correlation()

        return [
            f"{largest_department} has the highest employee count.",
            f"{highest_salary} has the highest average salary.",
            f"Average salary is {stats['mean']:.2f}.",
            f"Salary standard deviation is {stats['std']:.2f}.",
            f"Experience and salary correlation is {correlation:.2f}."
        ]

    def analyze(self):
        return self.findings()

