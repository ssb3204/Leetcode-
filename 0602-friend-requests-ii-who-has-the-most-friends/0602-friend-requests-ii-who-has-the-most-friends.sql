select requester_id id, count(*) num
from(
select requester_id
from requestaccepted
union all
select accepter_id
from requestaccepted
) t
group by requester_id
order by num desc limit 1