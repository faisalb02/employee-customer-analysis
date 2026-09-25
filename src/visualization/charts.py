import os
import matplotlib.pyplot as plt


class VisualizationManager:

    def __init__(self, output_dir="outputs/charts"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_charts(self, df):

        # 1. Average Salary by Department
        avg_salary = df.groupby("Department")["Salary"].mean()

        plt.figure(figsize=(8, 5))
        avg_salary.plot(kind="bar")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/average_salary_by_department.png")
        plt.close()

        # 2. Cumulative Joining Trend
        joining = (
            df.groupby("Joining_Date")
            .size()
            .sort_index()
            .cumsum()
        )

        plt.figure(figsize=(8, 5))
        joining.plot(kind="line")
        plt.title("Cumulative Employee Joining Trend")
        plt.xlabel("Joining Date")
        plt.ylabel("Cumulative Employees")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/cumulative_joining_trend.png")
        plt.close()

        # 3. Salary Distribution
        plt.figure(figsize=(8, 5))
        df["Salary"].plot(kind="hist", bins=20)
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Employees")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/salary_distribution.png")
        plt.close()

        # 4. Experience vs Salary
        plt.figure(figsize=(8, 5))
        plt.scatter(df["Experience_Years"], df["Salary"], alpha=0.5)
        plt.title("Experience vs Salary")
        plt.xlabel("Experience (Years)")
        plt.ylabel("Salary")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/experience_vs_salary.png")
        plt.close()

        # 5. Headcount Share
        headcount = df["Department"].value_counts()

        plt.figure(figsize=(7, 7))
        headcount.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Employee Headcount Share by Department")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/headcount_share.png")
        plt.close()

        print("5 charts created successfully.")