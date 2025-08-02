# 📊 Data Science Job Market Dashboard

This project provides an interactive Power BI dashboard analyzing data science job trends using the [ds_salaries.csv](https://github.com/kizons/Data_Science/blob/main/ds-job-market-powerbi/ds_salaries.csv) dataset. It covers key aspects such as salaries, job titles, remote work trends, experience levels, and geographic distributions.

---

## 🔍 Dataset Summary

- **Source**: [Kaggle - Data Science Job Salaries](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)
- **Rows**: 607
- **Fields**: work year, experience level, employment type, Job title, salary, salary currency, salary in USD, employee residence, remote ratio, company location, company size

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `ds_salaries.csv` | Raw dataset used for the dashboard |
| `clean_ds_salaries.pbix` | Power BI report file (fully interactive) |
| `README.md` | Project documentation (this file) |

---

## 📄 Report Pages Overview

### ✅ Page 1: **Overview**
- Total Jobs, Average Salary, Max Salary (KPI cards)
- Top 5 Job Titles (bar chart)
- Filters: Year, Experience Level, Company Size

### 🌐 Page 2: **Remote Work Impact**
- Pie chart of remote role distribution
- Avg salary by remote type
- Filters: Year, Job Title, Company Size

### 📍 Page 3: **Geographic Salary Insights**
- Map of salary by country
- Top 10 countries by average salary
- Filters: Year, Experience Level, Remote Share

### 👔 Page 4: **Job Title Explorer**
- Select a job title to view:
  - Salary range (min, avg, max)
  - Common locations and company sizes
  - Remote work type breakdown

### 📈 Page 5: **Salary Trends**
- Salary trend over years (line chart)
- Job count trend over time
- Breakdowns by:
  - Job title
  - Experience level
  - Country or company size
- Filters: Experience Level, Company Size, Remote Share, Year

---

## 🚀 How to Use

1. Download or clone this repository:
   ```bash
   git clone https://github.com/kizons/Data_Science.git
   cd Data_Science/ds-job-market-powerbi
2. Open the clean_ds_salaries.pbix file in Power BI Desktop.
3. Explore each page interactively and apply filters as needed.

📌 Skills Demonstrated
* Power BI: Visuals, DAX measures, calculated columns, slicers.
* Data modeling and transformation.
* Data storytelling and dashboard navigation.
* Salary analysis, role-based insights, geographic patterns.

📬 Contact
If you have questions or suggestions, feel free to reach out:

GitHub: @kizons

Email: okaforkizito@gmail.com

🏁 License
This project is open source and available under the MIT License.


