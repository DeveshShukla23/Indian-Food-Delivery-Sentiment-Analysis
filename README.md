# 🍕 Indian Food Delivery Sentiment Intelligence System
### A Multi-Source NLP Analysis of Zomato, Swiggy & Blinkit Reviews

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-3776AB?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-NLP%20%7C%20Sentiment%20Analysis-0D47A1?style=for-the-badge)

> 🚀 An end-to-end **Sentiment Intelligence System** analyzing **1459 real customer reviews**
> from India's top food delivery apps — Zomato, Swiggy & Blinkit — using NLP,
> Machine Learning and Deep Learning to extract powerful business insights.
> Data collected directly from **Google Play Store** — 100% original dataset!

## 🌐 Live Demo
### 👉 [Click Here to Try the App](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)

---

## 📌 Project Overview

Customer reviews are a goldmine of business intelligence. This project
builds a complete **Sentiment Intelligence System** that:
- Collects **real reviews** directly from Google Play Store
- Processes text using advanced **NLP techniques**
- Trains and compares **7 models** (5 ML + 2 Deep Learning)
- Delivers **actionable business recommendations** for food delivery companies
- Deploys as an **interactive web application**

---

## 🗄️ Dataset — Real Multi-Source Data

> 💡 Data collected directly from Google Play Store — no Kaggle dataset used!

| Property | Details |
|----------|---------|
| **Source** | Google Play Store (Real Data) |
| **Apps** | Zomato, Swiggy, Blinkit |
| **Total Reviews** | 1459 |
| **Country** | India 🇮🇳 |
| **Language** | English |
| **Collection Method** | google-play-scraper Python library |

---

## 📊 Exploratory Data Analysis

### 🔥 Rating Distribution
> Overall and app-wise rating comparison across all three apps

![Rating Distribution](rating_distribution.png)

### 💬 Sentiment Distribution
> VADER based NLP sentiment vs Rating based sentiment — interesting gap found!

![Sentiment Distribution](sentiment_distribution.png)

### ☁️ Word Cloud Analysis
> Most frequently used words per app — reveals key customer concerns

![WordCloud](wordcloud.png)

### 📏 Review Length Analysis
> Negative reviewers write significantly longer reviews than positive ones!

![Review Length](review_length.png)

---

## 🤖 Models Built & Compared

| Model | Type | Strength |
|-------|------|----------|
| 🌲 Random Forest | ML Ensemble | Best accuracy — combines 100 decision trees |
| ⚡ SVM | ML | Excellent for high-dimensional TF-IDF features |
| 📈 Logistic Regression | ML | Fast, interpretable baseline model |
| 🎯 Naive Bayes | ML | Classic NLP model — probability based |
| 🌳 Decision Tree | ML | Rule-based — most interpretable |
| 🧠 ANN | Deep Learning | Multi-layer neural network — 276K parameters |
| ⚡ Perceptron | Deep Learning | Single layer — simplest neural network |

---

## 📉 Model Results & Performance

### 🏅 Model Accuracy & F1 Score Comparison

![Model Comparison](model_comparison.png)

### 📊 Final ML vs Deep Learning Comparison

![Final Comparison](final_comparison.png)

### 🔢 Detailed Results

| Rank | Model | Type | Accuracy | F1 Score |
|------|-------|------|----------|----------|
| 🥇 | Random Forest | ML | 91.10% | 91.25% |
| 🥈 | SVM | ML | 89.73% | 89.82% |
| 🥉 | ANN | Deep Learning | 87.67% | 87.45% |
| 4 | Logistic Regression | ML | 86.99% | 87.71% |
| 5 | Naive Bayes | ML | 86.64% | 86.14% |
| 6 | Perceptron | Deep Learning | 82.19% | 81.90% |
| 7 | Decision Tree | ML | 73.63% | 76.31% |

> 💡 **Key Finding:** Random Forest outperforms ANN because deep learning needs
> more data to shine — for datasets under 5000 samples, traditional ML wins!

---

## 💡 Business Insights

### 📊 App-wise Sentiment & Satisfaction Score

![Business Insights](business_insight_1.png)

### 🚨 Top Complaint Categories

![Complaints](business_insight_2.png)

### 🎯 Priority Areas for Improvement

![Recommendations](recommendations.png)

### Key Findings:
- 🚚 **Delivery Speed** is #1 complaint — 25.9% of all negative reviews
- 😟 **Swiggy** has highest negative sentiment (19.9%) among all apps
- ⭐ **Zomato** leads with best satisfaction score (4.11/5)
- ✍️ Negative reviewers write **5x longer** reviews than positive ones
- 📲 **App Performance & UI** is second biggest issue (19.6%)
- 💰 **Pricing Transparency** complaints are consistent across all apps

---

## 🖥️ Live Streamlit Web App

> 🎯 Type any food delivery review and get **instant sentiment analysis** with business recommendations!

| Feature | Details |
|---------|---------|
| 📱 Select App | Zomato / Swiggy / Blinkit |
| ✍️ Input | Any customer review text |
| 🎯 Output | Sentiment + Confidence Score |
| 💡 Business Insight | App-specific actionable recommendations |

### 👉 [Try the Live App Here!](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)

---

## 📂 Project Structure

```
Indian-Food-Delivery-Sentiment-Analysis/
│
├── notebooks/
│   ├── 01_Data_Collection.ipynb      # Data scraping & preprocessing
│   ├── 02_EDA.ipynb                  # Visualizations & ML models
│   ├── 03_Deep_Learning.ipynb        # ANN & Perceptron models
│   └── 04_Business_Insights.ipynb   # Business analysis & recommendations
│
├── data/processed/
│   └── processed_reviews.csv         # Cleaned & processed dataset
│
├── streamlit_app/
│   └── app.py                        # Live web application
│
├── *.png                             # All graphs and visualizations
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/DeveshShukla23/Indian-Food-Delivery-Sentiment-Analysis.git
cd Indian-Food-Delivery-Sentiment-Analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Notebooks in Order
```
01_Data_Collection → 02_EDA → 03_Deep_Learning → 04_Business_Insights
```

### 4. Run Streamlit App
```bash
cd streamlit_app
streamlit run app.py
```

---

## 🛠️ Tools & Technologies

| Tool | Usage |
|------|-------|
| **Python 3.13** | Core programming language |
| **NLTK & VADER** | NLP text processing & sentiment analysis |
| **Scikit-Learn** | ML model building & evaluation |
| **TensorFlow & Keras** | Deep learning — ANN & Perceptron |
| **Pandas & NumPy** | Data manipulation & analysis |
| **Matplotlib & Seaborn** | Data visualization |
| **WordCloud** | Text frequency visualization |
| **Streamlit** | Interactive web app deployment |
| **Google Play Scraper** | Real data collection |

---

## 🔮 Future Improvements

- 📦 Collect 5000+ reviews for better deep learning performance
- 🏗️ Build app-specific models for Zomato, Swiggy & Blinkit separately
- ⚡ Add real-time sentiment monitoring dashboard
- 🧠 Implement LSTM for better sequence understanding
- 🌐 Add Hindi/Hinglish review support for wider Indian audience
- 📊 Integrate Power BI dashboard for executive reporting

---

## 👨‍💻 Author

**Devesh Shukla**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devesh-shukla23)
[![GitHub](https://img.shields.io/badge/GitHub-DeveshShukla23-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DeveshShukla23)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shukladevesh40@gmail.com)
[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)

