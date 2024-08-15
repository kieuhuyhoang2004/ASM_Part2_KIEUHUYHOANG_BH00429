import pandas as pd

#1 Load data from CSV files
df_customers = pd.read_csv('customers1.csv')
df_MarketTrendData = pd.read_csv('MarketTrendData.csv')
df_ProductDetailData = pd.read_csv('ProductDetailData.csv')
df_ProductGroupTable = pd.read_csv('ProductGroupTable.csv')
df_sales = pd.read_csv('sale_data1.csv')
df_WebsiteAccessCategoryData = pd.read_csv('WebsiteAccessCategoryData.csv')


#2 Check and process missing data
# Display the first rows of each DataFrame
#print(df_customers.head())
#print(df_MarketTrendData.head())
#print(df_ProductDetailData.head())
#print(df_ProductGroupTable.head())
#print(df_WebsiteAccessCategoryData.head())
#print(df_sales.head())

# Check the data type and details of each DataFrame
#print(df_customers.info())
#print(df_MarketTrendData.info())
#print(df_ProductDetailData.info())
#print(df_ProductGroupTable.info())
#print(df_WebsiteAccessCategoryData.info())
#print(df_sales.info())

# Descriptive statistics of numeric columns of each DataFrame
#print(df_customers.describe())
#print(df_MarketTrendData.describe())
#print(df_ProductDetailData.describe())
#print(df_ProductGroupTable.describe())
#print(df_WebsiteAccessCategoryData.describe())
#print(df_sales.describe())

#3: Remove duplicate data:
# Check the number of duplicate rows in df_customers
#print("Number of duplicate rows in df_customers:", df_customers.duplicated().sum())
# Remove duplicate rows in df_customers
#df_customers = df_customers.drop_duplicates()
# Check again after removing
#print("Number of duplicate rows after removing in df_customers:", df_customers.duplicated().sum())

# Remove duplicate rows based on 'MarketID' column
#df_MarketTrendData = df_MarketTrendData.drop_duplicates(subset=['MarketID'])
# Check again after removing
#print("Number of duplicate rows after removing in df_MarketTrendData:", df_MarketTrendData.duplicated(subset=['MarketID']).sum())

# Remove duplicate rows but keep the first row
#df_ProductDetailData = df_ProductDetailData.drop_duplicates(keep='first')
# Check again after removing
#print("Number of duplicate rows after removing in df_ProductDetailData:", df_ProductDetailData.duplicated().sum())

# Remove duplicate rows but keep the last row
#df_ProductGroupTable = df_ProductGroupTable.drop_duplicates(keep='last')
# Check again after removing
#print("Number of duplicate rows after removing in df_ProductGroupTable:", df_ProductGroupTable.duplicated().sum())

# Keep only non-duplicated rows
#df_sales = df_sales[~df_sales.duplicated()]
# Check again after removing
#print("Number of duplicate rows after removing in df_sales:", df_sales.duplicated().sum())

# Remove duplicate rows based on columns 'CategoryID' and 'AccessTime'
#df_WebsiteAccessCategoryData = df_WebsiteAccessCategoryData.drop_duplicates(subset=['AccessID', 'AccessDate'])
# Check again after removing
#print("Number of duplicate rows after removing in df_WebsiteAccessCategoryData:", df_WebsiteAccessCategoryData.duplicated(subset=['AccessID', 'AccessDate']).sum())

#4: Normalize and encode data:
# Merge customer data with sales data based on 'CustomerID'
#merged_customer_sales_df = pd.merge(df_customers, df_sales, on='CustomerID')
# Calculate the total quantity of products purchased by each customer
#df_sales['Total Products Bought'] = df_sales.groupby('CustomerID')['Quantity Sold'].transform('sum')

# Merge sales data with product detail data based on 'ProductID'
#merged_sales_product_detail_df = pd.merge(df_sales, df_ProductDetailData, on='ProductID')
# Calculate total cost of products sold
#df_sales['Total Product Cost'] = df_sales['Quantity Sold'] * df_ProductDetailData['Product Cost']

#5 Save the processed DataFrame to CSV files
#df_customers.to_csv('Processed_Customer_Data.csv', index=False)
#df_ProductDetailData.to_csv('Processed_Product_Detail_Data.csv', index=False)
#df_ProductGroupTable.to_csv('Processed_Product_Group_Data.csv', index=False)
#df_MarketTrendData.to_csv('Processed_Market_Trend_Data.csv', index=False)
#df_sales.to_csv('Processed_Sales_Data.csv', index=False)
#df_WebsiteAccessCategoryData.to_csv('Processed_Website_Access_Category_Data.csv', index=False)












