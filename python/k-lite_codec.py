import re
import wget
import requests
from bs4 import BeautifulSoup

# Sending a request and receiving content
page_url = 'https://codecguide.com/download_k-lite_codec_pack_mega.htm'
page_html = requests.get(page_url)
page_soup = BeautifulSoup(page_html.content, 'html.parser')

# Find download link with regular expression
regex = r"files3\.codecguide\.com/[\s\S]+\.exe"
for a in page_soup.findAll('a', {'href': re.compile(regex)}):
    download_file = a['href']

# Downloading file
wget.download(download_file)
