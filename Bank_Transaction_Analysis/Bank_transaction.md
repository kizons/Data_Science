```sql
select * from ds_salaries;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/salaries.csv)

select distinct employment_type, job_title from ds_salaries
order by job_title;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/employment_type-job_title.csv)

select * from ds_salaries where job_title in ('Data Scientist');
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/job_title-data_scientist.csv)

select * from ds_salaries where job_title not in ('Data Scientist');
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/job_title-not_data_scientist)

select * from ds_salaries where work_year < 2021;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/work_year_before_2021.csv)

select avg(salary_in_usd) from ds_salaries where job_title='Data Scientist';
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/avg_salary-data_scientist.csv)

select * from ds_salaries where experience_level = 'SE';
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/experience_level-SE.csv)

select * from ds_salaries where (1.25 * salary) > 72000;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/1.25_salary_above_72000.csv)

select * from ds_salaries where (1.25 * salary) > 72000 and salary_currency = 'USD';
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/1.25_salary_above_72000USD.csv)

select k.experience_level, k.work_year, k.salary from ds_salaries k where 'work_year' < 2021;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

select * from ds_salaries where work_year = 2022;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

select * from ds_salaries where salary between 100000 and 200000;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- 1. order by popularity
select * 
from ds_salaries
order by salary_in_usd desc;
[output](https://github.com/kizons/Data_Science/blob/main/edit/main/Bank_Transaction_Analysis/Output)

-- 2. Add popularity column
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity
from ds_salaries;
[output](https://github.com/kizons/Data_Science/blob/main/edit/main/Bank_Transaction_Analysis/Output)

-- 3. Try different functions
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity,
        rank() over(order by salary_in_usd desc) as popularity_r,
        dense_rank() over(order by salary_in_usd desc) as popularity_dr
from ds_salaries;
[output](https://github.com/kizons/Data_Science/blob/main/edit/main/Bank_Transaction_Analysis/Output)

-- Try diffent windows
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries;
[output](https://github.com/kizons/Data_Science/blob/main/edit/main/Bank_Transaction_Analysis/Output)

-- 5. what are the top 3 most popular job_titles for each experience_level ?
select * from

(select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries) as pop

where popularity <=3;
[output](https://github.com/kizons/Data_Science/blob/main/edit/main/Bank_Transaction_Analysis/Output)

-- 6. Group by
select job_title, avg(salary_in_usd)
from ds_salaries
group by job_title;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- 7. window function
select employment_type, 
	job_title, 
    avg(salary_in_usd) 
    over(partition by job_title) as avg_salary
from
	ds_salaries;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)
    
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
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)
    
-- using group by
select
	job_title,
    avg(salary_in_usd) avr_salary,
    min(salary_in_usd) min_salary,
    max(salary_in_usd) min_salary
from
	ds_salaries
group by job_title;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

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
 [output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)   
    
-- How many job_title have a maximum salary_in_usd below $20000 ?
select count(*)
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 20000;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- What is the max salary_in_usd for each job_title ?
select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- How many max salary_in_usd are less than $20000 ?

-- subquery
select *
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 20000;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- cte
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select *
from ms
where max_salary < 20000;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- cte: multiple references
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select count(*)
from ms
where max_salary < (select avg(max_salary) from mp);
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

-- cte multiple tables
with ms as (select job_title, max(salary_in_usd) as max_salary
		from ds_salaries
		group by job_title),
    jt as (select *
		from ds_salaries
        where job_title like '%Data Scientist%')

select *
from jt left join ms on jt.job_title = ms.job_title;
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)

select *
from ds_salaries
where job_title like '%Data Scientist%';
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/Output)


-- recursive CTEs
