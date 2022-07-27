# Zillow Regression Project

## Project Goals

The goal is to find the key drivers of property value for single-family properties on Zillow, then make recommendations to help the data science team have a better prediction on the house value.

## Project Description

In this report, we will analyze the Zillow 2017 single-family property transaction data, use the regression machine learning method to develop a model to prediction of the house value base on the selected features. Then give out the recommendations about how to improve the predictions for the future.

## Initial Questions

1. Does bedroom count affect the house value?
2. Does bathroom count affect the house value?
3. Is there a relationship between fips and house value?
4. Is there a relationship between building year and house value?
5. Is there a linear relationship between square feet and house value?

## Data Dictionary

Variables are used in this analysis:

* bedroom : Number of bedrooms in home.
* bathroom : Number of bathrooms in home including fractional bathrooms.
* fips : Federal Information Processing Standard code.
* yearbuilt: The Year the principal residence was built.
* square_ft : Calculated total finished living area of the home.
* house_value : The total tax assessed value of the parcel.
* taxamount : The total property tax assessed for that assessment year.

## Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the Zillow table. Store that env file locally in the repository.
2. Clone my repo (including the acquire_zillow.py and prepare_zillow.py) (confirm .gitignore is hiding your env.py file)
3. Libraries used are pandas, matplotlib, seaborn, numpy, sklearn, scipy.stats, math.
4. You should be able to run zillow_prediction_report.

## Plan

## Wrangle

### Modules (acquire.py + prepare.py)

1. Write SQL query to acquire the data from mysql server, then test acquire function
2. Add to acquire.py module
3. Write code to clean data in notebook
4. Write code to split data in notebook
6. Merge functions in a single function & test
8. Add all 3 functions (or more) to prepare.py file
9. Import into notebook and test functions

### Acquire the Zillow data

1. select bedroom, bathroom, square_feet, fips, yearbuilt, house_value and tax amount from zillow.properties_2017 and rename the columns at the same time
2. left join zillow.predictions_2017 and select transaction date like '2017%%'
3. then choose prepertylandusetypeid = 261 which is single family properties code

### Missing Values (report.ipynb)

Missing value:
1. square_ft       82
2. yearbuilt      116
3. fips             0
4. house_value      1
5. tax              4

There are 203 missing values, the percentage of missing values is only 0.4%, so I will just drop them.

### Convert data type
convert bedroom, yearbuilt, square_ft and fips into int.

### Set up a cut-off line to analyze majority of data
bedroom <= 6, bathroom <= 6, house_value < 2,000,000

### Data Split (prepare.py (def function), report.ipynb (run function))

* train = 56%
* validate = 24%
* test = 20%

### Using your modules (report.ipynb)
once acquire.py and prepare.py are created and tested, import into final report notebook to be ready for use.

## Set the Data Context

In this report, there are 52,441 observations in 2017 zillow data and 5 features will be used for my analysis to predict the house value.

1. plot a displot for overall house value, x is house value, y is count
2. plot a countplot for bedroom, x is bedroom number, y is count
3. plot a countplot for bathroom, x is bathroom number, y is count
4. plot a histplot for yearbuilt, x is year, y is count
5. plot a cpuntplot for fips, x is fips number, y is count

## Explore

1. Does bedroom count affect the house value?
2. Does bathroom count affect the house value?
3. Is there a relationship between fips and house value?
4. Is there a relationship between building year and house value?
5. Is there a linear relationship between square feet and house value?

## Exploring through visualizations (report.ipynb)

1. Does bedroom count affect the house value?

* what is the house value mean for different bedroom count? plot a boxplot to show the difference between different room counts. X is bedroom count, y is house value.
* run a pearsonr statistic test to test the correlation

2. Does bathroom count affect the house value?

* what is the house value mean for different bathroom count? plot a boxplot to show the difference between different room counts. X is bathroom count, y is house value.
* run a pearsonr statistic test to test the correlation

3. Is there a relationship between fips and house value?

* what is the house value mean for different location? plot a boxplot to show the difference between different location. X is fips number, y is house value.

4. Is there a relationship between building year and house value?

* is there a linear relationship? run a jointplot chart with a indicate line, x is year built, y is house value.

5. Is there a linear relationship between square feet and house value?

* is there a linear relationship? run a jointplot chart with a indicate line, x is square feet, y is house value.
* run a pearsonr statistic test to test the correlation

Plot a correlation heat map to pick the top three features drive house value.

## Summary (report.ipynb)

Bedroom count, bathroom count, square feet, yearbuilt and fips all have some relationships with house value. Among those arributes, bedroom count, bathroom count and square feet have the strongest correlation with house value.

Therefore, the features I will use for modeling:
* bedroom count
* bathroom count
* square feet

# Modeling

## Select Evaluation Metric (Report.ipynb)

Because house value is a continuous variable, so I will use five different Regression machine learning models to fit the train. Those five models will use same features but different algorithms. Then evaluate on validate set to test overfit and pick the best model on the test set.

The metrics I will use are RMSE (Root Mean Squared Error) and R2 score. RMSE is the most common used metric for regression model also it has the same unit with our target value which is 'dollar'. And R2 is also a very often used function computes the coefficient of determination.

## Evaluate Baseline (Report.ipynb)

The baseline value I set for train and validate set is the mean of house value on the train set.

## Develop 5 Models (Report.ipynb)

1. Linear Regression
2. Lasso-Lars
3. TweedieRegressor
4. 2nd degree Polynomial
5. interaction only polynomial

## Evaluate on Train (Report.ipynb)

caculate RMSE and R2 scores for each model, three top models are:

1. 2nd degree polynomial 
2. interaction only polynomial
3. multiple Regression

## Evaluate on Validate (Report.ipynb)

caculate RMSE and R2 scores for each model, the best model is 2nd degree polynomial.

## Evaluate Top Model on Test (Report.ipynb)

test result:
* RMSE: 289424.55
* R2: 0.35

## Expectation:
According to the test result, I expect there will be a $289,425 price difference with a correlation of 0.35 for my future prediction if the data souce has no major change.

# Report (Final Notebook)

## Code commenting (Report.ipynb)

## Written Conclusion Summary (Report.ipynb)

By analyzing the key drivers of the majority of Zillow single house value of 2017, we built a 2nd degree polynomisl regression model with the top three attributes (bedroom, bathroom, square ft) to predict the house value. The RMSE for the test set is $289,425 and the r2 score is 0.35.

## conclusion recommendations (Report.ipynb)

This is a very general and basic overall report only uses the most basic features to show what I learned from the regression model with the data science pipeline.

This model result will not look good on low-value houses like some houses in Los Angeles, since the average unit prices are different by location. Therefore, using different models and feature combinations for different locations will give us a better prediction.

## conclusion next steps (Report.ipynb)

1. I would like to do individual exploration and build different models for different locations.
2. Bring more features to explore, and use different algorithms and metrics to improve the overall performance.

## no errors (Report.ipynb)

# Live Presentation

## Intro (live)

## audience & setting (live)

A group of collegues and managers.

## content (live)

## Verbal Conclusion (findings, next steps, recommendations) (live)

## time (live)
5 minutes.