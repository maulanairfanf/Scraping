from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    'https://www.detik.com/').text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all(
    'article', class_="list-content__item column")
news = soup.find_all('div', class_="article_inview")



# for headline in headlines:
#     data = []
#     link = headline.a["href"]
#     html_links = requests.get(link).text
#     soup_headlines = BeautifulSoup(html_links, 'lxml')

#     if(soup_headlines.find('h1', class_="detail__title")):
#         title = soup_headlines.find('h1', class_="detail__title").text
#     else:
#         title = soup_headlines.find('h1', class_="mt5").text

#     if (soup_headlines.find('div', class_="detail__author")):
#         author = soup_headlines.find('div', class_="detail__author").text
#     elif (soup_headlines.find('div', class_="color-gray-light-1 font-xs")):
#         author = soup_headlines.find('div', class_="color-gray-light-1 font-xs").text
#     else:
#         authro = soup_headlines.find('div', class_="valign").text

#     if(soup_headlines.find('div', class_="detail__date")):
#         date = soup_headlines.find('div', class_="detail__date").text
#     else:
#         date = soup_headlines.find('div', class_="date").text

#     # body = soup_headlines.find(
#     #     "div", class_="detail__body-text itp_bodycontent")
#     # if (body.find_all('p')):
#     #     contents = body.find_all('p').text
#     #     for content in contents:
#     #         data.append(content.text)

#     print(f"Link Berita : {link.strip()}")
#     print(f"Judul Berita : {title.strip()}")
#     print(f"Author : {author.strip()}")
#     print(f"Date : {date.strip()}")
# print("Isi Berita :", data)

# print("")

for new in news:
    link_news = new["i-link"]
    html_links_news = requests.get(link_news).text
    soup_news = BeautifulSoup(html_links_news, 'lxml')

    if(soup_news.find('h1', class_="detail__title")):
        title = soup_news.find('h1', class_="detail__title").text
    else:
        title = soup_news.find('h1', class_="mt5").text

    if (soup_news.find('div', class_="detail__author")):
        author = soup_news.find('div', class_="detail__author").text
    elif (soup_news.find('div', class_="color-gray-light-1 font-xs")):
        author = soup_news.find(
            'div', class_="color-gray-light-1 font-xs").text
    else:
        authro = soup_news.find('div', class_="valign").text

    if(soup_news.find('div', class_="detail__date")):
        date = soup_news.find('div', class_="detail__date").text
    else:
        date = soup_news.find('div', class_="date").text

    print(f"Link Berita : {link_news.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {date.strip()}")
