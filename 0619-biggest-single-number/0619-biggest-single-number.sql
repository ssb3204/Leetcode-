# Write your MySQL query statement below
select max(num) num
from(
    select num,count(*) over(partition by num) cnt
    from mynumbers 
) t
where cnt=1
