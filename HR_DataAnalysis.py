import pandas as pd

# Replace 'your_dataset.csv' with the actual path or URL to your dataset
file_path = 'HR-Employee-Attrition.csv'

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to inspect the data
# print(df.head())

# Define a list of redundant column names
redundant_columns = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber', 
                     'HourlyRate', 'DailyRate', 'MonthlyRate']

# Drop the redundant columns from the DataFrame
df = df.drop(columns=redundant_columns)

# Display the updated DataFrame
# print(df.head())

# Assuming 'df' is your DataFrame
# Use the drop_duplicates method to remove duplicate rows
df = df.drop_duplicates()

# Reset the index to have continuous integer indices (optional)
df = df.reset_index(drop=True)

# Display the updated DataFrame
# print(df.head())

# List of columns to check for missing values
columns_with_missing_values = [
    'Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome','EducationField',
    'EnvironmentSatisfaction', 'Gender','JobInvolvement', 'JobLevel',
    'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
    'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears',
    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

# Handle missing values by either removing rows or imputing values
for column in columns_with_missing_values:
    if df[column].dtype == 'object':
        # For categorical columns, you can replace missing values with a specific category or mode
        df[column].fillna('Unknown', inplace=True)
    else:
        # For numeric columns, you can replace missing values with the mean or median
        df[column].fillna(df[column].median(), inplace=True)

# Display the updated DataFrame
# print(df.head())

# Create a new feature 'TotalYearsWithCompany'
df['TotalYearsWithCompany'] = df['YearsAtCompany'] + df['YearsInCurrentRole'] + df['YearsSinceLastPromotion'] + df['YearsWithCurrManager']

# Display the updated DataFrame
print(df.head())


# Calculate the average MonthlyIncome by JobRole
income_by_jobrole = df.groupby('JobRole')['MonthlyIncome'].mean().reset_index()
income_by_jobrole.rename(columns={'MonthlyIncome': 'AvgMonthlyIncome'}, inplace=True)

# Display the result
print(income_by_jobrole)


# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the correlation matrix for numeric variables
numeric_variables = df.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_variables.corr()

# Create a correlation heatmap using Seaborn
plt.figure(figsize=(12, 8))  # Adjust the figure size if needed
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numeric Variables')
# plt.show()

# # Count the number of employees in each Overtime category
overtime_counts = df['OverTime'].value_counts()

# # Create a bar chart for Overtime
plt.figure(figsize=(8, 6))
sns.barplot(x=overtime_counts.index, y=overtime_counts.values, palette='viridis')
plt.title('Distribution of Overtime')
plt.xlabel('Overtime')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# # Count the number of employees in each MaritalStatus category
marital_counts = df['MaritalStatus'].value_counts()

# # Create a bar chart for Marital Status
plt.figure(figsize=(8, 6))
sns.barplot(x=marital_counts.index, y=marital_counts.values, palette='magma')
plt.title('Distribution of Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()



# Create a scatter plot for Overtime vs. Age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='OverTime', data=df, hue='OverTime', palette='Set2')
plt.title('Relationship between Overtime and Age')
plt.xlabel('Age')
plt.ylabel('Overtime')
plt.show()


# # Create a box plot for Total Working Years vs. Education Level
plt.figure(figsize=(10, 6))
sns.boxplot(x='Education Level', y='TotalWorkingYears', data=df, palette='viridis')
plt.title('Relationship between Education Level and Total Working Years')
plt.xlabel('Education Level')
plt.ylabel('Total Working Years')
plt.xticks(rotation=45)
plt.show()


# Create a scatter plot for Number of Companies Worked vs. Distance from Home
plt.figure(figsize=(10, 6))
sns.scatterplot(x='NumCompaniesWorked', y='DistanceFromHome', data=df, hue='NumCompaniesWorked', palette='plasma')
plt.title('Relationship between Number of Companies Worked and Distance from Home')
plt.xlabel('Number of Companies Worked')
plt.ylabel('Distance from Home')
plt.show()

# Export your DataFrame to a CSV file
df.to_csv('cleaned_hr_data.csv', index=False)


