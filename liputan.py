from re import sub
from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.liputan6.com/"
# webbrowser.open(url)
html_text = requests.get(
    url).text
soup = BeautifulSoup(html_text, 'lxml')
main_news = soup.find('a', class_="ui--a headline--main__title-link")
headlines = soup.find_all(
    'a', class_="ui--a headline--bottom-slider__link")
news = soup.find_all(
    'a', class_="ui--a articles--iridescent-list--text-item__title-link")
news_famous = soup.find_all('h5', class_="article-snippet--numbered__title")
# print(news_famous)


def rules(sub_soup, link):
    if (sub_soup.find(
            'h1', class_="read-page--header--title entry-title")):
        title = sub_soup.find(
            'h1', class_="read-page--header--title entry-title").text

        date = sub_soup.find(
            'time', class_="read-page--header--author__datetime updated").text.replace(',', '')

        author = sub_soup.find('span',
                               class_="read-page--header--author__name fn").text

        print(f"Link Berita : {link.strip()}")
        print(f"Judul Berita : {title.strip()}")
        print(f"Author : {author.strip()}")
        print(f"Date : {date.strip()}")
        print(" ")


link_main = main_news['href']
html_link_main = requests.get(link_main).text
soup_main = BeautifulSoup(html_link_main, 'lxml')
rules(soup_main, link_main)

for headline in headlines:
    link_headline = headline['href']
    html_link_headline = requests.get(link_headline).text
    soup_headline = BeautifulSoup(html_link_headline, 'lxml')
    rules(soup_headline, link_headline)

for new in news:
    link_new = new['href']
    html_link_new = requests.get(link_new).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)

for new_famous in news_famous:
    link_new_famous = new_famous.a['href']
    html_link_new_famous = requests.get(link_new_famous).text
    soup_new_famous = BeautifulSoup(html_link_new_famous, 'lxml')
    rules(soup_new_famous, link_new_famous)