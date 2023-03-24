# ANALYSING DATA AS PRACTICE USING PANDAS. CASE - WHY ARE STAFF LEAVING?
import pandas as pd
import matplotlib.pyplot as plt

file = "/Data analysis/Metadata-Table 1.csv"

# MAKE FILE ACCESSIBLE AND CHECK DATA
data = pd.read_csv(file)
col_names = data.columns.tolist()  # places all column names in list
print("COLUMN NAMES:")
print(col_names)
print("\nSAMPLE DATA:")
print(data.head())  # .head() method is quick tool to check sample of data for correct inputs

# CHECK DATA TYPE
print(f"\nDATA TYPE FOR COLUMNS:\n{data.dtypes}")

# CHECK FOR MISSING VALUES WITHIN DATA SET
print(f"\nCHECK FOR MISSING VALUES:\n{data.isnull().any()}")

# NUMBER OF CURRENT STAFF AND LEAVERS
print(f"\nCURRENT STAFF(0) AND LEAVERS(1)\n{data['Left'].value_counts()}\n")

# GET MEAN AVERAGES VIA CURRENT AND STAFF LEFT FOR EACH COLUMN
print(f"\nAVERAGES VIA LEFT FOR EACH COLUMN\n{data.groupby('Left').mean()}\n")  # .groupby() method is a useful tool
# to check averages


# DATA VISUALISATION
# Bar chart to show turnover via performance rating
pd.crosstab(data.PerformanceRating, data.Left).plot(kind='bar')
plt.xlabel('Performance rating')
plt.ylabel('Frequency of turnover')

# Stacked bar chart to show turnover based on monthly income
table = pd.crosstab(data.BusinessTravel, data.Left)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Employee turnover and monthly income')
plt.xlabel('Monthly income')
plt.ylabel('Proportion of employees')


plt.show()
