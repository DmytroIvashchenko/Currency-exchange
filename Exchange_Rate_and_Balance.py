import json

import requests  # Модуль для обробки URL
from bs4 import BeautifulSoup  # Модуль для роботи с HTML

DOLLAR_UAH = 'https://www.google.com/search?q=доллар+к+гриве&sxsrf=ALiCzsYgLKVR0f8N410Ftc3On9rL0oJL1Q%3A1655289806250&ei=zrepYqbrDpTRqwGbkK24Bw&ved=0ahUKEwimipuHo6_4AhWU6CoKHRtIC3cQ4dUDCA0&uact=5&oq=доллар+к+гриве&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEIcCEBQyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BAgAEEc6BAgjECc6BQgAEIAEOgkIIxAnEEYQggI6CAgAEIAEELEDOgsIABCABBCxAxCDAToOCAAQgAQQsQMQgwEQyQM6DQgAEIAEEIcCELEDEBRKBAhBGABKBAhGGABQ5AZYlxlg2RpoAHACeACAAYoBiAGpCJIBAzQuNpgBAKABAcgBCMABAQ&sclient=gws-wiz'
UAH_DOLLAR = 'https://www.google.com/search?q=гривна+к+доллару&sxsrf=ALiCzsbvWKSb5q2OcyIUE-GrWwxumJK56g%3A1655289822407&ei=3repYsihGKzLrgTBsqqoAQ&ved=0ahUKEwjIiPWOo6_4AhWspYsKHUGZChUQ4dUDCA0&uact=5&oq=гривна+к+доллару&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoICC4QgAQQ1AI6DgguEIAEELEDEMcBEKMCOhEILhCABBCxAxCDARDHARDRAzoICAAQsQMQgwE6DwgAEIAEEIcCEBQQRhD_AToJCC4QgAQQChABOgQIABAKOgkIABCABBAKEAE6CwgAEIAEEAoQARAqOgcIABCABBAKOg8ILhCABBDHARCvARAKEAE6CQgAEIAEEAoQKjoLCC4QgAQQxwEQrwE6BwgjEOoCECc6BAgjECc6BwgAELEDEEM6BAgAEEM6CwguEIAEELEDEIMBOg0IABCABBCHAhCxAxAUOggILhCABBCxAzoMCAAQsQMQQxBGEIICOggIABCABBCxAzoFCAAQywE6CggAEIAEEMkDEAo6BAgAEB46CggAEIAEEIcCEBQ6CwgAEIAEELEDEMkDOgwIABCxAxAKEEYQggJKBAhBGABKBAhGGABQAFjySmCpTWgHcAF4AIABpAGIAdETkgEEOS4xNJgBAKABAbABCsABAQ&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70'
}


def get_currency_dollar_uah():
    # Парсимо всю сторінку
    full_page_dollar_uah = requests.get(DOLLAR_UAH, headers=headers)
    # Розбираємо через BeautifulSoup
    soup = BeautifulSoup(full_page_dollar_uah.content, 'html.parser')
    # Отримуємо необхідне для нас значення та повертаємо його
    result = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return float(result[0].text.replace(',', '.'))


def get_currency_uah_dollar():
    # Парсимо всю сторінку
    full_page_dollar_uah = requests.get(UAH_DOLLAR, headers=headers)
    # Розбираємо через BeautifulSoup
    soup = BeautifulSoup(full_page_dollar_uah.content, 'html.parser')
    # Отримуємо необхідне для нас значення та повертаємо його
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 3})
    return float(convert[0].text.replace(',', '.'))


def get_balance():
    with open('balance.json') as f:
        return json.loads(f.read())


def save_balance(balance):
    with open('balance.json', 'w') as f:
        f.write(json.dumps(balance))

