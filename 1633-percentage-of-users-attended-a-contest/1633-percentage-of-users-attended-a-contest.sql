# Write your MySQL query statement below
-- select r.contest_id, count(*) cnt
-- from register r left join users u on r.user_id=u.user_id
-- group by contest_id
-- order by cnt desc, contest_id

select contest_id , round(count(*)*100.0/(select count(*) from users),2) percentage
from register
group by contest_id
order by percentage desc , contest_id