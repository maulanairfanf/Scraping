from traceback import print_tb
from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    'https://www.detik.com/').text
soup = BeautifulSoup(html_text, 'lxml')
news = soup.find_all(
    'article', class_="list-content__item column")
for new in news:
    data = []
    link = new.a["href"]
    html_links = requests.get(link).text
    sub_soup = BeautifulSoup(html_links, 'lxml')

    title = sub_soup.find('h1', class_="detail__title").text
    author = sub_soup.find('div', class_="detail__author").text
    date = sub_soup.find('div', class_="detail__date").text
    body = sub_soup.find(
        "div", class_="detail__body-text itp_bodycontent")
    contents = body.find_all('p')
    for content in contents:
        data.append(content.text)

    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {date.strip()}")
    print("Isi Berita :", data)

    print("")
