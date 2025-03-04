IPL Win Probability Predictor

Overview

The IPL Win Probability Predictor is a machine learning project that predicts the win probability of an IPL match based on real-time match data. Built using Logistic Regression, the model was trained on ball-by-ball IPL data to provide accurate predictions.

Features

Predicts real-time win probability of a team based on match conditions.

User-friendly Streamlit interface for seamless interaction.

Uses ball-by-ball IPL match data for precise analysis.

Achieves 81% accuracy using Logistic Regression with hyperparameter tuning.

Tech Stack

Python

Pandas, NumPy (Data processing)

Scikit-learn (Machine learning model)

Matplotlib, Seaborn (Data visualization)

Streamlit (Web app deployment)

Dataset

Ball-by-ball IPL match data (Till last season)

Preprocessed features like runs left, balls left, wickets, CRR, RRR

Model Development

Data Preprocessing: Handled missing values, feature scaling, and categorical encoding.

Feature Engineering: Created key predictors like runs left, balls left, wickets left, CRR, RRR.

Model Training & Optimization: Applied Logistic Regression, fine-tuned hyperparameters, and used cross-validation.

Evaluation: Achieved 81% accuracy using Log Loss and AUC-ROC.

Deployment: Built an interactive Streamlit app for real-time predictions.

How to Run

Clone the repository:

git clone https://github.com/yourusername/IPL-Win-Predictor.git
cd IPL-Win-Predictor

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Future Enhancements

Improve accuracy by trying different ML models like Random Forest or XGBoost.

Incorporate live match data for real-time analysis.

Enhance UI for better user experience.



