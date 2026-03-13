import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(
    page_title="Food Delivery Sentiment Analyzer",
    page_icon="🍕",
    layout="centered"
)

st.title("🍕 Food Delivery Sentiment Analyzer")
st.subheader("Analyze customer reviews for Zomato, Swiggy & Blinkit")
st.markdown("---")

analyzer = SentimentIntensityAnalyzer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.strip()
    return text


def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word)
              for word in tokens
              if word not in stop_words
              and len(word) > 2]
    return ' '.join(tokens)


def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'Positive', score
    elif score <= -0.05:
        return 'Negative', score
    else:
        return 'Neutral', score


app_name = st.selectbox(
    "Select App:",
    ["Zomato", "Swiggy", "Blinkit"]
)

review = st.text_area(
    "Enter Customer Review:",
    placeholder="Type your review here...",
    height=150
)

if st.button("Analyze Sentiment", type="primary"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            cleaned = clean_text(review)
            processed = preprocess_text(cleaned)
            sentiment, score = get_sentiment(processed)

        st.markdown("---")
        st.subheader("Analysis Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("App", app_name)

        with col2:
            if sentiment == "Positive":
                st.metric("Sentiment", "Positive 😊")
            elif sentiment == "Negative":
                st.metric("Sentiment", "Negative 😞")
            else:
                st.metric("Sentiment", "Neutral 😐")

        with col3:
            st.metric("Confidence Score", f"{abs(score):.2f}")

        if sentiment == "Positive":
            st.success("This review reflects a POSITIVE customer experience!")
        elif sentiment == "Negative":
            st.error("This review reflects a NEGATIVE customer experience!")
        else:
            st.info("This review reflects a NEUTRAL customer experience!")

        st.markdown("---")
        st.subheader("Business Insight")

        if sentiment == "Negative":
            st.write(f"**Recommendation for {app_name}:**")
            keywords = processed.split()
            if any(word in keywords for word in
                   ['deliver', 'late', 'slow', 'time']):
                st.write("Delivery speed issue detected — "
                         "optimize delivery routes and partner allocation.")
            elif any(word in keywords for word in
                     ['food', 'quality', 'taste', 'cold']):
                st.write("Food quality issue detected — "
                         "implement stricter restaurant quality checks.")
            elif any(word in keywords for word in
                     ['app', 'crash', 'bug', 'slow']):
                st.write("App performance issue detected — "
                         "prioritize technical fixes and UI improvements.")
            elif any(word in keywords for word in
                     ['price', 'expensive', 'charge', 'fee']):
                st.write("Pricing issue detected — "
                         "review pricing transparency and hidden charges.")
            else:
                st.write("Customer service issue detected — "
                         "improve response time and resolution quality.")

st.markdown("---")
st.markdown(
    "**Indian Food Delivery Sentiment Intelligence System** | "
    "Built with Python, NLTK, VADER & Streamlit"
)