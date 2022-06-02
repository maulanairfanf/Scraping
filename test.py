import time
from bs4 import BeautifulSoup
import requests
import json

response_API = requests.get(
    'https://indonesia-news-api.herokuapp.com/website=liputan?limit=100')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
if(response_API.status_code == 200):
    parse_json = json.loads(response_API.text)
    data = parse_json['result']

    st = time.time()

    for _data in data:
        url = _data['link']
        title_api = _data['title']
        html_text = requests.get(url, verify=None, timeout=30,headers=headers).text
        soup = BeautifulSoup(html_text, 'lxml')
        print("succes")
else:
    print(response_API.status_code)