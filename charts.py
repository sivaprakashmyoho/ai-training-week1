import pandas as pd
import matplotlib.pyplot as plt

# Read employees.csv
df = pd.read_csv("employees.csv")


# 1. BAR CHART - Average salary per department

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(plt.gca().containers[0], fmt="%.0f")

plt.savefig("average_salary.png")
plt.show()


# 2. HISTOGRAM - Salary distribution

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.savefig("salary_histogram.png")
plt.show()


# 3. SCATTER PLOT - Employee ID vs Salary

plt.figure(figsize=(8, 5))

for department in df["department"].unique():

    data = df[df["department"] == department]

    plt.scatter(
        data["id"],
        data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

plt.legend()

plt.savefig("employee_scatter.png")
plt.show()


# 4. LINE CHART - Monthly sales

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("monthly_sales.png")
plt.show()

print("All 4 charts saved successfully!")
