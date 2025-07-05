# 🔮 Customer Churn Prediction

Predicting which customers are likely to stop using a service using machine learning techniques. This project helps businesses identify churn risk and take proactive steps to improve customer retention.

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Data](#data)
- [Results](#results)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 📝 Overview

Customer churn prediction is a vital task for subscription-based businesses. The goal of this project is to build a supervised machine learning model that accurately predicts whether a customer will churn (i.e., discontinue using a product or service).

## ✨ Features

- ✅ End-to-end machine learning pipeline
- ✅ Exploratory Data Analysis (EDA) and visualization
- ✅ Feature engineering and preprocessing
- ✅ Multiple model training and evaluation (Logistic Regression, Random Forest, XGBoost, etc.)
- ✅ Model performance tracking and comparison
- ✅ Inference script for real-time churn prediction
- ✅ Clean, modular code structure

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/kizons/Data_Science.git
cd customer_churn_prediction
pip install -r requirements.txt
```

(Optional: Set up a virtual environment or use Docker)

## 🚀 Usage

Run data preprocessing and train the model:

```bash
python src/train.csv --config configs/train_config.yaml
```

Run inference on new data:

```bash
python src/test.csv --input data/test.csv
```

Explore notebooks:

```bash
jupyter notebook notebooks/EDA.ipynb
```

## 🧠 Model Details

- **Model types**: KNN, Logistic Regression, Naive Bayes, Decision Tree, Random Forest, XGBoost
- **Frameworks**: Scikit-learn, XGBoost
- **Target variable**: `Churn` (binary: Yes/No)
- **Input features**: state, account_length, area_code, international_plan, voice_mail_plan, number_vmail_messages, etc.
- **Evaluation metrics**: Accuracy

## 📊 
- **Source**: [Data Kostas Diamantaras](https://kaggle.com/competitions/customer-churn-prediction-2020)
- **Samples**: ~4,250 customers
- **Features**:
  - international_plan (e.g., yes or no)
  - voice_mail_plan (e.g., yes or no)
  - total_day_minutes
  - etc
- **Preprocessing**:
  - Handling outliers
  - Encoding categorical variables
  - Feature scaling

## 📈 Results

| Model            | Accuracy | F1-Score | ROC AUC |
|------------------|----------|----------|---------|
| Logistic Regression | 77.7%   | 0.48     | 0.81    |
| Random Forest    | 94.5%   | 0.81     | 0.92    |
| XGBoost          | 96.9%   | 0.89     | 0.92    |
| Decision Tree    | 94.0%   | 0.81      | 0.90   |
| KNN   | 81.2%   |  0.32   | 0.60   |
|  Naive Bayes   | 54.0%   | 0.27   |  0.60   |

(Include plots: ROC curves, feature importance, confusion matrix, etc.)

## 📁 Project Structure

```
customer-churn-prediction/
├── data/                  # Raw and processed data
├── notebooks/             # Jupyter notebooks for EDA, experiments
├── models/                # Saved model files
├── src/                   # Core source code (train.py, test.py, utils/)
│   ├── preprocessing.py
│   ├── train.py
│   ├── test.py
├── configs/               # Configuration YAML files
├── requirements.txt       
├── README.md
└── ...
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch and open a pull request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact

Email: [okaforkizito@gmail.com](mailto:okaforkizito@gmail.com)  
GitHub: [@kizons](https://github.com/kizons)
