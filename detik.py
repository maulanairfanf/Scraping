import re
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.detik.com/"
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


def loopContent_P(contents):
    arr_content = []
    for data_content in contents.find_all("p"):
        arr_content.append(data_content.text)
    content = "".join(arr_content)
    return content


def loopContent(contents):
    arr_content = []
    for data_content in contents:
        arr_content.append(data_content.text)
    content = "".join(arr_content)
    return content


def decomposeNav(contents):
    if(contents.find('div', class_="mp-nav mp-nav-ap mp-nav-bot ap-update")):
        contents.find(
            'div', class_="mp-nav mp-nav-ap mp-nav-bot ap-update").decompose()
    if(contents.find('div', class_="detail__long-nav")):
        contents.find('div', class_="detail__long-nav").decompose()
    return contents


def rules(sub_soup, link):
    # print("Link : ", link)
    # title
    if(sub_soup.find('h1', class_="detail__title")):
        title = sub_soup.find('h1', class_="detail__title").text
    elif (sub_soup.find('h1', class_="mt5")):
        title = sub_soup.find('h1', class_="mt5").text
    elif (sub_soup.find('h1')):
        title = sub_soup.find('h1').text
    else:
        title = "Kerangka belum dikenali"

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
        author = "Kerangka belum dikenali"

    # date
    if(sub_soup.find('div', class_="detail__date")):
        date = sub_soup.find(
            'div', class_="detail__date").text
    elif (sub_soup.find(class_="date")):
        date = sub_soup.find(class_="date").text
    elif(sub_soup.find('div', class_="caption")):
        date = sub_soup.find('div', class_="caption").span.text
    else:
        date = "Kerangka belum dikenali"

    # content
    if(sub_soup.find('div', class_="detail__body-text itp_bodycontent")):
        contents = sub_soup.find(
            'div', class_="detail__body-text itp_bodycontent")
        get_texts = contents.find_all('strong')
        for get_text in get_texts:
            if(get_text.text.split(':')[0] == "Baca juga"):
                get_text.decompose()
        decomposeNav(contents)
        content = loopContent_P(contents)
        # print(content)
    elif(sub_soup.find('div', class_="itp_bodycontent read__content pull-left")):
        contents = sub_soup.find(
            'div', class_="itp_bodycontent read__content pull-left")
        content = loopContent_P(contents)
        # print(content)
    elif(sub_soup.find('div', class_="itp_bodycontent detail__body-text")):
        contents = sub_soup.find(
            'div', class_="itp_bodycontent detail__body-text")
        content = loopContent_P(contents)
        # print(content)
    elif(sub_soup.find('article', class_="detail")):  # content 2 body
        content_1 = sub_soup.find(
            'div', class_="detail__body-text").text.replace("\n", "")
        content_2 = sub_soup.find('figcaption', class_="mgt-16").text
        arr_content = []
        arr_content.append(content_1)
        arr_content.append(content_2)
        content = "".join(arr_content)
        # print(content)
    elif(sub_soup.find('div', class_="detail__body-text")):
        content = sub_soup.find('div', class_="detail__body-text").text
        # print(content)
    elif(sub_soup.find('div', class_="column full body_text")):  # detik intermeso
        contents = sub_soup.find_all('div', class_="column full body_text")
        arr_content = []
        for data_content in contents:
            arr_content.append(loopContent_P(data_content))
        content = "".join(arr_content)
        # print(content) #hilangin penulis
    elif(sub_soup.find('div', class_="itp_bodycontent detail_text group")):
        contents = sub_soup.find(
            'div', class_="itp_bodycontent detail_text group")
        decomposeNav(contents)
        content = loopContent_P(contents)
        # print(content)
    elif(sub_soup.find('div', class_="itp_bodycontent detail_text")):
        contents = sub_soup.find('div', class_="itp_bodycontent detail_text")
        decomposeNav(contents)
        content = loopContent_P(contents)
        # print(content)
    elif(sub_soup.find('p', class_="text_par mt20")):
        content = sub_soup.find('p', class_="text_par mt20").text
    elif(sub_soup.find('div', class_="detail_text group detail_text2")):
        content = sub_soup.find(
            'div', class_="detail_text group detail_text2").text
    elif(sub_soup.find('div', class_="newstag newstag2")):
        content = sub_soup.find('div', class_="newstag newstag2").text
    else:
        content = "Kerangka belum dikenali"

    list_author.append(author.strip())
    list_title.append(title.strip())
    list_date.append(configureDate(date).strip())
    list_link.append(link.strip())
    list_content.append(content.strip())

    # print(f"Link Berita : {link.strip()}")
    # print(f"Judul Berita : {title.strip()}")
    # print(f"Author : {configureAuthor(author).strip()}")
    # print(f"Date : {configureDate(date).strip()}")
    # print(f"Isi Berita : {content.strip()}")
    # print(" ")



def setUp(new, link):
    if(link == "headline"):
        link_new = new.a['href']
    else:
        link_new = new['i-link']
    html_link_new = requests.get(link_new).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)

list_author = []
list_title = []
list_date = []
list_link = []
list_content = []

for headline in headlines:
    setUp(headline, 'headline')

for new in news:
    setUp(new, 'i-link')

# for new_c in news_c:
#     setUp(new_c)

# for new_d in news_d:
#     setUp(new_c)

items = {'Author' : list_author ,'Judul Berita' : list_title, 'Date' : list_date, "Link" : list_link, "Content" : list_content}
df = pd.DataFrame(items)
df.to_csv("detik.csv")