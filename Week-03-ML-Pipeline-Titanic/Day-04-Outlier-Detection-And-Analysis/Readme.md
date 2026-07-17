# Outlier Detection and Analysis

## Overview
This notebook provides a comprehensive exploration of outlier detection techniques and their impact on data analysis and machine learning models. It covers various methods for identifying outliers, handling them, and assessing their influence on statistical measures and predictive models.

---

## Dataset
The exercises utilize the **California Housing dataset**, a popular dataset for regression tasks. It includes features like:
- **MedInc**: Median Income
- **HouseAge**: Median House Age
- **AveRooms**: Average Rooms per Household
- **Population**: Block Group Population
- **MedHouseVal**: Median House Value (Target Variable)

---

## Exercises Overview

| # | Exercise | Description |
|---|----------|-------------|
| 1 | **EDA for Outlier Detection** | Visual identification using histograms and box plots |
| 2 | **Univariate Outlier Detection** | Z-score and IQR methods on MedHouseVal |
| 3 | **Isolation Forest** | ML-based outlier detection algorithm |
| 4 | **Impact on Linear Regression** | Compare model performance with/without outliers |
| 5 | **Custom Outlier Workflow** | Ensemble function combining Z-score + IQR |
| 6 | **Robust Feature Engineering** | Log transformation, binning, and ratio features |
| 7 | **Multivariate Outlier Detection** | Mahalanobis distance with chi-squared threshold |

---

## Key Findings

- Outliers can significantly skew statistical measures (mean, standard deviation).
- Different outlier detection methods (Z-score, IQR, Isolation Forest, Mahalanobis distance) identify varying sets of outliers. Choice depends on data distribution and domain knowledge.
- Removing or transforming outliers can improve the performance and robustness of machine learning models.
- Feature engineering (log transformation) effectively reduces skewness and outliers.

---

## Usage

1. Open the notebook in Jupyter or Google Colab.
2. Execute each code cell sequentially.
3. Review visualizations and outputs as they appear.

---

## Dependencies

pip install numpy pandas matplotlib seaborn scikit-learn scipy

Sample Output

MedHouseVal outliers (Z-score): 0 found
MedHouseVal outliers (IQR): 1071 found
Isolation Forest outliers: 1032 found


Author
Jazib Faisal

Date
17 July 2026