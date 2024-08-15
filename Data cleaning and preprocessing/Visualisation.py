import pandas as pd 
import matplotlib.pyplot as plt

#Load data from CSV files
df_customers = pd.read_csv('customers1.csv')
df_MarketTrendData = pd.read_csv('MarketTrendData.csv')
df_ProductDetailData = pd.read_csv('ProductDetailData.csv')
df_ProductGroupTable = pd.read_csv('ProductGroupTable.csv')
df_sales = pd.read_csv('sale_data1.csv')
df_WebsiteAccessCategoryData = pd.read_csv('WebsiteAccessCategoryData.csv')

# Line Chart: Distribution of Customer Registrations over Time
#df_customers['RegistrationDate'] = pd.to_datetime(df_customers['RegistrationDate'])
#registrations_per_month = df_customers.groupby(df_customers['RegistrationDate'].dt.to_period('M')).size()

#plt.figure(figsize=(10, 6))
#registrations_per_month.plot(kind='line', marker='o')
#plt.title('Distribution of Customer Registrations Over Time')
#plt.xlabel('Month')
#plt.ylabel('Number of Registrations')
#plt.grid(True)
#plt.show()

###################################################################################

# # Convert sale_date to datetime for accurate handling
# df_sales['sale_date'] = pd.to_datetime(df_sales['sale_date'])

# # Group data by product_id and calculate the total sales amount for each product
# total_sales_by_product = df_sales.groupby('product_id')['total_amount'].sum()

# # Create the bar chart
# plt.figure(figsize=(12, 6))
# total_sales_by_product.plot(kind='bar', color='skyblue')
# plt.title('Total Sales by Product')
# plt.xlabel('Product ID')
# plt.ylabel('Total Sales Amount')
# plt.xticks(rotation=90)
# plt.show()

#######################################################################################
# Pie Chart: Proportion of Customers by Type
#customer_type_counts = df_customers['CustomerType'].value_counts()

#plt.figure(figsize=(8, 8))
#customer_type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
#plt.title('Proportion of Customers by Type')
#plt.ylabel('')
#plt.show()

######################################################################################
# Scatter Plot: Session Duration vs. Engagement Score
#plt.figure(figsize=(10, 6))
#plt.scatter(df_WebsiteAccessCategoryData['SessionDuration'], df_WebsiteAccessCategoryData['EngagementScore'], alpha=0.5)
#plt.title('Session Duration vs. Engagement Score')
#plt.xlabel('Session Duration (seconds)')
#plt.ylabel('Engagement Score')
#plt.grid(True)
#plt.show()

###############################################################################
# Histogram: Distribution of Session Duration
#plt.figure(figsize=(10, 6))
#plt.hist(df_WebsiteAccessCategoryData['SessionDuration'], bins=20, color='purple', alpha=0.7)
#plt.title('Distribution of Session Duration')
#plt.xlabel('Session Duration (seconds)')
#plt.ylabel('Frequency')
#plt.grid(True)
#plt.show()


