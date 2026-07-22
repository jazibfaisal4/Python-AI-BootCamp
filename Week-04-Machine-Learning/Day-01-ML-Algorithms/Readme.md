## Assignment Overview

This assignment contains **4 Jupyter Notebooks** covering different machine learning algorithms:

| # | File Name | Topic | Status |
|---|-----------|-------|--------|
| 1 | `decision_tree_classifier.ipynb` | Decision Tree Classifier (Titanic Dataset) | Complete |
| 2 | `support_vector_machine.ipynb` | Support Vector Machine (Digits Dataset) | Complete |
| 3 | `linear_regression_exercise.ipynb` | Linear Regression (Restaurant Profit) | Complete |
| 4 | `linear_regression_solved.ipynb` | Linear Regression (Cars & Hiring Dataset) | Complete |

---

#Datasets Used

| Dataset | Purpose | Type |
|---------|---------|------|
| Titanic | Survival Prediction | Classification |
| Digits (sklearn) | Digit Recognition | Classification |
| Restaurant Profit | Profit Prediction | Regression |
| Cars Price | Price Prediction | Regression |
| Hiring | Salary Prediction | Regression |

---

## Libraries Used

- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `matplotlib` - Data visualization
- `seaborn` - Statistical visualization
- `scikit-learn` - Machine Learning algorithms
  - `sklearn.tree` - Decision Tree
  - `sklearn.svm` - Support Vector Machine
  - `sklearn.linear_model` - Linear Regression
  - `sklearn.model_selection` - Train-Test Split
  - `sklearn.preprocessing` - Label Encoding
  - `sklearn.metrics` - Model Evaluation
- `pickle` - Model persistence
- `math` - Mathematical functions

---

## Results Summary

### Classification Models

| Model | Dataset | Accuracy |
|-------|---------|----------|
| **Decision Tree** | Titanic | ~80% |
| **SVM** | Digits | ~98% |

### Regression Models

| Model | Dataset | Best Cost/R² |
|-------|---------|--------------|
| **Linear Regression** | Restaurant Profit | Cost minimized |
| **Linear Regression** | Cars Price | R²: [Value] |
| **Linear Regression** | Hiring Salary | R²: [Value] |

---

## Key Learnings

### 1. Decision Tree Classifier
- Data preprocessing (handling missing values)
- Feature engineering (creating new features)
- Train-test split
- Model training and evaluation
- Feature importance analysis

### 2. Support Vector Machine (SVM)
- Working with image data (Digits dataset)
- High-dimensional classification
- Model accuracy comparison

### 3. Linear Regression
- Cost function implementation
- Gradient descent algorithm
- Multiple linear regression
- One-hot encoding for categorical variables
- Model persistence using pickle

### 4. Data Preprocessing Techniques
- Handling missing values (mean, mode, median)
- Label encoding (categorical → numerical)
- One-hot encoding
- Feature scaling

---

## Instructions to Run

1. **Install required libraries:**
   pip install pandas numpy matplotlib seaborn scikit-learn
Open Jupyter Notebook:

jupyter notebook
Run cells sequentially:

Open each .ipynb file

Run cells from top to bottom (Shift + Enter)

Datasets:

All CSV files are included in the respective folders

Some datasets are loaded directly from sklearn

Checklist
☑ Data Loading
☑ Data Preprocessing
☑ Exploratory Data Analysis
☑ Feature Engineering
☑ Model Training
☑ Model Evaluation
☑ Predictions
☑ Results Visualization

Acknowledgments
Course: Python AI Bootcamp

Date: 22 July 2026

Name: Jazib Faisal

Email: jazibfaisal4@gmail.com


