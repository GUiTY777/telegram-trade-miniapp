import telebot
from telebot import types
import time
import os

TOKEN = os.getenv("BOT_TOKEN")  # Безопасно: читаем из переменной окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="👉 Открыть трейд", url="https://your-domain.up.railway.app")
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы открыть трейд:", reply_markup=markup)

print("Бот запущен")
while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print("Ошибка в боте:", e)
        time.sleep(5)