import requests, os, time
from dotenv import load_dotenv
import schedule

# Load environment variables
load_dotenv()

news_api = os.getenv("NEWS_API_KEY")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# 1️⃣ Fetch top 5 news headlines
def get_news():
    url = f"https://newsapi.org/v2/everything?q=technology+AI+cricket&language=en&sortBy=publishedAt&apiKey={news_api}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    if not articles:
        return "No fresh news found today!"
    headlines = [a["title"] for a in articles[:5]]  # only top 5 for testing
    return "\n".join(headlines)

# 2️⃣ Temporary summarization (no OpenAI)
def summarize_news(headlines_text):
    # Simply returns the first 5 headlines as "summary"
    return "\n".join(headlines_text.split("\n")[:5])

# 3️⃣ Send Telegram message
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

# 4️⃣ Daily news function
def daily_news():
    print("🗞️ Fetching news...")
    headlines = get_news()
    summary = summarize_news(headlines)
    message = f"🗞️ *Your Daily AI & Tech Digest*\n\n{summary}"
    send_telegram_message(message)
    print("✅ News sent!")

# Schedule task every day at 07:30
schedule.every().day.at("07:30").do(daily_news)

# ✅ Send immediately for testing
daily_news()

# Keep script running for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(30)
