<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:1a1a2e,100:FF6B6B&height=200&section=header&text=Indian%20Food%20Delivery%20Sentiment%20Analysis&fontSize=38&fontColor=FF6B6B&fontAlignY=38&desc=NLP%20%7C%207%20Models%20%7C%20Zomato%20%E2%80%A2%20Swiggy%20%E2%80%A2%20Blinkit%20%7C%20Live%20Streamlit%20App&descAlignY=58&descSize=16&descColor=a0aec0&animation=fadeIn)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=FF6B6B&center=true&vCenter=true&width=850&lines=NLP+%7C+Sentiment+Analysis+%7C+1459+Real+Reviews;7+Models+%7C+Random+Forest+91.10%25+%F0%9F%8F%86;Zomato+%E2%80%A2+Swiggy+%E2%80%A2+Blinkit+%7C+Google+Play+Store+Data;Live+Streamlit+App+Deployed+%F0%9F%9A%80+%7C+100%25+Real+Dataset+%E2%9C%85)](https://git.io/typing-svg)

<br>

![Status](https://img.shields.io/badge/Status-Completed%20✅-FF6B6B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-3776AB?style=for-the-badge)

<br>

[![Live App](https://img.shields.io/badge/🚀%20LIVE%20APP-Try%20It%20Now-FF6B6B?style=for-the-badge)](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Devesh_Shukla-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devesh-shukla23)
[![GitHub](https://img.shields.io/badge/GitHub-DeveshShukla23-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DeveshShukla23)

</div>

---

## 🍕 About This Project
```python
project = {
    "name"      : "Indian Food Delivery Sentiment Intelligence System",
    "data"      : "1459 Real Reviews — Google Play Store",
    "apps"      : ["Zomato", "Swiggy", "Blinkit"],
    "models"    : 7,
    "best_model": "Random Forest — 91.10% Accuracy",
    "techniques": ["NLP", "TF-IDF", "VADER", "ML", "Deep Learning"],
    "deployment": "Live Streamlit Web App",
    "outcome"   : "🏆 Actionable business recommendations for food delivery companies"
}
```

> 💡 *"Customer reviews are a goldmine of business intelligence — if you know how to mine them."*

---

## 📊 Dataset — Real Multi-Source Data

<div align="center">

| 📱 Apps | 📝 Total Reviews | 🌍 Country | 🔗 Source |
|:---:|:---:|:---:|:---:|
| **Zomato • Swiggy • Blinkit** | **1,459** | **India 🇮🇳** | **Google Play Store** |

</div>

> ⚡ Data collected directly from Google Play Store using `google-play-scraper` — no Kaggle dataset used!

---

## 📈 Exploratory Data Analysis

### Rating Distribution
![Rating Distribution](rating_distribution.png)

### Sentiment Distribution
![Sentiment Distribution](sentiment_distribution.png)

### Word Cloud Analysis
![WordCloud](wordcloud.png)

### Review Length Analysis
![Review Length](review_length.png)

---

## 🤖 7 Models Built & Compared

<div align="center">

| Rank | Model | Type | Accuracy | F1 Score |
|:---:|:---:|:---:|:---:|:---:|
| 🥇 | **Random Forest** | ML Ensemble | **91.10%** | **91.25%** |
| 🥈 | SVM | ML | 89.73% | 89.82% |
| 🥉 | ANN | Deep Learning | 87.67% | 87.45% |
| 4 | Logistic Regression | ML | 86.99% | 87.71% |
| 5 | Naive Bayes | ML | 86.64% | 86.14% |
| 6 | Perceptron | Deep Learning | 82.19% | 81.90% |
| 7 | Decision Tree | ML | 73.63% | 76.31% |

</div>

> 💡 **Key Finding:** Random Forest beats ANN — for datasets under 5000 samples, traditional ML wins over Deep Learning!

### Model Comparison Charts

![Model Comparison](model_comparison.png)
![Final Comparison](final_comparison.png)
![ANN Training History](ann_training_history.png)
![Confusion Matrix](confusion_matrix.png)

---

## 💡 Business Insights

### App-wise Sentiment & Satisfaction Score
![Business Insights 1](business_insight_1.png)

### Top Complaint Categories
![Business Insights 2](business_insight_2.png)

### Priority Areas for Improvement
![Recommendations](recommendations.png)
```
🚚  Delivery Speed    → #1 complaint — 25.9% of all negative reviews
😟  Swiggy            → highest negative sentiment (19.9%) among all apps
⭐  Zomato            → leads with best satisfaction score (4.11/5)
✍️  Negative reviews  → 5x longer than positive ones
📲  App Performance   → second biggest issue (19.6%)
💰  Pricing           → transparency complaints consistent across all apps
```

---

## 🖥️ Live Streamlit App

<div align="center">

| Feature | Details |
|:---:|:---:|
| 📱 Select App | Zomato / Swiggy / Blinkit |
| ✍️ Input | Any customer review text |
| 🎯 Output | Sentiment + Confidence Score |
| 💡 Insight | App-specific actionable recommendations |

### 👉 [Try the Live App Here!](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)

</div>

---

## 📂 Project Structure
```
Indian-Food-Delivery-Sentiment-Analysis/
│
├── 01_Data_Collection.ipynb     → Data scraping & preprocessing
├── 02_EDA.ipynb                 → Visualizations & ML models
├── 03_Deep_Learning.ipynb       → ANN & Perceptron models
├── 04_Business_Insights.ipynb   → Business analysis & recommendations
├── app.py                       → Live Streamlit web application
├── processed_reviews.csv        → Cleaned & processed dataset
├── requirements.txt             → Python dependencies
├── *.png                        → All graphs and visualizations
└── README.md
```

---

## 🚀 Run Locally
```bash
git clone https://github.com/DeveshShukla23/Indian-Food-Delivery-Sentiment-Analysis.git
cd Indian-Food-Delivery-Sentiment-Analysis
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-3776AB?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![WordCloud](https://img.shields.io/badge/WordCloud-Text%20Viz-FF6B6B?style=for-the-badge)

</div>

---

## 🔮 Future Improvements
```
📦  Collect 5000+ reviews for better deep learning performance
🏗️  Build app-specific models for Zomato, Swiggy & Blinkit separately
⚡  Add real-time sentiment monitoring dashboard
🧠  Implement LSTM for better sequence understanding
🌐  Add Hindi/Hinglish review support for wider Indian audience
📊  Integrate Power BI dashboard for executive reporting
```

---

## 💡 Skills Demonstrated

<div align="center">

| NLP | Machine Learning | Deployment |
|:---:|:---:|:---:|
| ✅ Text Preprocessing | ✅ 7 Models Compared | ✅ Streamlit App |
| ✅ VADER Sentiment | ✅ Random Forest 91.10% | ✅ Live Deployment |
| ✅ TF-IDF Vectorization | ✅ ANN & Perceptron | ✅ Real Data Collection |
| ✅ Word Cloud | ✅ Model Evaluation | ✅ Business Insights |

</div>

---

## 👨‍💻 Author

<div align="center">

**Devesh Shukla**
*Data Analyst | NLP Engineer | Builder*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Devesh_Shukla-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devesh-shukla23)
[![GitHub](https://img.shields.io/badge/GitHub-DeveshShukla23-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DeveshShukla23)
[![Live App](https://img.shields.io/badge/🚀%20Try%20Live%20App-FF6B6B?style=for-the-badge)](https://indian-food-delivery-sentiment-analysis-lug5wqpmv42siqiu2aisxa.streamlit.app/)
[![CHANAKYA](https://img.shields.io/badge/My%20Capstone-CHANAKYA-00D4AA?style=for-the-badge)](https://github.com/DeveshShukla23/CHANAKYA)

<br>

⭐ **If you find this useful, please give it a star!** ⭐

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:1a1a2e,100:FF6B6B&height=120&section=footer&animation=fadeIn)

</div>
