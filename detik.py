from re import sub
from bs4 import BeautifulSoup
import requests
import webbrowser


url = "https://www.detik.com/"
webbrowser.open(url)
html_text = requests.get(
    url).text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all(
    'article', class_="list-content__item column")
news_c = soup.find_all('div', class_="article_inview")
news_d = soup.find_all('article', class_="article_inview")


def rules(sub_soup, link):

    if(sub_soup.find('h1', class_="detail__title")):
        title = sub_soup.find('h1', class_="detail__title").text
    elif (sub_soup.find('h1', class_="mt5")):
        title = sub_soup.find('h1', class_="mt5").text
    else:
        title = sub_soup.find('h1').text

    if (sub_soup.find('div', class_="detail__author")):
        author = sub_soup.find('div', class_="detail__author").text
    elif (sub_soup.find('div', class_="color-gray-light-1 font-xs")):
        author = sub_soup.find(
            'div', class_="color-gray-light-1 font-xs").text
    elif (sub_soup.find('div', class_="valign")):
        author = sub_soup.find('div', class_="valign").text
    else:
        author = sub_soup.find('span', class_="author").text

    if(sub_soup.find('div', class_="detail__date")):
        date = sub_soup.find('div', class_="detail__date").text
    else:
        date = sub_soup.find(class_="date").text

    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {date.strip()}")


for headline in headlines:
    data = []
    link_headlines = headline.a["href"]
    html_links = requests.get(link_headlines).text
    soup_headlines = BeautifulSoup(html_links, 'lxml')

    rules(soup_headlines, link_headlines)

print("==================================================")

for new_c in news_c:
    link_news_c = new_c["i-link"]
    html_links_news_c = requests.get(link_news_c).text
    soup_news_c = BeautifulSoup(html_links_news_c, 'lxml')

    rules(soup_news_c, link_news_c)

print("==================================================")


for new_d in news_d:
    link_news_d = new_d["i-link"]
    html_links_news_d = requests.get(link_news_d).text
    soup_news_d = BeautifulSoup(html_links_news_d, 'lxml')

    rules(soup_news_d, link_news_d)
