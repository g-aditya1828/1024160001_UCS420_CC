
import pandas as pd

#ques 1 Create a dataset as follow in the table.  
data = {
    'Tid' : [1,2,3,4,5,6,7,8,9,10],
    'Refund': ['yes', 'no' , 'no' , 'yes' , 'no', 'no' , 'yes' , 'no' , 'no' , 'no'],
    'Marital Status': ['single', 'married', 'single', 'married', 'divorced', 'married', 'divorced', 'single', 'married', 'single'],
    'Taxeable Income': [125000, 100000, 75000, 120000, 95000, 60000, 220000, 85000, 75000, 90000],
    'Cheat' : ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no', 'yes']
    }
# ques 2 From the above table that you have created, locate row 0, 4, 7 and 8 using DataFrame.

df = pd.DataFrame(data)
print(df.loc[[0, 4, 7, 8]])
print(df.loc[0])

#ques 3  Navigate the DataFrame and do the following task for the table created in question 1: 
# 1. Select row from index 3 to 7. 
# 2. Select row from index 4 to 8, and column 2 to 4. 
# 3. Select all rows with column index 1 to 3 (include index 3 during selection).  
print(df.loc[3:7])
print(df.iloc[4:9, 2:5])
print(df.iloc[:, 1:4])

#ques 4 Read a csv file and display its first five rows. 
# Downloaded dataset from https://www.kaggle.com/datasets/uciml/iris)  
path = "D:\\Aditya\\5th semester\\CC lab\\lab3\\Iris.csv"
iris_data = pd.read_csv(path)
print(iris_data.head())

# Q.5 From the csv file (uploaded in the Q.4) delete row 4, and delete column 3. Display the result.  
iris_data.drop(labels = ['PetalWidthCm'], axis=1, inplace=True)
iris_data.drop(iris_data.index[4], axis=0, inplace=True)
print(iris_data.head())

#Q.6 Create a sample dataset (employees.csv) containing information about employees in a company.
employee = {
    'Employee_ID' : [101, 102 , 103 , 104 , 105],
    'name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [5, 8, 10, 3, 12],
    'Joining_Date': ['2018-01-15', '2016-03-22', '2014-07-10', '2019-11-05', '2012-05-30'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4000, 8000],
    'Rating': [4.5, 4.8, 4.2, 4.0, 4.7]
}

df = pd.DataFrame(employee)

#a 
print(df.shape)

#b 
df.info()

#c
print(df.describe())

#d
print(df.head())
print(df.tail(3))

#e 1
df["salary"].mean()
#e 2
df["Bonus"].sum()
#e 3
df["Age"].min()
#e 4
df["Rating"].max()

#f
df_sorted = df.sort_values(by="salary", ascending=False)

#g
def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance_Category"] = df["Rating"].apply(performance_category)

print("\nPerformance Categories:")
print(df[["Employee_ID", "Rating", "Performance_Category"]])

#h
print(df.isnull().sum())

#i
# i) Rename Employee_ID to ID
df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print(df.columns)

#j
# i. More than 5 years of experience
experienced_employees = df[df["Years_of_Experience"] > 5]
print("\nEmployees with more than 5 years of experience:")
print(experienced_employees)


# ii. Belong to IT department
it_employees = df[df["department"] == "IT"]
print("\nEmployees in IT department:")
print(it_employees)


# k) Add Tax column (10% of Salary)
df["Tax"] = df["salary"] * 0.10
print("\nDataFrame with Tax:")
print(df)


# l) Save modified DataFrame to a new CSV file
output_path = r"D:\Aditya\5th semester\CC lab\lab3\Modified_Employees.csv"
df.to_csv(output_path, index=False)
print("\nModified DataFrame saved successfully!")
