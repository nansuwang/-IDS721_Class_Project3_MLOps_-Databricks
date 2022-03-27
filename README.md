# IDS721 Class Project3 MLOps with Databricks

[![CI with Github Actions](https://github.com/nansuwang/IDS721_Class_Project3_MLOps_-Databricks/actions/workflows/main.yml/badge.svg)](https://github.com/nansuwang/IDS721_Class_Project3_MLOps_-Databricks/actions/workflows/main.yml)

## Introduction
It is a demo project for assignment in IDS721 course.
A AutoML model using Databricks Azure

It uses temp_median_c,	temp_min_c, temp_max_c, precip_mm, beer_cons_liters, to predict whether it is a weekend or not.

The dataset is from Kaggle. https://www.kaggle.com/datasets/dongeorge/beer-consumption-sao-paulo

## Workflow
1. The working environment is in Databricks. The repo was integrated with Github.
2. The data was wrangled using "preprocessing.py"
3. The cleaned data was performed Auto-ML process using Databricks Azure
4. The best model was registered
5. The service was provided using Databricks (For saving credit, batch inference was used in the demo. But real-time service could be easily deployed)
6. CI workflow was built in this assignment

## Advantages
1. It could cover almost ALL processes in traditional machine learning workflow, including EDA, preprocessing, train/validation/test split, hyper-parameters tuning, and model evaluation. Almost ALL are automated.
2. The model building process could be reproduced on local machine. I show this process using "model_reproduce.ipynb".
3. The real-time and batch services in Databricks are convenient. The model could also be downloaded for other services like AppRunner. The codes for downloading the model are provided in the "List Models.py". The model is also provided in the "classification_model.pkl".
