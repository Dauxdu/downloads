# Импорт библиотек
import re  # Для регулярных выражений
import requests  # Для отправки запроса на сайт
from bs4 import BeautifulSoup  # Для парсинга контента
import wget  # Для скачивания файла

page_url = 'https://codecguide.com/download_k-lite_codec_pack_mega.htm'
page_html = requests.get(page_url)
page_soup = BeautifulSoup(page_html.content, 'html.parser')


regex = r"files3\.codecguide\.com/[\s\S]+\.exe"
for a in page_soup.findAll('a', {'href': re.compile(regex)}):
    download_file = a['href']

# Скачивание файла
wget.download(download_file)
