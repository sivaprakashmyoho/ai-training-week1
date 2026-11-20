# Customer Data Analysis Project

## 1. Project Overview
This project focuses on analysing customer data using Python and Pandas. The goal is to understand customer distribution across different cities and perform basic data exploration.

## 2. Dataset Details
- Dataset: Customer CSV Dataset
- Total Records: 4
- Total Columns: 3
- Columns: ID, Name, City

## 3. Technologies Used
- Python
- Pandas
- Jupyter Notebook

## 4. Data Exploration
The following operations were performed:
- Dataset shape
- Dataset information using `info()`
- Statistical summary using `describe()`
- Missing value checking
- Duplicate row checking

## 5. Business Questions
1. How many customers are in the dataset?
2. Which city has the highest number of customers?
3. How many customers belong to Chennai?
4. Which cities have customers?
5. What percentage of customers belong to each city?

## 6. Key Findings
- Total customers: 4
- Chennai: 2 customers (50%)
- Mumbai: 1 customer (25%)
- Bangalore: 1 customer (25%)
- Missing values: 0
- Duplicate rows: 0

## 7. Project Structure
```text
employee-data-analysis/
├── data/
│   └── employees.csv
├── notebooks/
│   └── employee_analysis.ipynb
└── README.md
```

## 8. Conclusion
The analysis shows that Chennai has the highest number of customers in this dataset. This project demonstrates basic data exploration and analysis using Pandas.

Note: This is a small practice dataset containing only four records.


# Employee Data Cleaning and Analysis

## Project Overview
This project focuses on cleaning and preparing the IBM HR Analytics Employee Attrition dataset using Python and Pandas.

## Dataset Information
- Total records: 1,470
- Total columns: 35
- File: `data/ibm_hr.csv`

## Tools and Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Data Cleaning Steps

### 1. Missing Values
- Checked missing values in all columns.
- No missing values were found.
- No filling or deletion was required.

### 2. Duplicate Records
- Checked for duplicate records.
- Duplicates found: 0.
- No records were removed.

### 3. Data Types
- Inspected numeric and categorical columns.
- Numeric columns were already stored as numeric types.
- Categorical columns were already stored as text.
- No date columns required conversion.

### 4. Text Standardisation
- Applied whitespace trimming to categorical columns using `str.strip()`.
- Existing category values were preserved.

### 5. Outlier Detection
- Used the Interquartile Range (IQR) method.
- Excluded EmployeeNumber, EmployeeCount, and StandardHours from outlier detection.
- Identified potential outliers in several numeric columns.
- Reviewed the results and retained the records because statistical outliers are not necessarily invalid data.

## Before and After Summary

| Metric | Before | After |
|---|---:|---:|
| Rows | 1470 | 1470 |
| Missing Values | 0 | 0 |
| Duplicates | 0 | 0 |

## Output Files
- `data/clean_data.csv` – cleaned dataset.
- `data/before_after_summary.csv` – cleaning summary.
- `notebooks/data_cleaning.ipynb` – data cleaning notebook.

## Conclusion
The dataset was inspected and cleaned successfully. It contains 1,470 rows and 35 columns. No missing values or duplicate records were found. Potential outliers were identified using IQR and retained after review.

The cleaned dataset is ready for further exploratory data analysis (EDA).

## 8. Conclusion

In this project, I performed Exploratory Data Analysis (EDA)
using Python, Pandas, and NumPy.

### Key Activities
- Calculated summary statistics.
- Analyzed department-wise employee salaries.
- Performed correlation analysis.
- Answered five business questions.
- Merged employee and department budget tables.
- Created a pivot table.

### Final Note
The dataset contains four records. Department, gender, age,
and salary values were added as illustrative sample data
for practice purposes. Therefore, the findings are not
representative of a real company's workforce.

## Part 2 – Employee Data Visualisation

### Project Overview
Created five visualisations using Python, Pandas, Matplotlib and Seaborn to analyse the IBM HR Employee Attrition dataset.

### Dataset Information
- Total Records: 1,470
- Total Columns: 35
- Missing Values: 0

### Visualisations
1. **Bar Chart:** Employee Count by Department
2. **Histogram:** Employee Age Distribution
3. **Scatter Plot:** Monthly Income vs Years at Company
4. **Line Chart:** Sorted Employee Monthly Income
5. **Heatmap:** Employee Data Correlation

### Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

### Project Outputs
All five visualisation images are saved in `reports/figures/`.

### Key Learning Outcomes
- Data visualisation using Matplotlib and Seaborn
- Understanding employee data distributions
- Analysing relationships between numerical variables
- Communicating insights through charts