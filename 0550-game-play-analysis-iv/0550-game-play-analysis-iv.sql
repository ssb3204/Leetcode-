# Write your MySQL query statement below
select round(count(case when i.md=t.fd then 1 else null end)/ count(distinct i.player_id),2) fraction
from (
    select player_id,event_date, date_sub(event_date, interval 1 day) md
    from activity
) i join
(
    select player_id,device_id, MIN(event_date) fd
    from activity
    group by player_id
) t
on i.player_id =t.player_id



