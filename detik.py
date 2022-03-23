import re
from bs4 import BeautifulSoup
import requests
import webbrowser


url = "https://www.detik.com/"
# webbrowser.open(url)
html_text = requests.get(
    url).text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all(
    'article', class_="list-content__item column")
news = soup.find_all(['div', 'article'], class_="article_inview")
# news_c = soup.find_all('div', class_="article_inview")
# news_d = soup.find_all('article', class_="article_inview")


def configureDate(day):
    return day.split(', ')[-1].replace("Jan", "Januari").replace("Feb", "Februari").replace("Mar", "Maret").replace("Apr", "April").replace("Jun", "Juni").replace("Jul", "Juli").replace("Agu", "Agustus").replace("Sep", "Sepptember").replace("Nov", "November").replace("Des", "Desember")


def configureAuthor(site):
    return site.split('-')[0]


def rules(sub_soup, link):
    # title
    if(sub_soup.find('h1', class_="detail__title")):
        title = sub_soup.find('h1', class_="detail__title").text
    elif (sub_soup.find('h1', class_="mt5")):
        title = sub_soup.find('h1', class_="mt5").text
    else:
        title = sub_soup.find('h1').text

    # Author
    # detikOto #sepakbola #detiknews #detikFinance #detikInet
    if (sub_soup.find('div', class_="detail__author")):
        # sub_soup.find('span', class_="detail__label").decompose()
        author = sub_soup.find(
            'div', class_="detail__author").text
    elif (sub_soup.find('div', class_="color-gray-light-1 font-xs")):  # 20Detik
        author = sub_soup.find(
            'div', class_="color-gray-light-1 font-xs").text
    elif (sub_soup.find('div', class_="ugc__block__name")):
        author = sub_soup.find('div', class_="ugc__block__name").a.text
    elif (sub_soup.find('span', class_="author")):  # detikHealth #wolipop
        author = sub_soup.find('span', class_="author").text
    else:
        author = "Kerangka berbeda"

    # date
    if(sub_soup.find('div', class_="detail__date")):
        date = sub_soup.find(
            'div', class_="detail__date").text
    elif (sub_soup.find(class_="date")):
        date = sub_soup.find(class_="date").text
    elif(sub_soup.find('div', class_="caption")):
        date = sub_soup.find('div', class_="caption").span.text
    else:
        date = "Kerangka berbeda"

    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {configureAuthor(author).strip()}")
    print(f"Date : {configureDate(date).strip()}")
    print(" ")


for headline in headlines:
    link_headlines = headline.a["href"]
    html_links = requests.get(link_headlines).text
    soup_headlines = BeautifulSoup(html_links, 'lxml')
    rules(soup_headlines, link_headlines)

for new in news:
    link_news = new["i-link"]
    html_links_news = requests.get(link_news).text
    soup_news = BeautifulSoup(html_links_news, 'lxml')
    rules(soup_news, link_news)

# for new_c in news_c:
#     link_news_c = new_c["i-link"]
#     html_links_news_c = requests.get(link_news_c).text
#     soup_news_c = BeautifulSoup(html_links_news_c, 'lxml')
#     rules(soup_news_c, link_news_c)

# for new_d in news_d:
#     link_news_d = new_d["i-link"]
#     html_links_news_d = requests.get(link_news_d).text
#     soup_news_d = BeautifulSoup(html_links_news_d, 'lxml')
#     rules(soup_news_d, link_news_d)
