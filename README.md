 Smart Irrigation System Using Machine Learning
📌 Overview
This project presents a Smart Irrigation System that automates the ON/OFF status of 20 individual sprinklers based on real-time sensor data. Using a trained machine learning model, the system predicts whether a sprinkler should be activated or not, optimizing water usage and reducing manual effort in farm management.

🎯 Objectives
Predict the status (ON/OFF) of 20 sprinklers using sensor inputs.
Build an interactive user interface for real-time predictions.
Enhance irrigation efficiency through data-driven automation.

🧰 Tools & Technologies
Python for backend logic and data processing.
NumPy, Pandas for numerical and data operations.
Scikit-learn to train and save the classification model.
Joblib to serialize and load the trained model.
Streamlit for the interactive web application.
Matplotlib for graphical summary (bar & line charts).

🔍 How It Works
Input: 20 sliders allow users to simulate or input sensor values (scaled 0 to 1).
Prediction: A machine learning model predicts ON/OFF status for each sprinkler.
Output: Sprinkler status is shown with intuitive emojis and color codes.
Visualization: Bar and line charts display a summary of active/inactive sprinklers.

🧪 Methodology
The sensor data is preprocessed and used to train a classification model capable of deciding sprinkler statuses. The trained model is integrated into a Streamlit app, which offers a simple interface for users to adjust sensor inputs and view live predictions. Visualizations are used to help interpret the sprinkler behavior across parcels.

🔚 Conclusion
This project demonstrates the use of machine learning in agriculture to automate irrigation, improve water management, and reduce manual operations. It is scalable for large farms and adaptable for IoT sensor integration.

🚀 Future Scope
Integrate with live IoT sensors and weather data APIs.
Expand to zone-based irrigation with predictive analytics
