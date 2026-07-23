## 🎯 Project 1: K-Means Clustering on Iris Dataset

### Description
This notebook applies **K-Means Clustering** on the famous **Iris Dataset** to identify natural groupings of iris flowers based on their petal and sepal measurements.

### Dataset
- **Name:** Iris Dataset (built-in sklearn)
- **Samples:** 150
- **Features:** 4 (Sepal Length, Sepal Width, Petal Length, Petal Width)
- **Target Species:** 3 (Setosa, Versicolor, Virginica)

### Technologies Used
- Python
- Scikit-learn (KMeans, MinMaxScaler)
- Pandas, NumPy
- Matplotlib

### Steps Performed
1. Loaded Iris dataset
2. Selected Petal Length and Petal Width features
3. Applied MinMaxScaler for feature scaling
4. Used **Elbow Method** to find optimal k
5. Applied K-Means with **k=3** (optimal)
6. Visualized clusters with centroids
7. Compared with actual species labels

### Results
- **Optimal k:** 3 (confirmed by elbow method)
- **Accuracy:** ~95%
- **Clusters:**
  - Cluster 0: Iris Setosa (perfectly separated)
  - Cluster 1: Iris Versicolor
  - Cluster 2: Iris Virginica

### Visualizations
- Elbow plot showing optimal k=3
- 3D scatter plot of clusters with different colors
- Centroids marked with black X

---

## 🔬 Project 2: PCA (Principal Component Analysis) on Heart Disease Dataset

### Description
This notebook applies **Principal Component Analysis (PCA)** on the Heart Disease Dataset to reduce dimensionality and analyze the trade-off between feature reduction and model accuracy.

###  Dataset
- **Name:** Heart Disease Dataset (Copy of heart.csv)
- **Samples:** 918
- **Features:** 12 (after preprocessing: ~20 features)
- **Target:** Heart Disease (0 = No, 1 = Yes)

### Technologies Used
- Python
- Scikit-learn (PCA, StandardScaler, KNN, LogisticRegression, RandomForestClassifier)
- Pandas, NumPy
- Matplotlib

### Steps Performed
1. Loaded and preprocessed the dataset
2. Handled missing values (replaced 0 with mean)
3. Performed one-hot encoding for categorical features
4. Applied StandardScaler for feature scaling
5. Applied PCA with different variance values:
   - 95%, 90%, 85%, 80%, 75%, 70%
6. Trained 3 models for each variance:
   - K-Nearest Neighbors (KNN)
   - Random Forest (with Cross-Validation)
   - Logistic Regression (with Cross-Validation)
7. Analyzed accuracy drop and component reduction

### Results

| Variance | Components | KNN Accuracy | RF Accuracy | LR Accuracy |
|----------|-----------|--------------|-------------|-------------|
| 95% | 10 | 85.0% | 84.4% | 83.4% |
| 90% | 8 | 84.7% | 84.2% | 83.1% |
| 85% | 7 | 84.4% | 84.0% | 82.9% |
| 80% | 6 | 84.0% | 83.7% | 82.5% |
| 75% | 5 | 83.5% | 83.3% | 82.0% |
| 70% | 4 | 82.8% | 82.6% | 81.2% |

### Key Findings
- **80-85% variance** gives the best balance
- Components reduced by **30-40%**
- Accuracy loss is only **0.6-1.0%**
- Models become **faster** and use **less memory**

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook or Google Colab

### Installation
# Clone the repository
git clone <repository-url>
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

 Key Learnings
From K-Means Project:
 How to find optimal number of clusters using elbow method

 How to apply K-Means clustering

 How to visualize clusters

 How to evaluate clustering performance

From PCA Project:
 How PCA reduces dimensionality

 How to tune PCA parameters (variance, components)

 How to compare model performance

 How to find optimal balance between speed and accuracy

Author
Name: Jazib Faisal