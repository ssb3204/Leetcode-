# Write your MySQL query statement below
select round(count(case when order_date = customer_pref_delivery_date then 1 else null end)/count(*)*100 ,2)immediate_percentage
from(
    select * , row_number() over(partition by customer_id order by order_date) rd
    from delivery
) t
where rd=1

