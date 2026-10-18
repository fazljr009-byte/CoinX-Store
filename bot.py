import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в CoinX!\n\n"
        "🪙 Магазин Robux\n"
        "Выбери нужный пакет."
    )

@bot.message_handler(commands=["shop"])
def shop(message):
    bot.send_message(
        message.chat.id,
        "🛒 Магазин:\n\n"
        "💰 400 Robux — 100 ₽\n"
        "💰 800 Robux — 200 ₽\n"
        "💰 1700 Robux — 400 ₽"
    )

bot.infinity_polling()
