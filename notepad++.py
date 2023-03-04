import re
import wget
import requests
from bs4 import BeautifulSoup

# Sending a request and receiving content
main_page_url = 'https://notepad-plus-plus.org'
main_page_html = requests.get(main_page_url)
main_page_soup = BeautifulSoup(main_page_html.content, 'html.parser')

# Find download page with regular expression
regex_first = r"(/downloads/)[\s\S]"
for a in main_page_soup.findAll('a', {'href': re.compile(regex_first)}):
    download_page_url = main_page_url + a['href']

# Sending a request and receiving content
download_page_html = requests.get(download_page_url)
download_page_soup = BeautifulSoup(download_page_html.content, 'html.parser')

# Find download link with regular expression
regex_second = r"[\s\S]Installer\.x64\.exe"
for a in download_page_soup.findAll('a', {'href': re.compile(regex_second)}):
    download_file = a['href']

# Crutch to remove the .sig
download_file = download_file.replace(".sig", "")

# Downloading file
wget.download(download_file)
