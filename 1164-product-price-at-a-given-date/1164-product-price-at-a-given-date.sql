# Write your MySQL query statement below
select p1.product_id, coalesce((select pr.new_price
                               from products pr
                               where p1.product_id=pr.product_id and pr.change_date<='2019-08-16'
                               order by pr.change_date desc limit 1),10) as price
from
(
    select distinct product_id
    from products
)p1