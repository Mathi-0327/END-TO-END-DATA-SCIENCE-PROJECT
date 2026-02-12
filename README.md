# End-to-End Data Science Project - House Price Prediction

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MATHIYAZHAGAN M 

*INTERN ID*: CTIS4317

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

## 📌 Project Description
This project is an End-to-End Data Science application designed to predict house prices using the California Housing dataset. The main objective of this project is to demonstrate the complete machine learning workflow, starting from data collection and preprocessing to model training, evaluation, and deployment as a web API.

The dataset contains multiple housing-related features such as median income, house age, average number of rooms, average bedrooms, population, average occupancy, latitude, and longitude. These features are used as input variables to predict the target value, which represents the house price.

In this project, the dataset is loaded and analyzed to understand feature relationships and patterns. Basic exploratory data analysis (EDA) is performed, including correlation analysis and visualization, to identify important features influencing house prices. The data is then split into training and testing sets to build a machine learning model. A Linear Regression algorithm is used to train the model due to its simplicity and effectiveness for regression-based prediction problems.

After training, the model is evaluated using metrics such as Mean Squared Error (MSE) and R2 Score to measure prediction accuracy and performance. The trained model is then saved using Joblib, enabling reuse without retraining.

To make the model accessible for real-world usage, it is deployed using FastAPI. A REST API is created with endpoints that allow users to send feature values as input and receive predicted house prices as output. The API can be tested using Swagger UI provided by FastAPI at /docs.

Overall, this project successfully demonstrates an end-to-end machine learning pipeline and model deployment, making it a practical example of how data science solutions can be developed and integrated into real applications.

---

## 📊 Output Visualizations
<img width="1317" height="747" alt="Image" src="https://github.com/user-attachments/assets/b7668814-de19-4a2f-b61e-f02b39874a91" />
<img width="1315" height="442" alt="Image" src="https://github.com/user-attachments/assets/907c993a-7acb-4ef1-9707-8e9bdc1fffad" />


### Correlation Heatmap
![Correlation Heatmap](outputs/correlation_heatmap.png)

### Actual vs Predicted Plot
![Actual vs Predicted Plot](outputs/actual_vs_predicted.png)

---

## 🛠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib
- FastAPI
- Uvicorn

---



---

## 🧪 How to Test Output in Swagger UI

After running the FastAPI server, open this link in browser:


### Steps to Test Prediction:
1. Click **POST /predict**
2. Click **Try it out**
3. Paste the input JSON in the request body
4. Click **Execute**
5. You will get the predicted output in the response section

---
## output
<img width="1852" height="908" alt="Image" src="https://github.com/user-attachments/assets/998977ef-2f44-4472-b0ff-363029c1b1f6" />
<img width="1846" height="811" alt="Image" src="https://github.com/user-attachments/assets/d08d7529-9096-45df-b575-921cc0f87a89" />
<img width="1864" height="801" alt="Image" src="https://github.com/user-attachments/assets/8c51e7f9-fbc4-4f94-84ad-f94820b5447b" />
<img width="1801" height="935" alt="Image" src="https://github.com/user-attachments/assets/a9c3a2a7-abea-4916-a51e-026ccb0a4248" />










