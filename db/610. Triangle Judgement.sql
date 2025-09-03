-- https://leetcode.com/problems/triangle-judgement/description/

Create table If Not Exists Triangle (x int, y int, z int)
Truncate table Triangle
insert into Triangle (x, y, z) values ('13', '15', '30')
insert into Triangle (x, y, z) values ('10', '20', '15')

select * , case 
when (t.x + t.y > t.z) & (t.x + t.z > t.y) & (t.y + t.z > t.x) then "Yes"
else "No" end as triangle 
from Triangle t

