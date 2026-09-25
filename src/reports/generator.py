import json
from pathlib import Path


class ReportGenerator:

    def generate(self, results):

        output_dir = Path("outputs/reports")
        output_dir.mkdir(parents=True, exist_ok=True)

        # Convert results to text
        if isinstance(results, list):
            findings = results
        else:
            findings = [str(results)]

        # Markdown report
        report = "# Employee Data Analysis Report\n\n"
        report += "## Key Findings\n\n"

        for i, finding in enumerate(findings, 1):
            report += f"{i}. {finding}\n"

        with open(
            output_dir / "analysis_report.md",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(report)

        # JSON summary
        summary = {
            "findings": findings
        }

        with open(
            "outputs/analysis_summary.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(summary, file, indent=4)

        # TXT summary
        with open(
            "outputs/analysis_summary.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write("Employee Data Analysis Summary\n\n")

            for i, finding in enumerate(findings, 1):
                file.write(f"{i}. {finding}\n")

        print("Reports generated successfully.")