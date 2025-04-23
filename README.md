
# 📰 MYTHQUEST - News Sentiment Analyzer

This project is a simple Streamlit web application that allows users to search for news articles by topic and analyze the **sentiment** of each article using **TextBlob**.

## 🚀 Features
- Enter any topic (e.g., "AI", "Sports", "Politics") to search latest news articles.
- Perform **Sentiment Analysis** (Positive, Negative, Neutral) on each article's description.
- Display Sentiment Scores.
- Visualize the overall sentiment distribution using a **Radar Chart** created with **Plotly**.

## 🛠️ Technologies Used
- Python
- Streamlit
- Requests
- TextBlob
- Plotly
- Pandas

## 📦 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/mythquest-news-analyzer.git
cd mythquest-news-analyzer
pip install -r requirements.txt
```

## 🧑‍💻 Run Locally

```bash
streamlit run app.py
```

## 🔑 API Key
This app uses the [NewsData.io API](https://newsdata.io/) for fetching news articles.  
Replace the `api_key` variable in the code with your own API key if needed.

## 📸 Screenshots

| News List and Sentiments | Radar Chart |
|:------------------------:|:-----------:|
| ![News Example](./screenshots/news_example.png) | ![Radar Chart](./screenshots/radar_chart.png) |

## ✨ Demo
- Coming soon after deployment!

## 📄 License
This project is licensed under the MIT License.

---
Made with ❤️ using Streamlit
