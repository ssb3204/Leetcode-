# Write your MySQL query statement below
select t.student_id, t.student_name , t.subject_name, count(e.subject_name) attended_exams
from (
    select *
    from students s cross join subjects j
) t left join examinations e on e.student_id =t.student_id and e.subject_name = t.subject_name
group by t.student_id, t.student_name , t.subject_name
order by s.student_id, j.subject_name