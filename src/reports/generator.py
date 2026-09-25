import json
import os


class ReportGenerator:

    def __init__(self):
        os.makedirs("outputs/reports", exist_ok=True)

    def generate(self, results):

        report = f"""# Employee Analysis Report

## Dataset Overview

- Total Employees: {results['total_employees']}
- Average Salary: {results['average_salary']:.2f}
- Minimum Salary: {results['minimum_salary']:.2f}
- Maximum Salary: {results['maximum_salary']:.2f}
- Average Experience: {results['average_experience']:.2f} years

## Department Salary

"""

        for dept, salary in results["department_salary"].items():
            report += f"- {dept}: {salary:.2f}\n"

        report += """
## Key Findings

1. The dataset contains 10,000 employees.
2. Salary varies across departments.
3. Employee experience can be compared with salary.
4. Department headcount varies across departments.
5. The dataset was cleaned and enriched with department information.
"""

        with open(
            "outputs/reports/analysis_report.md",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(report)

        with open(
            "outputs/analysis_summary.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(results, file, indent=4)

        with open(
            "outputs/analysis_summary.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(report)

        print("Reports generated successfully.")