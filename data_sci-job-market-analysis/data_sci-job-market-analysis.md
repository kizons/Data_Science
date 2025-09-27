### SQL Query  
### select all columns from ds_salaries
```sql  
select * from ds_salaries;
``` 
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/salaries.csv)
### retrieve unique records of employment_type and job
```sql
select distinct employment_type, job_title from ds_salaries
order by job_title;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/employment_type-job_title.csv)
### retrieve all columns from ds_salaries where job title is Data Scientist
```sql
select * from ds_salaries where job_title in ('Data Scientist');
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/job_title-data_scientist.csv)
### retrieve all columns from ds_salaries where job title is not Data Scientist
```sql
select * from ds_salaries where job_title not in ('Data Scientist');
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/job_title-not_data_scientist.csv)
### retrieve all columns from ds_salaries where work year is before 2021
```sql
select * from ds_salaries where work_year < 2021;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/work_year_before_2021.csv)
### compute Data Scientist's average salary in usd from ds_salaries 
```sql
select avg(salary_in_usd) from ds_salaries where job_title='Data Scientist';
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/avg_salary-data_scientist.csv)
### retrieve all columns from ds_salaries where experience level is SE
```sql
select * from ds_salaries where experience_level = 'SE';
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/experience_level-SE.csv)
### retrieve all columns from ds_salaries where 125% of salary is less than 72000
```sql
select * from ds_salaries where (1.25 * salary) > 72000;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/1.25_salary_above_72000.csv)
### retrieve all columns from ds_salaries where 125% of salary is less than 72000USD
```sql
select * from ds_salaries where (1.25 * salary) > 72000 and salary_currency = 'USD';
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/1.25_salary_above_72000USD.csv)
### retrieve experience_level, work_year and salary from ds_salaries for work_year before 2021
```sql
select k.experience_level, k.work_year, k.salary from ds_salaries k where 'work_year' < 2021;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/experience-work-salary-before-2021.csv)
### retrieve all columns from ds_salaries where work_year is 2022
```sql
select * from ds_salaries where work_year = 2022;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/work_year_2022.csv)
### retrieve all columns from ds_salaries where salary is between 100000 and 200000
```sql
select * from ds_salaries where salary between 100000 and 200000;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/salary_between_10k-20k.csv)

### order by popularity
```sql
select * 
from ds_salaries
order by salary_in_usd desc;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/salary_in_usd-popularity.csv)

### Add popularity column
```sql
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity
from ds_salaries;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/add_popularity_column.csv)

### Try different functions
```sql
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(order by salary_in_usd desc) as popularity,
        rank() over(order by salary_in_usd desc) as popularity_r,
        dense_rank() over(order by salary_in_usd desc) as popularity_dr
from ds_salaries;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/multiple_functions.csv)

 ### Try diffent windows
```sql
select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/partition_by_JT.csv)

### what are the top 3 most popular job_titles for each experience_level ?
```sql
select * from

(select experience_level, employment_type, job_title, salary_in_usd,
		row_number() over(partition by job_title order by salary_in_usd desc) as popularity
from ds_salaries) as pop

where popularity <=3;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/top_3_most_popular_JT.csv)

### Group by
```sql
select job_title, avg(salary_in_usd)
from ds_salaries
group by job_title;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/group_by_JT.csv)

### window function
```sql
select employment_type, 
	job_title, 
    avg(salary_in_usd) 
    over(partition by job_title) as avg_salary
from
	ds_salaries;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/window_function_1.csv)
    
### avg, min, max
```
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
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/avg_min_max.csv)
    
### using group by
```sql
select
	job_title,
    avg(salary_in_usd) avg_salary,
    min(salary_in_usd) min_salary,
    max(salary_in_usd) max_salary
from
	ds_salaries
group by job_title;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/avg_min_max-salary.csv)

### Rank
```sql
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
```
 [output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/rank)   
    
### How many job_title have a maximum salary_in_usd below $50000 ?
```sql
select count(*)
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 50000;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/max_salary-less-than_50k.csv)

### What is the max salary_in_usd for each job_title ?
```sql
select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/max_salary-JT.csv)

### How many max salary_in_usd are less than $50000 ?

-- subquery
```sql
select *
from

(select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title) as ms

where max_salary < 50000;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/salary_less_than_50k.csv)

### CTE
```sql
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select *
from ms
where max_salary < 50000;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/CTE_max_salary_less_than_50k.csv)

### CTE: multiple references
```sql
with ms as (select job_title, max(salary_in_usd) as max_salary
from ds_salaries
group by job_title)

select count(*)
from ms
where max_salary < (select avg(max_salary) from ms);
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/CTE-multiple_ref.csv)

### CTE: multiple tables
```sql
with ms as (select job_title, max(salary_in_usd) as max_salary
		from ds_salaries
		group by job_title),
    jt as (select *
		from ds_salaries
        where job_title like '%Data Scientist%')

select *
from jt left join ms on jt.job_title = ms.job_title;
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/CTE-multiple_tables.csv)

```sql
select *
from ds_salaries
where job_title like '%Data Scientist%';
```
[output](https://github.com/kizons/Data_Science/blob/main/data_sci-job-market-analysis/output/JT_like_Data_Scientist.csv)

### Recursive CTEs: Compute cumulative salary for "Data Scientist" year by year:
```sql
WITH RECURSIVE salary_trend AS (
    SELECT 
        work_year,
        salary_in_usd,
        ROW_NUMBER() OVER (ORDER BY work_year) AS rn,
        salary_in_usd AS cumulative_salary
    FROM ds_salaries
    WHERE job_title = 'Data Scientist'
    
    UNION ALL

    SELECT 
        d.work_year,
        d.salary_in_usd,
        d.rn,
        st.cumulative_salary + d.salary_in_usd
    FROM salary_trend st
    JOIN (
        SELECT 
            work_year,
            salary_in_usd,
            ROW_NUMBER() OVER (ORDER BY work_year) AS rn
        FROM ds_salaries
        WHERE job_title = 'Data Scientist'
    ) d ON d.rn = st.rn + 1
)
SELECT * FROM salary_trend;
```
[output](https://github.com/kizons/Data_Science/blob/main/Bank_Transaction_Analysis/output/CTE-recursive.csv)
