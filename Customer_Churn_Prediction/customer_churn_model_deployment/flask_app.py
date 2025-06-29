import joblib
from flask import Flask, request, render_template
import pandas as pd
from feature_utils import feature_engineering


app = Flask(__name__)
pipeline = joblib.load('pipeline.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_dict = request.form.to_dict()
        input_df = pd.DataFrame([input_dict])
        prediction = pipeline.predict(input_df)
        return render_template('index.html', prediction_text=f"The churn prediction is: {prediction[0]}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
