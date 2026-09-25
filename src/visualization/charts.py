import matplotlib.pyplot as plt
from pathlib import Path


class VisualizationManager:

    def __init__(self, df, output_dir="outputs/charts"):
        self.df = df
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def create_charts(self):

        # 1. Average salary by department
        dept_salary = self.df.groupby("Department")["Salary"].mean()
        dept_salary.plot(kind="bar")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.tight_layout()
        plt.savefig(self.output_dir / "average_salary_by_department.png")
        plt.close()

        # 2. Cumulative joining trend
        joining = self.df.copy()
        joining["Joining_Year"] = joining["Joining_Date"].dt.year
        trend = joining.groupby("Joining_Year").size().sort_index().cumsum()
        trend.plot(kind="line", marker="o")
        plt.title("Cumulative Joining Trend")
        plt.xlabel("Year")
        plt.ylabel("Cumulative Employees")
        plt.tight_layout()
        plt.savefig(self.output_dir / "cumulative_joining_trend.png")
        plt.close()

        # 3. Salary distribution
        self.df["Salary"].plot(kind="hist", bins=20)
        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Employees")
        plt.tight_layout()
        plt.savefig(self.output_dir / "salary_distribution.png")
        plt.close()

        # 4. Experience vs salary
        plt.scatter(
            self.df["Experience_Years"],
            self.df["Salary"]
        )
        plt.title("Experience vs Salary")
        plt.xlabel("Experience Years")
        plt.ylabel("Salary")
        plt.tight_layout()
        plt.savefig(self.output_dir / "experience_vs_salary.png")
        plt.close()

        # 5. Headcount share
        headcount = self.df["Department"].value_counts()
        headcount.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Department Headcount Share")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(self.output_dir / "headcount_share.png")
        plt.close()