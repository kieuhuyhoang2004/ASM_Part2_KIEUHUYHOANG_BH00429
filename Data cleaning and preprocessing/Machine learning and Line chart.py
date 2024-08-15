import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# #1 Load data
df_sales = pd.read_csv('Processed_Sales_Data.csv')

# # 2. Load the data (assuming sales data is already cleaned)
df_sales = pd.read_csv('sale_data1.csv')


# Preprocessing the data
df_sales['sale_date'] = pd.to_datetime(df_sales['sale_date'])

# Aggregate sales data by month to get total monthly sales
monthly_sales = df_sales.resample('M', on='sale_date').sum()

# Use the 'total_amount' column for forecasting
sales_data = monthly_sales['total_amount']

# Split the data into training and test sets
train_data = sales_data[:-12]  # Use all data except the last 12 months for training
test_data = sales_data[-12:]   # Use the last 12 months for testing

# Train the Holt-Winters Exponential Smoothing model
model = ExponentialSmoothing(train_data, seasonal='add', seasonal_periods=12).fit()

# Generate predictions
predictions = model.forecast(steps=12)

# Plot the historical data, test data, and predictions
plt.figure(figsize=(14, 7))
plt.plot(sales_data.index, sales_data, label='Historical Sales')
plt.plot(test_data.index, test_data, label='Actual Sales', color='orange')
plt.plot(predictions.index, predictions, label='Predicted Sales', color='red', linestyle='--')
plt.title('Sales Forecasting')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.legend()
plt.grid(True)
plt.show()