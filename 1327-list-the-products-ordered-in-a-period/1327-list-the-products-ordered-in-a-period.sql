# Write your MySQL query statement below
select t.product_name,sum(t.unit) unit
from(
select product_name ,unit, substring(order_date,1,7) date, sum(unit) over (partition by p.product_id ,substring(order_date,1,7)) u_s
from products p left join orders o on p.product_id=o.product_id
) t
where u_s>=100 and date='2020-02'
group by product_name