# Write your MySQL query statement below
select distinct class
from(
    select class, count(student) over(partition by class) cnt
    from courses
) t
where cnt >=5