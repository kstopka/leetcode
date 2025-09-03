-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

Create table If Not Exists orders (order_number int, customer_number int)
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')


select customer_number
from Orders 
group by customer_number
order by count(customer_number) desc limit 1