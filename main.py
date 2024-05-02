import requests
from bs4 import BeautifulSoup
import hashlib
import time
import telebot

# Вставте сюди ваш токен бота
BOT_TOKEN = '6937303308:AAEMrGtZRjgGpixbhSlxZZ_d21FRS27a8wc'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, 'Привіт!')

# Запуск бота

URL = 'https://90186dac-ba2a-4777-adfa-c2b0c007e95d-00-2fjyuxkthu7te.picard.replit.dev/'  # Замените URL на адрес нужной веб-страницы
current_hash = None

def fetch_content(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.content, 'html.parser')
       return soup.get_text()  # Получаем текст страницы для сравнения

while True:
       print("Проверка на изменения...")
       content = fetch_content(URL)
       new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

       if current_hash is None:
           current_hash = new_hash
           print("Мониторинг начат...")
       elif new_hash != current_hash:
           print("Обнаружены изменения!")
           current_hash = new_hash
           # Здесь можно добавить отправку уведомлений или другие действия

bot.polling()
