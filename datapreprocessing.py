# data_preprocessing_with_plot.py

# --------------------------
# IMPORT LIBRARIES
# --------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# READ DATA
# --------------------------
csv_path = "D:/practice/dataframe/employee.csv"
json_path = "D:/practice/dataframe/employee.json"
processed_path = "D:/practice/dataframe/employee_processed.csv"

# Read CSV and JSON into DataFrames
df_csv = pd.read_csv(csv_path)
df_json = pd.read_json(json_path)

print("CSV Data Preview:\n", df_csv.head())
print("\nJSON Data Preview:\n", df_json.head())

# --------------------------
# BASIC DATA PRE-PROCESSING
# --------------------------
# Handle missing values
df_csv['Age'].fillna(df_csv['Age'].mean(), inplace=True)
df_csv['Salary'].fillna(df_csv['Salary'].mean(), inplace=True)

# Handle outliers using IQR
for col in ['Age', 'Salary']:
    Q1 = df_csv[col].quantile(0.25)
    Q3 = df_csv[col].quantile(0.75)
    IQR = Q3 - Q1
    df_csv[col] = np.clip(df_csv[col], Q1 - 1.5*IQR, Q3 + 1.5*IQR)

# --------------------------
# DATA MANIPULATION
# --------------------------
# Filtering: Employees with Salary > 45000
high_salary = df_csv[df_csv['Salary'] > 45000]
print("\nFiltered Employees (Salary > 45000):\n", high_salary)

# Sorting: Sort by Salary descending
sorted_salary = df_csv.sort_values(by='Salary', ascending=False)
print("\nEmployees Sorted by Salary (Descending):\n", sorted_salary)

# Grouping: Average Salary by Department
avg_salary_dept = df_csv.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", avg_salary_dept)

# Transformation: Add new column Salary_in_K
df_csv['Salary_in_K'] = df_csv['Salary'] / 1000
print("\nTransformed DataFrame:\n", df_csv)

# Save processed CSV
df_csv.to_csv(processed_path, index=False)
print(f"\nProcessed CSV saved at: {processed_path}")

# --------------------------
# VISUALIZATIONS
# --------------------------
# 1. Boxplot of Salary (to see outliers)
plt.figure(figsize=(8,5))
sns.boxplot(y=df_csv['Salary'])
plt.title("Boxplot of Employee Salary")
plt.ylabel("Salary")
plt.show()

# 2. Histogram of Age
plt.figure(figsize=(8,5))
plt.hist(df_csv['Age'], bins=8, color='skyblue', edgecolor='black')
plt.title("Histogram of Employee Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 3. Bar plot: Average Salary by Department
plt.figure(figsize=(8,5))
avg_salary_dept.plot(kind='bar', color='orange')
plt.title("Average Salary by Department")
plt.ylabel("Average Salary")
plt.xlabel("Department")
plt.show()

# 4. Scatter plot: Age vs Salary
plt.figure(figsize=(8,5))
plt.scatter(df_csv['Age'], df_csv['Salary'], color='green')
plt.title("Scatter Plot: Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
