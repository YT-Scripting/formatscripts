# formatscripts

# 📌 Telegram Bot - Setup Guide

This repository contains a simple Telegram bot script. Follow the steps below to get your bot up and running.

---

## 🚀 Getting Started

### 1️⃣ Create a Telegram Bot & Get a Token
1. Open Telegram and search for `@BotFather`.
2. Start a chat with `@BotFather` and send the command:
   ```
   /newbot
   ```
3. Follow the instructions to set up your bot.
4. After completion, `@BotFather` will give you a **bot token**.
5. Copy the token for later use.

---

### 2️⃣ Install Dependencies
Make sure you have **Python 3** installed, then install the required libraries:
```bash
pip install pyTelegramBotAPI
```

---

### 3️⃣ Configure the Token
1. Open `bot.py` 
2. Find this line:
   ```python
   application = Application.builder().token("YOUR TOKEN").build()
   ```
3. Replace `YOUR TOKEN` with the token from `@BotFather`.

---

### 4️⃣ Run the Bot
To start your bot, run:
```bash
python bot.py
```

---

### 🛠️ Features
- Simple and easy to set up.
- Can be expanded with more functionalities.

---

### ❓ Troubleshooting
If you encounter issues:
- **Check your token**: Ensure there are no extra spaces or missing characters.
- **Check dependencies**: Run `pip install --upgrade pyTelegramBotAPI`.
- **Ensure Python is installed**: Run `python --version` to check.

---

