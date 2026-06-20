# ❤️ CardioCare: AI-Powered Heart Disease Predictor & Analyzer

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=flat-square&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3">
</p>

An intelligent, full-stack clinical web application that predicts a patient's risk of heart disease using a highly-tuned **Random Forest Machine Learning Model** (98% accuracy). Beyond just a prediction, the app leverages the **Google Gemini AI API** to provide personalized, easy-to-understand lifestyle, diet, and exercise recommendations based on the patient's specific medical parameters.

---

## ✨ Features

- **High-Accuracy ML Model**: Trained using `scikit-learn` on clinical data to predict heart disease based on 13 critical medical indicators.
- **Generative AI Integration**: Feeds clinical results directly to Google's Gemini 3.5 Flash model to generate personalized health insights, dietary suggestions, and habit changes.
- **Professional Clinical UI/UX**: Built with a custom, responsive, flat-design CSS architecture utilizing an elegant "Slate & Trust Blue" color palette to reduce eye strain and look highly professional.
- **Dynamic Markdown Rendering**: Seamlessly parses AI-generated markdown into beautiful HTML for the end user.

---

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn (Random Forest), Pandas, NumPy
- **Generative AI**: Google Gemini API (`google-genai` SDK)

---

## 📁 Project Structure

```text
Heart-Disease-Predictor/
├── app.py               # Main Flask application & API routes
├── src.ipynb            # Jupyter notebook for EDA & ML Model training
├── heart.csv            # Clinical dataset
├── encoder.pkl          # Pickled StandardScaler for input normalization
├── model.pkl            # Pickled Random Forest Machine Learning model
├── .env                 # Environment variables (API keys)
├── README.md            # Project documentation
└── templates/
    ├── index.html       # Input form for clinical parameters
    └── result.html      # AI Analysis & Risk prediction output
```

---

## 📊 Model Performance

The predictive engine uses a `RandomForestClassifier` optimized via Hyperparameter Tuning. Evaluated on test splits of the dataset, the model achieved an outstanding **Accuracy of 98%**, with high precision and recall across both the High Risk and Low Risk classes. All inputs are normalized via `StandardScaler` to maintain structural integrity before prediction.

---

## 🛠️ The 13 Clinical Parameters Assessed
1. **Age**
2. **Gender** 
3. **Chest Pain Type** (Typical, Atypical, Non-anginal, Asymptomatic)
4. **Resting Blood Pressure** (mm Hg)
5. **Serum Cholesterol** (mg/dl)
6. **Fasting Blood Sugar** (> 120 mg/dl)
7. **Resting ECG Results**
8. **Maximum Heart Rate Achieved**
9. **Exercise Induced Angina**
10. **ST Depression** (Oldpeak)
11. **Slope of Peak Exercise ST Segment**
12. **Number of Major Vessels** (Fluoroscopy)
13. **Thallium Stress Test Result**

---

## 🚀 Installation & Setup

Follow these steps to run the predictor locally on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Heart-Disease-Predictor.git
cd Heart-Disease-Predictor
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install flask scikit-learn pandas google-genai markdown python-dotenv
```

### 3. Setup your Environment Variables
Create a file named `.env` in the root directory of the project and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
Start the Flask web server:
```bash
python app.py
```
*The app will be live at `http://127.0.0.1:5000`*

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.
