import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# #1 Load data
df_sales = pd.read_csv('Processed_Sales_Data.csv')

# # 2. Load the data (assuming sales data is already cleaned)
df_sales = pd.read_csv('sale_data1.csv')

# # 3. Preprocess the data
# # Convert the sale_date to datetime format
# df_sales['sale_date'] = pd.to_datetime(df_sales['sale_date'])

# # Extract year and month for time series modeling
# df_sales['year'] = df_sales['sale_date'].dt.year
# df_sales['month'] = df_sales['sale_date'].dt.month

# # Group the sales by month and year to aggregate total sales
# monthly_sales = df_sales.groupby(['year', 'month'])['total_amount'].sum().reset_index()

# # Create a time index for the time series model
# monthly_sales['time_index'] = monthly_sales['year'] * 12 + monthly_sales['month'] - 1

# # 4. Visualize the Data
# # Plot total sales over time
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_sales['time_index'], monthly_sales['total_amount'], marker='o', color='b')
# plt.title('Total Sales Over Time')
# plt.xlabel('Time Index (Year-Month)')
# plt.ylabel('Total Sales Amount')
# plt.grid(True)
# plt.show()

# # 5. Modeling with Linear Regression
# # Prepare the data for modeling
# X = monthly_sales[['time_index']]  # Independent variable (time index)
# y = monthly_sales['total_amount']  # Dependent variable (sales)

# # Split the data into training and testing sets (80% train, 20% test)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# # Initialize and train the linear regression model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predict the sales on the testing set
# y_pred = model.predict(X_test)

# # 6. Evaluation and Insights
# # Calculate the mean squared error (MSE)
# mse = mean_squared_error(y_test, y_pred)

# # Plot actual vs predicted sales
# plt.figure(figsize=(10, 6))
# plt.plot(X_test, y_test, label='Actual Sales', marker='o', color='blue')
# plt.plot(X_test, y_pred, label='Predicted Sales', marker='x', color='red')
# plt.title('Actual vs Predicted Sales')
# plt.xlabel('Time Index (Year-Month)')
# plt.ylabel('Total Sales Amount')
# plt.legend()
# plt.grid(True)
# plt.show()


