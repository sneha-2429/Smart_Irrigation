# Smart Irrigation System 

## 🔍 Objective
Build a model that predicts whether irrigation is needed in 3 farm parcels based on 20 sensor readings.

## 📊 Dataset
- 2000 records
- 20 sensor columns
- 3 target columns (parcel_0, parcel_1, parcel_2)

## 🧠 Model
- MultiOutputClassifier with Random Forest
- Accuracy above 80% for most labels

## 🛠 Tools Used
- Python
- Pandas
- Scikit-learn

## 📌 Sample Prediction
Input: [2, 1, 3, 4, ..., 4, 1]  
Output: [1, 0, 0] – Irrigation needed in Parcel 0

## 🗂 Files
- irrigation_machine.csv – dataset
- smart_irrigation.ipynb – code# Smart_Irrigation
- min_max_scaler.joblib
- multi_output_irrigation_model.joblib
