EDA Challenge: Titanic Survival Analysis by Title
https://img.shields.io/badge/Python-3.x-blue.svg
https://img.shields.io/badge/Pandas-2.x-yellow.svg
https://img.shields.io/badge/Seaborn-0.12.x-green.svg

Table of Contents
Introduction

Exercise Goal

Key Steps Performed

Key Findings

Visualizations

Technologies Used

Getting Started

Conclusions

License

Introduction
This notebook performs an Exploratory Data Analysis (EDA) on the classic Titanic dataset. The primary goal of this specific exercise was to investigate the relationship between a passenger's title (e.g., Mr, Mrs, Miss) and their chances of survival, and to draw conclusions based on these findings.

Exercise Goal
The core objective was to understand if and how a passenger's social title influenced their survival probability during the Titanic disaster.

Key Question
"Did your title determine your fate on the Titanic?"

Key Steps Performed
1. Data Loading & Initial Inspection
Loaded Titanic dataset using pandas

Examined initial structure (df.info())

Generated summary statistics (df.describe())

Checked missing values (df.isnull().sum())

2. Univariate Analysis
Visualized distributions of numerical features ('Age', 'Fare')

Used histograms and boxplots

Explored categorical features ('Pclass', 'Sex', 'Embarked', 'Survived')

Created count plots for categorical variables

3. Bivariate Analysis
Visualized relationships between 'Survived' and:

Age

Fare

Pclass

Sex

Embarked

Used histograms, boxplots, and bar plots

4. Correlation Analysis
Computed correlation matrix for numerical variables

Visualized with heatmap

Understood inter-feature relationships

5. Outlier Detection
Applied Z-score method

Used IQR method

Detected outliers in 'Fare' column

Visualized outliers

6. Feature Engineering
Created 'AgeGroup' feature

Created 'FareCategory' feature

Created 'FamilySize' feature

Analyzed impact on survival rates

7. Title-Based Survival Analysis (Exercise Specific)
Title Extraction
Extracted titles from 'Name' column using regular expressions

Identified unique titles in dataset

Title Grouping
Grouped less frequent titles into 'Rare' category

Simplified analysis for better insights

Visualizations
Histograms showing survival distribution by title

Boxplots for title vs survival

Bar plots for survival rates by title

Statistical Calculation
Calculated survival rates for each title group

Quantified observed differences

Multi-factor Analysis (Bonus)
Explored relationship between 'Title_Group', 'Pclass', and 'Survived'

Created comprehensive visualizations

Key Findings
Survival Rates by Title Group
Title Group	Total	Survived	Survival Rate	Death Rate
Mrs	125	99	79.2%	20.8%
Miss	182	127	69.8%	30.2%
Master	48	23	47.9%	52.1%
Rare	18	7	38.9%	61.1%
Mr	517	81	15.7%	84.3%
Key Insights
#	Pattern	Insight
1	Women (Mrs/Miss)	Highest survival rates (70-79%)
2	Children (Master)	Moderate survival (48%)
3	Men (Mr)	Lowest survival rate (16%)
4	Rare Titles	Varied survival (39%)
Visualizations
1. Title Analysis
Stacked bar chart: Survival count by title group

Horizontal bar chart: Survival rate by title group

Pie chart: Passenger distribution by title

2. Multi-Factor Analysis
Title × Passenger Class

Title × Age Group

Title × Sex

3. Key Visualizations
Age distribution by title and survival

Fare distribution by title and survival

Correlation matrix of numerical variables

Tools Used
Library	Purpose
Python	Programming language
Pandas	Data manipulation and analysis
Matplotlib	Basic plotting
Seaborn	Statistical data visualization
SciPy	Statistical functions (Z-score, Chi-square)
NumPy	Numerical operations
Getting Started
Prerequisites
bash
Python 3.x
pip
Installation
bash
# Clone the repository
git clone https://github.com/yourusername/titanic-eda-title-analysis.git
cd titanic-eda-title-analysis

# Install dependencies
pip install -r requirements.txt
Requirements
txt
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
jupyter>=1.0.0
Running the Analysis
bash
jupyter notebook titanic_eda_analysis.ipynb
Conclusions
1. Strong Predictor
A passenger's title was found to be a strong predictor of survival on the Titanic.

2. Survival Rate Disparities
Group	Survival Rate	Observation
Women (Mrs/Miss)	70-79%	Highest survival rates
Children (Master)	48%	Relatively high survival
Men (Mr)	16%	Lowest survival rate
Rare Titles	39%	Varied survival rates
3. Influence of Social Hierarchy/Policy
Observed patterns strongly align with 'women and children first' policy

Reflects social class differences

Women and children were prioritized during evacuation

4. Combined Factors
Even within title groups, 'Pclass' played a significant role:

First Class Women: ~97% survival

Third Class Men: ~10% survival

Survival was a complex interplay of gender, age, and socioeconomic status

5. Statistical Significance
Test	Value	Conclusion
Chi-square	288.643	 p < 0.001
Interpretation	Title and survival are NOT independent	Significant relationship
Key Takeaways
Title extraction reveals important social patterns

Feature engineering (title extraction) reveals crucial insights

Thorough EDA reveals dataset patterns and relationships

Multi-factor analysis provides deeper understanding

Title combined with class and gender gives complete picture

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Kaggle for the Titanic dataset

Python AI Bootcamp for the curriculum

Data Science Community for inspiration

Author
Jazib Faisal

GitHub: https://www.linkedin.com/in/jazib-faisal-5a8978322

LinkedIn: Your LinkedIn

Show Your Support
If you found this analysis helpful, please give it a Star on GitHub!

<div align="center"> <h3> "Title on the Titanic was NOT just a formality - it determined who got a seat on the lifeboats."</h3> <br> Made with ❤️ for Day 9 of Python AI Bootcamp </div>

Quick Stats

Metric	Value
Total Passengers	891
Overall Survival Rate	38.4%
Women Survival Rate	74.2%
Men Survival Rate	18.9%
Title Effect (p-value)	< 0.001
Strongest Predictor	Sex + Title + Pclass