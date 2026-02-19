# Write your MySQL query statement below
select dn Department, t.name Employee, salary Salary
from (
select e.name,d.name dn,salary,dense_rank() over(partition by d.id order by salary desc) rk
from employee e left join department d on e.departmentId=d.id
) t
where rk<=3
