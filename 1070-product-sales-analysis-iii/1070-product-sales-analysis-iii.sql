# Write your MySQL query statement below
select s.product_id, fy first_year, quantity, price
from sales s
join (select product_id, min(year) fy
      from sales
      group by product_id
      ) t on s.product_id =t.product_id
and year =fy
    