import re
import wget
import requests
from bs4 import BeautifulSoup

# Sending a request and receiving content
page_url = 'https://www.7-zip.org/'
page_html = requests.get(page_url)
page_soup = BeautifulSoup(page_html.content, 'html.parser')

# Find download link with regular expression
regex = r"a/[\s\S]+x64\.exe"
for a in page_soup.findAll('a', {'href': re.compile(regex)}):
    download_file = page_url + a['href']

# Downloading file
wget.download(download_file)
