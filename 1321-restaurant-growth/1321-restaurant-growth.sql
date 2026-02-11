# Write your MySQL query statement below
with daily as(
    select visited_on, sum(amount) amount
    from customer
    group by visited_on
)
select d1.visited_on , sum(d2.amount) amount , round((sum(d2.amount))/7,2) average_amount
from daily d1 join daily d2 on d2.visited_on between date_sub(d1.visited_on,interval 6 day) and d1.visited_on
group by d1.visited_on
having count(*)=7
order by d1.visited_on