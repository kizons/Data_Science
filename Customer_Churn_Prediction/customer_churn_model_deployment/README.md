# 🧠 Customer Churn Prediction - Flask Web App

A simple machine learning Flask web app that predicts whether a customer will churn based on user input.

## 🚀 Features

- Trained classification model to predict customer churn
- Web interface for entering input and getting predictions
- Modular Flask structure
- Easily deployable locally or on cloud platforms

## 🗂️ Project Structure

```
customer-churn-flask-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── model.py
│   ├── utils.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│
├── models/
│   └── churn_model.pkl
├── data/
│   └── train.csv
├── requirements.txt
├── flask_app.py
├── .gitignore
├── Dockerfile
├── LICENSE
└── README.md
```

## ⚙️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/kizons/Data_Science/tree/main/Customer_Churn_Prediction/customer-churn-model-deployment.git
cd customer-churn-model-deployment
```

2. **Create a virtual environment and activate it**
```bash
python -m venv venv
source venv/bin/activate   # on Windows use `. venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
python flask_app.py
```

Then visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 🐳 Run with Docker

```bash
docker build -t churn-prediction-app .
docker run -p 5000:5000 churn-prediction-app
```

## 🛠 Technologies Used

- Python
- Flask
- scikit-learn
- HTML/CSS (Jinja2 templates)
- pandas / joblib

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
