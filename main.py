import requests
from bs4 import BeautifulSoup
import hashlib
import time

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

# Запуск бота

URL = 'https://nh-c1fe.onrender.com'  # Замените URL на адрес нужной веб-страницы
current_hash = None

def fetch_content(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.content, 'html.parser')
       return soup.get_text()  # Получаем текст страницы для сравнения
