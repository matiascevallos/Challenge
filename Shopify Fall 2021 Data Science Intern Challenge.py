# Question 1
## a. The problem is that there are order that there are orders of 704000, but they are reasonable because there were 2000 items bought. A better
#     way to show something like the AOV could be by getting the average item value and multiply it by the average items ordered (without taking 
#     into account the cases where orders had 20000 items). 

## b. A metric that could be measured could be the median. 

## c. The median is 284. This looks like a better value than the previously mentioned mean, taking into account that shoes are a relative affordable item.

import pandas as pd
import numpy as np

data = pd.read_excel("2019 Winter Data Science Intern Challenge Data Set.xlsx")

# Average item value
data['aiv'] = data['order_amount']/data['total_items']
aiv = data['aiv'].mean()

# Average item value TIMES Average items ordered (with out the orders of 2000 shoes)
modifiedData = np.where(data['total_items'] > 1000, data['total_items'], data['total_items'])
modifiedData = np.delete(modifiedData, np.where(modifiedData == 2000))

aio = modifiedData.mean()
newMetric = aiv*aio

# Average Order Amount per 30 day window
aov = data['order_amount'].mean()

# Get other statistics from the data given
print(data.describe())

# Overall order median 
overallMedian = data['order_amount'].median()

# Print Results
print(newMetric)
print(overallMedian)

# Question 2
## a. 54
##    SELECT COUNT(*) FROM Orders, Shippers WHERE Orders.ShipperId = Shippers.ShipperId AND ShipperName = "Speedy Express";

## b. Peacock (40 orders)
##    SELECT TOP 1 Employees.LastName, COUNT(Employees.LastName) as OrderCount FROM Orders, Employees WHERE Employees.EmployeeID = Orders.EmployeeID GROUP BY Employees.LastName ORDER BY COUNT(Employees.LastName) DESC;

## c. Boston Crab Meat (160)
##    SELECT TOP 1 Products.ProductID, Products.ProductName, SUM(Quantity) AS TotalQuantity FROM Orders, OrderDetails AS OD, Customers, Products WHERE Customers.Country = "Germany" AND OD.OrderID = Orders.OrderID AND OD.ProductID = Products.ProductID AND Customers.CustomerID = Orders.CustomerID GROUP BY Products.ProductID, Products.ProductName ORDER BY SUM(Quantity) DESC;