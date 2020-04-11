## Life of a Data Professional
**Understanding the aspects of a professional that works with a database.**  
Min Tan


## Table of Contents
- [Motivation](https://github.com/unit-00/data-professionals#motivation)
- [Dataset](https://github.com/unit-00/data-professionals#dataset)
- [Exploration](https://github.com/unit-00/data-professionals#exploration)
- [Testing](https://github.com/unit-00/data-professionals#testing)
    - [Welch's Test](https://github.com/unit-00/data-professionals#welchs-test)
    - [Power Analysis](https://github.com/unit-00/data-professionals#power-analysis)
    - [MannWhitneyU Test](https://github.com/unit-00/data-professionals#mannwhitneyu-test)
    - [Bayesian Test](https://github.com/unit-00/data-professionals#bayesian-test)
- [Conclusion](https://github.com/unit-00/data-professionals#conclusion)
- [Follow Up](https://github.com/unit-00/data-professionals#follow-up)


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

![Salary distribution, not adjusted](https://github.com/unit-00/data-professionals/blob/master/images/salary_not_adj_eda.png)

There's a heavy right tail skew, furthermore I don't think they are a good representation of the population.

Distribution of salary, adjusted.

![Salary distribution, adjusted](https://github.com/unit-00/data-professionals/blob/master/images/salary_adj_eda.png)

#### For the rest of the analysis, the data will be referring to salary without outliers.

### Top 5 States
---
![State Salary](https://github.com/unit-00/data-professionals/blob/master/images/salary_states_eda.png)

### Education
---
![Education Salary](https://github.com/unit-00/data-professionals/blob/master/images/salary_edu_eda.png)


### Years With Database
---
![Year Database Salary](https://github.com/unit-00/data-professionals/blob/master/images/salary_yrdb_eda.png)

### Years With This Type of Job
---
![Year Job Salary](https://github.com/unit-00/data-professionals/blob/master/images/salary_yrjb_eda.png)

### Hours of Working Per Week
---
![Hours of Working Salary](https://github.com/unit-00/data-professionals/blob/master/images/salary_hours_eda.png)

### Other People On Your Team
---
![Salary With People On Your Team](https://github.com/unit-00/data-professionals/blob/master/images/salary_opoyt_eda.png)

### Gender
---
![Salary Gender](https://github.com/unit-00/data-professionals/blob/master/images/salary_gender_eda.png)

### Top Database 
---
![Salary Database](https://github.com/unit-00/data-professionals/blob/master/images/salary_db_eda.png)

From these charts, 
- the `Actively Looking` group seems to have on average lower salary count than those who are `Not Looking` and `Passively Looking`. 
- But the difference between `Not Looking` and `Passively Looking` is much subtler.  

In the next section I will test it more rigorously. 

## Testing
Difference in means

|Not Looking, Passively Looking|Passively Looking, Actively Looking|Not Looking, Actively Looking|
|---|---|---|
|3493.82|2364.20|5858.02|

We see these differences in means. From a business point of view if there does prove to be a significance, it can be worthwile to try to retain employees instead of paying to train new ones. 



### Welch's Test
---
Under the assumption that normality would converge, Welch's correction was done here because of the difference in variance. 

![nl pl Welch](https://github.com/unit-00/data-professionals/blob/master/images/null_nl_pl.png)

![pl al Welch](https://github.com/unit-00/data-professionals/blob/master/images/null_pl_al.png)

![nl al Welch](https://github.com/unit-00/data-professionals/blob/master/images/null_nl_al.png)

We see that there is a significance in difference in means between `Not Looking` and `Looking` in general. While we fail to reject the null between `Passively Looking` and `Actively Looking`.

### Power Analysis
---
![nl pl power](https://github.com/unit-00/data-professionals/blob/master/images/power_nl_pl.png)

![pl al power](https://github.com/unit-00/data-professionals/blob/master/images/power_pl_al.png)

![nl al power](https://github.com/unit-00/data-professionals/blob/master/images/power_nl_al.png)

- To follow up with power analysis, we see that we can detect a change of 99% between `Not Looking` and `Passively Looking`. While there's a 87% to detect a change between `Not Looking` and `Actively Looking`. We would be confident in our analysis between these two comparisons.
- As for `Passively Looking` and `Actively Looking`, we see that there is only a 23% chance to detect a change.

### MannWhitneyU Test
---
A non-parametric test was done as well, to see if there is disagreement with Welch's. 

The p value for the tests were 

Not Looking, Passively Looking
- 3.91e-5

Passively Looking, Actively Looking
- 0.0685

Not Looking, Actively Looking
- 0.0003


It does seem to agree with Welch's, though the p value for `Passively Looking` and `Actively Looking` was much lower in comparison to Welch's. I believe this is because Welch's take variance into consideration while MannWhitneyU does not. Depending on the reason for the analysis, it would impact the conservativeness of the test.

### Bayesian Test
---
To follow up with Frequentist approach, I also did Bayesian Testing.
Since this likelihood function follows a normal distribution, I used the conjugate prior of Inverse Gamma to generate the variance for the distribution of salary. 

Based on 10,000 simulated means I have found that

- 100% of the samples of `Not Looking` is greater than `Passively Looking`
- 89.47% of the samples of `Passively Looking` is greater than `Actively Looking`
- 99.98% of the samples of `Not Looking` is greater than `Actively Looking`

It's interesting that under Bayesian approach, the sample mean of `Passively Looking` is greater than `Actively Looking`. Which holds disagreement with the Frequentist approach.
In regards to other two tests, it does seem to be that `Not Looking` has a greater sample mean than `Passively Looking` and `Actively Looking`.

## Conclusion
There seems to be a difference in means between `Not Looking` and `Looking` in general. In regards to a hypothetical situation trying to lower turnover rates, it would be fair to investigate farther into whether investment into employees for long term is worthwhile.

## Follow up
Couple next step would be to 
- collect more data
- automate a pipeline to repeat this analysis
