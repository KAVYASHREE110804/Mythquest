import streamlit as st
import requests
from textblob import TextBlob
import plotly.graph_objects as go
import pandas as pd

# --- API KEY ---
api_key = "pub_820399037e539dfb445a3a84daf2508dfd6d8"

# --- Streamlit UI ---
st.title("📰 MYTHQUEST-News Sentiment Analyzer")

topic = st.text_input("Enter a topic (e.g., sports, politics, AI):")

# --- Functions for sentiment ---
def analyze_sentiment(text):
    if text:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    return "Neutral"

def sentiment_score(text):
    if text:
        return round(TextBlob(text).sentiment.polarity, 2)
    return 0.0

# --- Main logic ---
if topic:
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={topic}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
    else:
        if response.status_code == 200:
            data = response.json()
            articles = data.get("results", [])

            # Use description instead of content
            filtered = [
                {"title": a.get("title", ""), "content": a.get("description", "")}
                for a in articles if a.get("title") and a.get("description")
            ]

            # Remove duplicates and junk
            seen = set()
            filtered_unique = []
            for article in filtered:
                content = article["content"].strip()
                if content.lower() != "only available in paid plans" and content not in seen:
                    seen.add(content)
                    filtered_unique.append(article)

            if filtered_unique:
                # Create Pandas DataFrame
                df = pd.DataFrame(filtered_unique)
                df["sentiment"] = df["content"].apply(analyze_sentiment)
                df["score"] = df["content"].apply(sentiment_score)

                st.subheader("📰 News Articles and Sentiments")
                for idx, row in df.iterrows():
                    st.write(f"**{row['title']}**")
                    st.write(row['content'])
                    st.write(f"**Sentiment:** {row['sentiment']} | **Score:** {row['score']}")
                    st.markdown("---")

                # Radar Chart
                sentiment_counts = df["sentiment"].value_counts()
                labels = ['Positive', 'Negative', 'Neutral']
                values = [sentiment_counts.get(l, 0) for l in labels]

                fig = go.Figure(data=go.Scatterpolar(
                    r=values,
                    theta=labels,
                    fill='toself',
                    name='Sentiment'
                ))

                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True)),
                    showlegend=False,
                    title="📊 Sentiment Radar Chart"
                )

                st.plotly_chart(fig)

            else:
                st.warning("No valid articles with full content found.")
        else:
            st.error("Failed to fetch news articles.")
            st.error(f"API Response Code: {response.status_code}")
else:
    st.info("Enter a topic to begin sentiment analysis.")
