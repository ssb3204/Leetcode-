select activity_date day,active_users
from(
    select activity_date, user_id ,count(*) over(partition by activity_date) active_users
    from activity
    where activity_date between '2019-06-28'and '2019-07-27'
    group by activity_date, user_id
) t
group by activity_date
