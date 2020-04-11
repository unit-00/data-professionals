## Life of a Data Professional
**Understanding the aspects of a professional that works with a database.**  
Min Tan


## Table of Contents
- [Motivation](https://www.github.com/unit-00/data-professional#motivation)
- [Dataset](https://www.github.com/unit-00/data-professional#dataset)
- [Question](https://www.github.com/unit-00/what-factors-have-a-relationship-to-wanting-to-change-jobs)


## Motivation
I am interested to learn about this field that works with data and databases. Since I will be working with other data professionals, it'll be good to be well informed.

## Dataset
The dataset came from [Brent Ozar's Salary Survey](https://www.brentozar.com/archive/2019/01/the-2019-data-professional-salary-survey-results/). 
- Responses from people around the world, answering questions regarding their job
    - year 2017 to 2019
- The data has 6893 rows by 29 columns
    - A mixture of strings and numbers
- I focused on the US, because 65% of the responses originated from there
- The survey evolved over time, some features do not have data in previous years

I have also collected data from [Capitol Impact's Government Gateway](https://www.ciclt.net/sn/clt/capitolimpact/gw_default.aspx).
- This database has state information on the zipcode of the responses.

**Caveat:**  
The data size is quite small, thus should take the tests and analysis with caution.

## Exploration
For this analysis, I focused on the difference of annual salary between three groups
- Not Looking for a new job
- Passively Looking for a new job
- Actively Looking for a new job

This particular write up will dive deeper into the features that I looked at that might influence the salary.

Features such as
- States
- Education
- Years With The Database
- Years With This Type of Job
- Amount of Other People On The Team
- Hours Worked Per Week
- Employment Sector
- Gender

The data was relatively clean. 
- It had 2 error values of `$92.27` and `100,  000`
- 3 outliers of salary in the millions  

To deal with these values, I have removed the outliers and transform the error value to integer. 

### Salary
---
Distribution of salary, not adjusted for outliers.

![Salary distribution, not adjusted](https://www.github.com/unit-00/data-professional/images/salary_not_adj_eda.png)

There's a heavy right tail skew, furthermore I don't think they are a good representation of the population.

Distribution of salary, adjusted.

![Salary distribution, adjusted](https://www.github.com/unit-00/data-professional/images/salary_adj_eda.png)

#### For the rest of the analysis, the data will be referring to salary without outliers.

### Top 5 States
---
![State Salary](https://www.github.com/unit-00/data-professional/images/salary_states_eda.png)

### Education
---
![Education Salary](https://www.github.com/unit-00/data-professional/images/salary_edu_eda.png)


### Years With Database
---
![Year Database Salary](https://www.github.com/unit-00/data-professional/images/salary_yrdb_eda.png)

### Years With This Type of Job
---
![Year Job Salary](https://www.github.com/unit-00/data-professional/images/salary_yrjb_eda.png)

### Hours of Working Per Week
---
![Hours of Working Salary](https://www.github.com/unit-00/data-professional/images/salary_hours_eda.png)

### Other People On Your Team
---
![Salary With People On Your Team](https://www.github.com/unit-00/data-professional/images/salary_opoyt_eda.png)

### Gender
---
![Salary Gender](https://www.github.com/unit-00/data-professional/images/salary_gender_eda.png)

### Top Database 
---
![Salary Database](https://www.github.com/unit-00/data-professional/images/salary_db_eda.png)


## Testing


## Conclusion


## Follow up
