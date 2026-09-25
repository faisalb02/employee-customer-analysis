import pandas as pd

from data.loader import DataLoader
from data.cleaner import DataCleaner
from analysis.analyzer import DataAnalyzer
from visualization.charts import VisualizationManager
from reports.generator import ReportGenerator
from api.client import APIClient


def main():

    # Load dataset
    loader = DataLoader("data/raw/employees.csv")
    df = loader.load_data()

    print("Original Dataset:")
    loader.inspect_data(df)

    # Clean dataset
    cleaner = DataCleaner()
    cleaned_df = cleaner.clean(df)

    # Save cleaned dataset
    cleaned_df.to_csv(
        "data/processed/cleaned_employees.csv",
        index=False
    )

    print("\nCleaned Dataset:")
    print(cleaned_df.head())
    print("Cleaned Shape:", cleaned_df.shape)

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
    analyzer = DataAnalyzer()
    results = analyzer.analyze(cleaned_df)

    print("\nAnalysis Results:")
    print(results)

    # Create charts
    visualizer = VisualizationManager()
    visualizer.create_charts(cleaned_df)
    # Generate reports
    report_generator = ReportGenerator()
    report_generator.generate(results)

    # API integration
    api_client = APIClient("https://jsonplaceholder.typicode.com/posts/1")
    api_data = api_client.get_data()

    if api_data:
        print("API integration successful.")


if __name__ == "__main__":
    main()