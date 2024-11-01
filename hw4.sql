-- Q1
SELECT COUNT(Order_id) AS Total_Orders
FROM SALES
WHERE Date = '2023-03-18';

-- Q2
SELECT COUNT(SALES.Order_id) AS Total_Orders
FROM SALES
JOIN CUSTOMERS ON SALES.Customer_id = CUSTOMERS.customer_id
WHERE SALES.Date = '2023-03-18'
  AND CUSTOMERS.first_name = 'John'
  AND CUSTOMERS.last_name = 'Doe';

-- Q3
SELECT COUNT(DISTINCT Customer_id) AS Total_Customers,
       AVG(Revenue) AS Avg_Spent_Per_Customer
FROM SALES
WHERE Date BETWEEN '2023-01-01' AND '2023-01-31';

-- Q4
SELECT ITEMS.department, SUM(SALES.Revenue) AS Total_Revenue
FROM SALES
JOIN ITEMS ON SALES.Item_id = ITEMS.Item_id
WHERE SALES.Date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY ITEMS.department
HAVING SUM(SALES.Revenue) < 600;

--Q5
SELECT MAX(Revenue) AS Max_Revenue, MIN(Revenue) AS Min_Revenue
FROM SALES;

--Q6
WITH Max_Order AS
    (SELECT Order_id
    FROM SALES
    ORDER BY Revenue DESC
    LIMIT 1)

SELECT SALES.Order_id, ITEMS.Item_name, SALES.Quantity, SALES.Revenue
FROM SALES
JOIN ITEMS ON SALES.Item_id = ITEMS.Item_id
WHERE SALES.Order_id = (SELECT Order_id FROM Max_Order);
