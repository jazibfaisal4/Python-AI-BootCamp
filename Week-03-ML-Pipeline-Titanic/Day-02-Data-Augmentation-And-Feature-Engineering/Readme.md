# Data Augmentation and Feature Engineering Exercises

This notebook demonstrates various techniques for **feature engineering** in tabular data and **data augmentation** in image and text data. It also includes an experiment to show the impact of class balancing via augmentation on model performance.

---

## Table of Contents

1. [Setup and Data Loading](#1-setup-and-data-loading)
2. [Missing Value Imputation](#2-missing-value-imputation)
3. [Feature Engineering](#3-feature-engineering)
4. [Encoding and Scaling](#4-encoding-and-scaling)
5. [Feature Selection & Modeling](#5-feature-selection--modeling)
6. [Advanced Feature Engineering](#6-advanced-feature-engineering)
7. [Image Data Augmentation](#7-image-data-augmentation)
8. [Text Data Augmentation](#8-text-data-augmentation)
9. [Class Balancing via Augmentation](#9-class-balancing-via-augmentation)
10. [Effect of Augmentation on Model Performance](#10-effect-of-augmentation-on-model-performance)

---

## 1. Setup and Data Loading

### Description
Loading the **Titanic dataset** from a CSV file for tabular data analysis.

### Steps Performed
- Loaded dataset using `pd.read_csv()`
- Displayed first few rows using `df.head()`
- Printed dataset shape using `df.shape`
- Printed count of missing values for each column using `df.isnull().sum()`

### Dataset Info
| Property | Value |
|----------|-------|
| **Source** | Titanic Dataset (Kaggle) |
| **Samples** | 891 |
| **Features** | 12 |
| **Target** | Survived (0/1) |

---

## 2. Missing Value Imputation

### Description
Handling missing values in the Titanic dataset to prepare it for modeling.

### Steps Performed
| Column | Method | Code |
|--------|--------|------|
| **Age** | Filled with **median** | `df['Age'].fillna(df['Age'].median(), inplace=True)` |
| **Embarked** | Filled with **mode** | `df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)` |
| **Cabin** | Replaced with **'Unknown'** | `df['Cabin'].fillna('Unknown', inplace=True)` |

---

## 3. Feature Engineering

###  Description
Creating new informative features from existing data to improve model performance.

### Features Created

| Feature | Method | Description |
|---------|--------|-------------|
| **Title** | Extracted from Name | Mr, Mrs, Miss, Master, Rare |
| **FamilySize** | SibSp + Parch + 1 | Total family members including self |
| **IsAlone** | Binary (1 if FamilySize == 1) | Passenger traveling alone |
| **FarePerPerson** | Fare / FamilySize | Fare divided by family size |
| **AgeBin** | Binning (0-12, 13-18, 19-65, >65) | Child, Teenager, Adult, Elderly |
| **FareBin** | Quantile binning | Low, Medium, High, Very High |
| **Deck** | First letter of Cabin | C, B, D, E, F, U (Unknown), Other |

---

## 4. Encoding and Scaling

### Description
Converting categorical variables to numerical format and scaling numerical features.

### One-Hot Encoding
Applied to categorical features:

categorical = ['Pclass', 'Sex', 'Embarked', 'Title', 'AgeBin', 'FareBin', 'Deck']
df_encoded = pd.get_dummies(df[categorical], drop_first=True)
Feature Scaling
Used three different scalers:

Scaler	Use Case
StandardScaler	Normal distribution (mean=0, std=1)
MinMaxScaler	Bounded range (0 to 1)
RobustScaler	Outliers present (median-based)

X_std = scaler_std.fit_transform(X)
X_mm  = scaler_mm.fit_transform(X)
X_rb  = scaler_rbv.fit_transform(X)
5. Feature Selection & Modeling
Description
Selecting the most important features and training a classification model.

Feature Selection

selector = SelectKBest(f_classif, k=15)
X_sel = selector.fit_transform(X_std, y)
Used ANOVA F-test for feature importance

Selected top 15 features

Model Training

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
Evaluation Metrics
Accuracy Score

Classification Report (Precision, Recall, F1-Score)

6. Advanced Feature Engineering
Description
Applying polynomial features and PCA for dimensionality reduction.

Polynomial Features

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_data = poly.fit_transform(df[['Age', 'Fare']].fillna(0))
Generated features:

Age, Fare

Age^2, Fare^2

Age * Fare (interaction)

PCA (Principal Component Analysis)
python
pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_std)
Reduced dimensions from ~30 to 10

Visualized explained variance ratio

Calculated cumulative variance

7. Image Data Augmentation
Description
Applying various augmentation techniques to MNIST handwritten digit images.

MNIST Data Preparation

(X_train_img, y_train_img), (X_test_img, y_test_img) = mnist.load_data()
X_train_img = X_train_img / 255.0
X_train_img = X_train_img.reshape(-1, 28, 28, 1)
Augmentation Methods
Method	Library	Techniques Used
Keras ImageDataGenerator	TensorFlow/Keras	Rotation, Shift, Zoom, Shear, Brightness
tf.image	TensorFlow	Rotation (rot90), Brightness, Contrast
OpenCV	OpenCV + scipy	Rotation, Gaussian Blur, Zoom
Albumentations	Albumentations	ElasticTransform, GridDistortion, OpticalDistortion
8. Text Data Augmentation
Description
Applying augmentation techniques to text data using word-level transformations.

Sample Texts

texts = [
    "This is a great product, I love it!",
    "The service was terrible and I'm disappointed.",
    "I'm not sure how I feel about this experience.",
    "The food was delicious and the staff was friendly.",
    "This movie is boring and too long."
]
Augmentation Functions
Function	Description	Example
swap_words()	Swaps two random words	"This a is great product"
delete_random_word()	Deletes a random word	"This is a product"
insert_random_word()	Inserts a random word	"This is a really great product"
9. Class Balancing via Augmentation
Description
Addressing class imbalance by augmenting minority classes.

Class Distribution Visualization
python
unique, counts = np.unique(y_train_img, return_counts=True)
plt.bar(unique, counts)
augment_minority_class() Function
Step	Description
1	Find indices of target class
2	Check if enough samples exist
3	Use ImageDataGenerator to generate augmentations
4	Combine original + augmented data
5	Return balanced X and y
Imbalanced Dataset Creation

# Example: 100 samples per class, 20 for class '8'
X_imbalanced, y_imbalanced = create_imbalanced_dataset(...)

10. Effect of Augmentation on Model Performance

Description
Comparing model performance on imbalanced vs balanced datasets.

CNN Model Architecture
python
model = tf.keras.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
Training Comparison

Model	            Training Data	  Epochs
Imbalanced Model	Imbalanced subset	5
Balanced Model	    After augmentation	5
Evaluation Plots
Accuracy Comparison (Training & Validation)

Loss Comparison (Training & Validation)

Expected Observation

Balanced model typically shows better validation accuracy and lower overfitting compared to the imbalanced model.