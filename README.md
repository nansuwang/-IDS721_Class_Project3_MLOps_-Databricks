# IDS721 Class Project3 MLOps with Databricks

## Introduction
It is a demo project for assignment in IDS721 course.
A AutoML model using Databricks Azure

It uses temp_median_c,	temp_min_c, temp_max_c, precip_mm, beer_cons_liters, to predict whether it is a weekend or not.

The dataset is from Kaggle. https://www.kaggle.com/datasets/dongeorge/beer-consumption-sao-paulo

## Workflow
1. The working environment is in Databricks. The repo was integrated with Github.
2. The data is wrangling using 'preprocessing.py'
3. The cleaned data is performed Auto-ML process using Databricks Azure
4. The best model is registered
5. The service is provided using Databricks (For saving credit, batch inference was used in the demo. But real-time service could be easily deployed)
6. CI workflow is built in this assignment
