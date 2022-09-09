# Smartphone-Price-Prediction-Model
## Introduction

The dataset includes a range of features for more than 1000 smartphones. XGBoost and CatBoost regression models are implemented and compared. The better one is chosen and used for price prediction. The users can input their own data and get an estimated price for specified features. 


![image](https://user-images.githubusercontent.com/105684729/187708339-99b12e54-fddc-4181-830b-6a4b94e35689.png)

## Problem 

This is a personal project. I had trouble deciding on the model and the brand of the smartphone I would buy. So, I decided to compare each brand in the market in regards to price and hardware capacity. Thanks to  ML algorithms I could have an idea about the budget size for a phone with the features I wanted.

## Process

I scraped data about the price, RAM, storage, CPU, screen size, color, camera resolution, brand and model of each smartphone on a retail e-commerce website. After cleaning and formatting the data, I built several ML regression models to that makes price predictions from desired specifications. I compared the models and used the best one.

![image](https://user-images.githubusercontent.com/105684729/189375183-b675cc74-2602-4c30-b675-e1c729fea4cb.png)

## Model Deployment

After the model is tested, it is saved in a .sav file and the save file is used in the deployment process. The deployment is done on the streamlit API. The detailed code is present in the repository. Here is the final product.  

[Application](https://yusufgulcan-smartphone-price-prediction-model-deployment-kr4n3c.streamlitapp.com/)

## Bonus:

### Power BI visualization
I also prepared an interactive dashboard where details of the market can be seen.

[BI Dashboard](https://app.powerbi.com/groups/me/reports/8210a11f-7cff-4325-b1cc-bee902817b99/ReportSection)

### Medium Article 
If you are interested, you can see my medium post about this project. I explained the steps in detail and my reasoning.

[Medium Article](https://medium.com/p/ad51bf8c45d6)


### Libraries
- XGBOOST 
- CATBOOST
- Pandas
- Numpy
- Streamlit
- Matplotlib
- Scikit-Learn
- Pickle
- Regular Expressions

## Further Improvements

In this project, the data came from only one website. It would represent the market more if there were more data coming from other resources. If this is achieved, the model predictions approximates to the prices of all market. Also increase in the data size would help the model avoid overfitting. 





