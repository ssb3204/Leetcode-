# Write your MySQL query statement below
select person_name 
from (
select *, sum(weight) over(order by turn rows between unbounded preceding and current row) w_s
from queue
) t 
where w_s <=1000
order by turn desc limit 1