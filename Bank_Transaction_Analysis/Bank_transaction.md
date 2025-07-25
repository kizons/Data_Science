```sql
select * from ds_salaries;

select salary_in_usd from ds_salaries;

select distinct employment_type, job_title from ds_salaries
order by job_title;

select * from ds_salaries where job_title in ('Data Scientist');

select * from ds_salaries where job_title not in ('Data Scientist');

select * from ds_salaries where work_year < 2021;

select avg(salary_in_usd) from ds_salaries where job_title='Data Scientist';

select * from ds_salaries where experience_level = 'SE';

select * from ds_salaries where (1.25 * salary) > 72000;

select * from ds_salaries where (1.25 * salary) > 72000 and salary_currency = 'USD';

select k.experience_level, k.work_year, k.salary from ds_salaries k where 'work_year' < 2021;

select * from ds_salaries where work_year = 2022;

select * from ds_salaries where salary between 100000 and 200000;

-- 1. order by popularity
select * 
from ds_salaries
order by salary_in_usd desc;

-- 2. Add popularity column
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity
from ds_salaries;

-- 3. Try different functions
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity,
        rank() over(order by salary_in_usd desc) as popularity_r,
        dense_rank() over(order by salary_in_usd desc) as popularity_dr
from ds_salaries;

-- Try diffent windows
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries;

-- 5. what are the top 3 most popular job_titles for each experience_level ?
select * from

(select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries) as pop

where popularity <=3;

-- 6. Group by
select job_title, avg(salary_in_usd)
from ds_salaries
group by job_title;

-- 7. window function
select employment_type, 
	job_title, 
    avg(salary_in_usd) 
    over(partition by job_title) as avg_salary
from
	ds_salaries;
    
-- avg, min, max
select employment_type, 
	job_title, 
    avg(salary_in_usd) 
    over(partition by job_title) as avg_salary,
    
    min(salary_in_usd) 
    over(partition by job_title) as min_salary,
    
    max(salary_in_usd) 
    over(partition by job_title) as max_salary
    
from
	ds_salaries;
    
-- using group by
select
	job_title,
    avg(salary_in_usd) avr_salary,
    min(salary_in_usd) min_salary,
    max(salary_in_usd) min_salary
from
	ds_salaries
group by job_title;

-- Rank
select employment_type, 
	job_title, 
    salary_in_usd,
    avg(salary_in_usd) 
    over(partition by job_title) as avg_salary,
    
    min(salary_in_usd) 
    over(partition by job_title) as min_salary,
    
    max(salary_in_usd) 
    over(partition by job_title) as max_salary,
    
    rank() over(order by salary_in_usd desc) as overall_rank,
    
    rank() over(partition by job_title order by salary_in_usd desc) as dept_rank
    
from
	ds_salaries;
    
    
-- How many job_title have a maximum salary_in_usd below $20000 ?
select count(*)
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 20000;

-- What is the max salary_in_usd for each job_title ?
select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title;

-- How many max salary_in_usd are less than $20000 ?

-- subquery
select *
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 20000;

-- cte
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select *
from ms
where max_salary < 20000;

-- cte: multiple references
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select count(*)
from ms
where max_salary < (select avg(max_salary) from mp);

-- cte multiple tables
with ms as (select job_title, max(salary_in_usd) as max_salary
		from ds_salaries
		group by job_title),
    jt as (select *
		from ds_salaries
        where job_title like '%Data Scientist%')

select *
from jt left join ms on jt.job_title = ms.job_title;

select *
from ds_salaries
where job_title like '%Data Scientist%';



-- recursive CTEs
