import requests
from bs4 import BeautifulSoup
import re
import json

# URL веб-сторінки, яку треба обробити
url = "https://example.com"  # Заміни на фактичну адресу

# Завантаження веб-сторінки
response = requests.get(url)
content = response.text

# Парсинг HTML вмісту
soup = BeautifulSoup(content, 'html.parser')

# 1. Знаходження всіх URL-адрес з гіперпосилань і запис у файл
links = [a['href'] for a in soup.find_all('a', href=True)]
with open("urls.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

# 2. Знаходження всіх email-адрес
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Підрахунок кількості адрес з доменами gmail.com та ukr.net
domains_count = {
    "gmail.com": sum(1 for email in emails if email.endswith("@gmail.com")),
    "ukr.net": sum(1 for email in emails if email.endswith("@ukr.net"))
}

# Запис результатів у файл mail.json
with open("mail.json", "w") as json_file:
    json.dump(domains_count, json_file, indent=4)

print("Програма успішно виконана. URL-адреси збережено в urls.txt, а статистику email-адрес у mail.json.")
