# Импорт библиотек
import re  # Для регулярных выражений
import requests  # Для отправки запроса на сайт
from bs4 import BeautifulSoup  # Для парсинга контента
import wget  # Для скачивания файла

main_page_url = 'https://notepad-plus-plus.org'
main_page_html = requests.get(main_page_url)
main_page_soup = BeautifulSoup(main_page_html.content, 'html.parser')

regex_first = r"(/downloads/)[\s\S]"
for a in main_page_soup.findAll('a', {'href': re.compile(regex_first)}):
    download_page_url = main_page_url + a['href']

download_page_html = requests.get(download_page_url)
download_page_soup = BeautifulSoup(download_page_html.content, 'html.parser')

regex_second = r"[\s\S]Installer\.x64\.exe"
for a in download_page_soup.findAll('a', {'href': re.compile(regex_second)}):
    download_file = a['href']

# Костыль, удаление .sig
download_file = download_file.replace(".sig", "")

# Скачивание файла
wget.download(download_file)
