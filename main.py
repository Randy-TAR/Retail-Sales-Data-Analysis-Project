
import pandas as pd 
import numpy as np 
import matplotlib as plt 

retail_sales = pd.read_csv("retail_sales - retail_sales.csv.csv" )
column_names=retail_sales.head(0)
# print(retail_sales.shape)

# checking the duplicates and remove empty values
retail_sales = retail_sales.drop_duplicates().dropna()



#  converting the data columns
retail_sales['Date'] = pd.to_datetime(retail_sales["Date"])
retail_sales['Quantity'] = pd.to_numeric(retail_sales['Quantity'])
retail_sales['UnitPrice'] = pd.to_numeric(retail_sales['UnitPrice'])
# print(retail_sales.info())

# removing negative values in quantity and unitprice
retail_sales = retail_sales[retail_sales["Quantity"] >= 0]
retail_sales = retail_sales[retail_sales["UnitPrice"] >= 0]

# creating a TotalPrice column
# retail_sales['TotalPrice'] = retail_sales['Quantity'] * retail_sales['UnitPrice']
retail_sales['TotalPrice'] = np.multiply(retail_sales["Quantity"], retail_sales["UnitPrice"])

# extract Year, Month, DayOfWeek
retail_sales['Year'] = retail_sales['Date'].dt.year
retail_sales['Month'] = retail_sales['Date'].dt.month
retail_sales['DayOfWeek'] = retail_sales['Date'].dt.day_name()

# dayofweek return 0 for Monday, 1 for Tuesday ... 6 for Sunday
retail_sales["DayType"] = retail_sales["Date"].dt.dayofweek
retail_sales["DayType"] = np.where(
    (retail_sales["DayType"] == 5) | (retail_sales["DayType"] == 6),
    "WeekEnd",
    "WeekDay"
)

# total sales of the years
total_sales_of_year = retail_sales["TotalPrice"].sum()
# print(total_sales_of_year)

# Group  Product and sum them then find the top 5
product_sales = retail_sales.groupby("ProductCategory")["TotalPrice"].sum()
top5_products = product_sales.sort_values(ascending=False).head(5)
# print(top5_products)

# Sum total sales per month
monthly_sales = retail_sales.groupby("Month")["TotalPrice"].sum()
highest_sales = monthly_sales.max() 
best_month = monthly_sales.idxmax()
# print(best_month)
# print(highest_sales)

# The most common payment method
most_common_payment_method = retail_sales["PaymentMethod"].mode()[0]
# print(most_common_payment_method)

# Average order value per store
avg_order_per_store = retail_sales.groupby("StoreID")["TotalPrice"].mean()
print(avg_order_per_store)

       


# print(retail_sales.dtypes)
# first10 = retail_sales.head(10)
# print(first10)



