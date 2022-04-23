from bs4 import BeautifulSoup
import requests
import pandas as pd
from help import configureDate, currentDateTime, executeTime
import time

st = time.time()

url = "https://www.detik.com/"
html_text = requests.get(
    url).text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all(
    'article', class_="list-content__item column")
news = soup.find_all(['div', 'article'], class_="article_inview")
link_new_famous = soup.find('div', class_="box cb-mostpop").find(
    'a', class_="btn btn--default color-orange-light-1 btn--md")['href']
# news_c = soup.find_all('div', class_="article_inview")
# news_d = soup.find_all('article', class_="article_inview")


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


def kerangkaDetik(sub_soup, link, category):
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
        author = sub_soup.find(
            'div', class_="detail__author").text
    elif (sub_soup.find('div', class_="color-gray-light-1 font-xs")):  # 20Detik
        author = sub_soup.find(
            'div', class_="color-gray-light-1 font-xs").text
    elif (sub_soup.find('div', class_="ugc__block__name")):
        author = sub_soup.find('div', class_="ugc__block__name").a.text
    elif (sub_soup.find('span', class_="author")):  # detikHealth #wolipop
        author = sub_soup.find('span', class_="author").text
    elif(sub_soup.find_all('div', class_="column full body_text")):
        find_name = sub_soup.find_all('div', class_="column full body_text")
        for find in find_name:
            if("Penulis" in find.text):
                split_author = find.text.split('Editor')[0]
                author = split_author.split(":")[1]
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

    listItem = []
    listItem.append(title.strip())
    listItem.append(configureDate(date, 'detik').strip())
    listItem.append(author.strip())
    listItem.append(link.strip())
    listItem.append(category)
    listItem.append("detik")
    listItem.append(content.strip())
    items.append(listItem)


def setUp(new, category):
    if(category == "headline" or category == "popular"):
        if(category == 'headline'):
            category = "biasa"
        link_new = new.a['href']
    else:
        link_new = new['i-link']
        category = 'biasa'
    html_link_new = requests.get(link_new).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    kerangkaDetik(soup_new, link_new, category)


items = []

link_famous = link_new_famous
html_link_famous = requests.get(link_famous).text
soup_main = BeautifulSoup(html_link_famous, 'lxml')
famous = soup_main.find_all('article', class_="list-content__item")

for many_famous in famous:
    setUp(many_famous, 'popular')

for headline in headlines:
    setUp(headline, 'headline')

for new in news:
    setUp(new, 'i-link')

listDetik = pd.DataFrame(items, columns=[
                         'title', 'date', 'author', 'link', 'category', 'website', 'content'])
listDetik.drop_duplicates(subset="link", keep='last', inplace=True)

et = time.time()
elapsed_time_detik = et - st
row_detik = listDetik.shape[0]
column_detik = listDetik.shape[1]

listDetik.to_csv(f'data/berita/Detik({currentDateTime}).csv', index=False)
print(listDetik)

print('Execution time Detik.com:', elapsed_time_detik, 'seconds')
executeTime(elapsed_time_detik, row_detik, column_detik, "Detik.com")
