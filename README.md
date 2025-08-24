# 🌱 SmartAgri - Crop Recommendation System
A machine learning-powered system to recommend the most suitable crop based on soil and environmental parameters such as Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.

## 🚀 Project Overview
This project uses Gradient Boosting Classifier trained on soil and weather data to predict the best crop recommendation. It includes:
- Data preprocessing with scaling of numeric features
- Model training and saving with pickle serialization
- Streamlit web app for interactive real-time predictions

## 📋 Prerequisites
- Python 3.13 
- Required Python libraries:
```bash
pip install pandas numpy scikit-learn streamlit
```

### 🧑‍💻 Step-by-Step Guide
1. Clone the repository
```bash
git clone https://github.com/sowmya13531/AgriPredict-Crop-Recommendation.git
cd your-AgriPredict-Crop-Recommendation
```

2. Prepare the dataset

Make sure you have a dataset (e.g., dataset.csv) containing the following columns:(Crop Recommendation.csv)
- N (Nitrogen)
- P (Phosphorus)
- K (Potassium)
- temperature
- humidity
- ph
- rainfall
- label (target crop)

3. Data Preprocessing and Feature Scaling
Select numeric columns to normalize:
numeric_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
Use MinMaxScaler to scale features between 0 and 1.

4. Train the Model
Split features and labels:
X = df[numeric_cols]
y = df['label']

Train the Gradient Boosting Classifier:
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()
model.fit(X_scaled, y)

5. Save the Model and Scaler
Save the trained model and scaler for later use in the app:
import pickle
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

6. Running the Streamlit App
The app loads the saved model and scaler.
Inputs from users are scaled and fed into the model for prediction.

To start the app, run:

*streamlit run app.py*

7. Using the App
Enter values for soil and environmental parameters.
*Click Recommend Crop*
See the recommended crop displayed instantly.

- ⚙️ Important Notes:
- The model was trained on scaled data; the app uses the same scaler to transform inputs before making predictions. This ensures accuracy and consistency.
- Keep the feature order consistent between training and inference.
- This project demonstrates an end-to-end machine learning workflow — from training to deployment.

- 📁 Project Structure
- ├── app.py            # Streamlit app for prediction UI
- ├── model.pkl         # Saved Gradient Boosting model
- ├── scaler.pkl        # Saved MinMaxScaler object
- ├── train_model.py    # Script to preprocess data, train, and save model + scaler
- ├── dataset.csv       # Dataset with features and crop labels
- ├── README.md         # This guide

💬 Contact & Contributions

If you find issues or want to contribute, please open an issue or submit a pull request. Feedback and collaboration are welcome!

Happy Farming! 🌾🚜
