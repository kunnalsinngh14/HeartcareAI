# Loading libraries
import pickle
from flask import Flask, request, render_template
from google import genai
import os
from dotenv import load_dotenv
import markdown

load_dotenv()
app = Flask(__name__)

# Pickle part
encoder = pickle.load(open('encoder.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

#main code 

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        input_data = [[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]]
        encoded_data = encoder.transform(input_data)

        prediction = model.predict(encoded_data)

        if prediction == 1:
            result = "High Risk of Heart Disease"
        else:
            result = "Low Risk of Heart Disease"
        
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents= f"""The heart disease prediction model has classified this patient as:
        {result}
        The details of the patient are:
        - Age (years): {age}
        - Sex (1 = male, 0 = female): {sex}
        - Chest pain type: {cp}
        - Resting blood pressure (mm Hg): {trestbps}
        - Serum cholesterol (mg/dl): {chol}
        - Fasting blood sugar > 120 mg/dl (1 = true, 0 = false): {fbs}
        - Resting electrocardiographic results: {restecg}
        - Maximum heart rate achieved: {thalach}
        - Exercise induced angina (1 = yes, 0 = no): {exang}
        - ST depression induced by exercise relative to rest: {oldpeak}
        - Slope of the peak exercise ST segment: {slope}
        - Number of major vessels colored by fluoroscopy: {ca}
        - Thallium Stress Test Result: {thal}
        Explain why this prediction may have occurred based on the patient's values
        then provide :
        Recommend foods to eat more often, foods or habits to avoid, suggest exercise and activity recommendations suitable for general heart health.        
        Provide the response in simple language that a non-medical person can understand.
        """
        )

        reply = markdown.markdown(response.text)
        
        
        return render_template('result.html', result=result, reply=reply)
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    
