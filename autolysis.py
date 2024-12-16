import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to analyze a CSV and generate outputs
def analyze_csv(file_path, output_folder):
    # Load the CSV with encoding handling
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            data = pd.read_csv(file_path, encoding='latin1')
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Generate basic analysis
    analysis_report = []
    analysis_report.append(f"# Analysis Report for {os.path.basename(file_path)}\n")

    # Dataset overview
    analysis_report.append("## Dataset Overview\n")
    analysis_report.append(f"Shape: {data.shape}\n")
    analysis_report.append(f"Columns: {', '.join(data.columns)}\n")
    analysis_report.append(f"\n\n{data.describe(include='all')}\n")

    # Null values
    analysis_report.append("## Null Value Analysis\n")
    null_values = data.isnull().sum()
    analysis_report.append(f"\n{null_values}\n")

    # Identify key insights
    analysis_report.append("## Key Insights\n")
    try:
        # Numeric insights
        numeric_data = data.select_dtypes(include=['number'])
        if not numeric_data.empty:
            max_corr_columns = numeric_data.corr().unstack().sort_values(ascending=False).drop_duplicates()
            top_corr = max_corr_columns[(max_corr_columns < 1.0) & (max_corr_columns > 0.7)]
            if not top_corr.empty:
                analysis_report.append(f"Highly correlated columns: {top_corr}\n")

        # Categorical insights
        categorical_data = data.select_dtypes(include=['object', 'category'])
        for column in categorical_data.columns:
            top_category = data[column].value_counts().idxmax()
            analysis_report.append(f"Most common value in {column}: {top_category}\n")
    except Exception as e:
        analysis_report.append(f"Could not compute insights: {e}\n")

    # Create and save visualizations
    analysis_report.append("## Charts\n")
    try:
        # Correlation heatmap for numeric data
        if not numeric_data.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
            heatmap_path = os.path.join(output_folder, "correlation_heatmap.png")
            plt.title("Correlation Heatmap")
            plt.savefig(heatmap_path)
            plt.close()
            analysis_report.append(f"![Correlation Heatmap](correlation_heatmap.png)\n")

        # Distribution of numeric columns
        for column in numeric_data.columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(data[column].dropna(), kde=True, bins=30)
            column_plot_path = os.path.join(output_folder, f"{column}_distribution.png")
            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.savefig(column_plot_path)
            plt.close()
            analysis_report.append(f"![{column} Distribution]({column}_distribution.png)\n")

        # Bar plots for categorical data
        for column in categorical_data.columns:
            plt.figure(figsize=(10, 6))
            data[column].value_counts().head(10).plot(kind='bar', color='skyblue')
            column_plot_path = os.path.join(output_folder, f"{column}_barplot.png")
            plt.title(f"Top 10 Categories of {column}")
            plt.xlabel(column)
            plt.ylabel("Count")
            plt.savefig(column_plot_path)
            plt.close()
            analysis_report.append(f"![{column} Bar Plot]({column}_barplot.png)\n")
    except Exception as e:
        analysis_report.append(f"Error creating visualizations: {e}\n")

    # Save README.md with insights and chart explanations
    with open(os.path.join(output_folder, "README.md"), "w") as readme_file:
        readme_file.write("\n".join(analysis_report))

    print(f"Analysis completed for {file_path}. Outputs saved in {output_folder}.")

# Main script to process multiple files
def main():
    datasets = {
        "goodreads": "goodreads.csv",
        "media": "media.csv",
        "happiness": "happiness.csv"
    }

    for dataset_name, file_path in datasets.items():
        output_folder = dataset_name
        analyze_csv(file_path, output_folder)

if __name__ == "__main__":
    main()
