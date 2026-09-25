import pandas as pd

from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.analysis.analyzer import DataAnalyzer
from src.visualization.charts import VisualizationManager
from src.reports.generator import ReportGenerator
from src.api.client import APIClient


def main():

    # Load dataset
    loader = DataLoader("data/raw/employees.csv")
    df = loader.load_data()

    print("Original Dataset:")
    loader.inspect_data(df)

    # Clean dataset
    cleaner = DataCleaner()
    cleaned_df = cleaner.clean(df)

    print("\nCleaned Dataset:")
    print(cleaned_df.head())
    print("Cleaned Shape:", cleaned_df.shape)

    # Save cleaned dataset
    cleaned_df.to_csv(
        "data/processed/cleaned_employees.csv",
        index=False
    )

    # Enrich with department data
    departments_df = pd.read_csv("data/raw/departments.csv")

    merged_df = cleaned_df.merge(
        departments_df,
        on="Department",
        how="left"
    )

    merged_df.to_csv(
        "data/processed/enriched_employees.csv",
        index=False
    )

    print("Department data merged successfully.")
    print("Merged Shape:", merged_df.shape)

    # Analyze dataset
    analyzer = DataAnalyzer(cleaned_df)
    results = analyzer.analyze()

    print("\nAnalysis Results:")
    print(results)

    # Create charts
    visualizer = VisualizationManager(cleaned_df)
    visualizer.create_charts()

    # Generate reports
    report_generator = ReportGenerator()
    report_generator.generate(results)

    # API integration
    api_client = APIClient(
        "https://jsonplaceholder.typicode.com/users"
    )

    api_data = api_client.get_data()

    if api_data:
        print("API integration successful.")


if __name__ == "__main__":
    main()