# Write your MySQL query statement below
select employee_id ,department_id
from (
    select *, count(department_id) over(partition by employee_id) cnt
    from employee
) t
where (cnt=1) or (primary_flag ="Y") 