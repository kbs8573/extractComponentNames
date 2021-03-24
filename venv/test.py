from bs4 import BeautifulSoup
import requests

html = requests.get('https://stackoverflow.com/jobs?q=python').text
print(html)
