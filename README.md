# Daily News Telegram Bot 🗞️

A lightweight, automated Python-based Telegram bot that fetches top daily news headlines regarding **Technology, AI, and Cricket** and broadcasts them to a designated Telegram channel/chat.

## 🚀 Features
- **API Integration**: Fetches real-time headlines using the [NewsAPI](https://newsapi.org/).
- **Automated Scheduling**: Automatically runs every day at **07:30 AM** using Python's `schedule` package.
- **Instant Telegram Delivery**: Sends formatted digests directly to your Telegram chat using the Telegram Bot API.
- **Environment Configuration**: Safe credential handling via `.env` files.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**:
  - `requests` (for HTTP API requests)
  - `python-dotenv` (for reading configurations)
  - `schedule` (for task scheduling)

## 📦 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bharathkumar7733/daily-news-telegram-bot.git
   cd daily-news-telegram-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install requests python-dotenv schedule
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add the following keys:
   ```env
   NEWS_API_KEY=your_news_api_key_here
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```
   *Note: On launch, the bot sends an immediate digest for testing before entering the daily scheduling loop.*

---
Developed by [bharathkumar7733](https://github.com/bharathkumar7733)
