# Write your MySQL query statement below
select 'Low Salary' category, count(case when income<20000 then 1 end) accounts_count
from accounts
union all
select 'Average Salary' category, count(case when income>=20000 and income<=50000 then 1 end) accounts_count
from accounts
union all
select 'High Salary' category, count(case when income>50000 then 1 end) accounts_count
from accounts
order by category