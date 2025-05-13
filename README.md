# Hillsborough County Parcel Sales Prediction

## Introduction
When a natural disaster, such as hurricanes, impacts a community, government entities rely on metrics from property appraisers to quantify and categorize the damages. For example: Market Value is the value that the land and improvements would sell for in a competitive market at a fair price; Building Value is the value of all structures on a property; and Tax Value is the assessed value minus any taxable exemptions. One issue with these metrics is that they are not standardized in how they are calculated or used, and the Market Value may not accurately represent price a buyer would pay to purchase the property. As a result, estimating total impacts can be challenging, and reimbursement programs may undervalue properties leaving substantial financial burdens on the residents while filing a claim. The purpose of this analysis is to use analytics to predict the sale values of properties within Hillsborough County, Florida.

## Methodology
Publically available data containing metrics about the parcels, buildings, and sale values, will be loaded into an environment and analyzed during the exploratory data analysis (EDA) phase to uncover hidden trends, multicollinearity, and other statistically significant factors. A cleaned version of the data will be split into training and testing subsets and will undergo multiple rounds of machine learning and deep learning training to identify the optimal hyperparameters based on the lowest cross-validation error. Once the optimal model and hyperparameters are determined, the model will be fitted to the testing data subset to measure its performance. 

See the provided [workflow](docs/flowchart/parcel_sales.png) diagram for a visual representation.

## Expected Outcome
This analysis will assist government agencies in accurately quantifying the impacts of a natural disaster. The results will be provided in the form of a written report, which will include a detailed description of the methodology and results, as well as an interactive dashboard.