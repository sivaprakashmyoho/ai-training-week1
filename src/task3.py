
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

print("Task 3 started successfully!")


# ==============================
# PART 1: NUMPY OPERATIONS
# ==============================

# Marks of 4 students in 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 95],
    [72, 80, 78]
])

# Print array and shape
print("\nOriginal Marks:")
print(marks)

print("Shape:", marks.shape)

# Student averages (axis=1)
student_averages = np.mean(marks, axis=1)
print("Student averages:", student_averages)

# Subject averages (axis=0)
subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("\nMarks after grace marks:")
print(grace_marks)

# Weighted scores using np.dot
weights = np.array([0.3, 0.3, 0.4])

weighted_scores = np.dot(marks, weights)

print("\nWeighted scores:")
print(weighted_scores)


# ==============================
# PART 2: PANDAS BASICS
# ==============================

# Load employee CSV
df = pd.read_csv(DATA_DIR / "employees.csv")

# Display first 5 rows
print("\nEmployee Data:")
print(df.head())

# DataFrame information
print("\nDataFrame Information:")
df.info()

# Statistical description
print("\nStatistical Description:")
print(df.describe())

# Select rows using loc
print("\nUsing loc:")
print(df.loc[0:2, ["name", "department", "salary"]])

# Select rows using iloc
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filter employees with salary above 50000
print("\nEmployees earning above 50000:")
print(df[df["salary"] > 50000])

# Filter IT department employees
print("\nIT Department Employees:")
print(df[df["department"] == "IT"])


# PART 2: PANDAS BASICS

df = pd.read_csv(DATA_DIR / "employees.csv")

print("\nEmployee Data:")
print(df.head())


# ==============================
# PART 3: DATA CLEANING
# ==============================

# Create a dataset with missing salaries
dirty_df = df.copy()

dirty_df.loc[0, "salary"] = np.nan
dirty_df.loc[1, "salary"] = np.nan

# Add one duplicate row
dirty_df = pd.concat(
    [dirty_df, dirty_df.iloc[[2]]],
    ignore_index=True
)

# Save dirty dataset
dirty_df.to_csv(
    DATA_DIR / "employees_task3.csv",
    index=False
)

print("\nBefore Cleaning:")
print("Rows:", len(dirty_df))
print("Missing salaries:", dirty_df["salary"].isna().sum())
print("Duplicate rows:", dirty_df.duplicated().sum())

# Remove duplicate rows
clean_df = dirty_df.drop_duplicates().copy()

# Fill missing salaries with median
median_salary = clean_df["salary"].median()

clean_df["salary"] = clean_df["salary"].fillna(median_salary)

# Correct data types
clean_df["id"] = clean_df["id"].astype(int)
clean_df["salary"] = clean_df["salary"].astype(int)
clean_df["name"] = clean_df["name"].astype(str)
clean_df["department"] = clean_df["department"].astype(str)
clean_df["city"] = clean_df["city"].astype(str)

# Display cleaned data
print("\nAfter Cleaning:")
print(clean_df)

print("\nMissing salaries:", clean_df["salary"].isna().sum())
print("Duplicate rows:", clean_df.duplicated().sum())

# Save cleaned dataset
clean_df.to_csv(
    DATA_DIR / "employees_cleaned.csv",
    index=False
)
clean_df.to_csv(DATA_DIR / "employees_cleaned.csv", index=False)
# ==============================
# PART 4: DEPARTMENT ANALYSIS
# ==============================

departments = pd.DataFrame({
    "department": ["Sales", "HR", "IT", "Finance", "Marketing"],
    "head": ["Arun", "Priya", "Rahul", "Karthik", "Meena"],
    "budget": [120000, 80000, 200000, 150000, 90000]
})

departments.to_csv(DATA_DIR / "departments.csv", index=False)

departments_df = pd.read_csv(DATA_DIR / "departments.csv")

print("\nDepartment Data:")
print(departments_df)

# GroupBy and Aggregation
department_summary = clean_df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\nDepartment Summary:")
print(department_summary)

# Inner Join
inner_join = pd.merge(
    department_summary,
    departments_df,
    on="department",
    how="inner"
)

print("\nInner Join:")
print(inner_join)

# Left Join
left_join = pd.merge(
    department_summary,
    departments_df,
    on="department",
    how="left"
)

print("\nLeft Join:")
print(left_join)

# Outer Join
outer_join = pd.merge(
    department_summary,
    departments_df,
    on="department",
    how="outer",
    indicator=True
)

print("\nOuter Join:")
print(outer_join)

# Departments without employees
no_employees = outer_join.loc[
    outer_join["_merge"] == "right_only",
    "department"
]

print("\nDepartments with no employees:")
print(no_employees.tolist())

# ==============================
# PART 5: DATA VISUALIZATION
# ==============================

# 1. BAR CHART - Employee Count by Department

plt.figure(figsize=(8, 5))

plt.bar(
    department_summary["department"],
    department_summary["headcount"],
    label="Employee Count"
)

plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.legend()

plt.savefig(REPORTS_DIR / "bar_chart.png")
plt.close()

print("\nBar chart saved successfully!")
print("Insight: IT has the highest number of employees.")
# 2. HISTOGRAM - Salary Distribution

plt.figure(figsize=(8, 5))

plt.hist(
    clean_df["salary"],
    bins=5,
    label="Employee Salaries"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()

plt.savefig(REPORTS_DIR / "histogram.png")
plt.close()

print("\nHistogram saved successfully!")
print("Insight: Most salaries fall between 48000 and 75000.")
# 3. SCATTER PLOT - Employee Salary

plt.figure(figsize=(8, 5))

plt.scatter(
    clean_df["id"],
    clean_df["salary"],
    label="Employee Salary"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.savefig(REPORTS_DIR / "scatter_plot.png")
plt.close()

print("\nScatter plot saved successfully!")
print("Insight: Karthik has the highest salary of 90000.")
# 4. LINE CHART - Average Salary by Department

plt.figure(figsize=(8, 5))

plt.plot(
    department_summary["department"],
    department_summary["average_salary"],
    marker="o",
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()

plt.savefig(REPORTS_DIR / "line_chart.png")
plt.close()

print("\nLine chart saved successfully!")
print("Insight: Finance has the highest average salary.")