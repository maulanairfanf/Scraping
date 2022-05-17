from ast import Try
from distutils.log import error
from bs4 import BeautifulSoup
import requests
import pandas as pd
from help import configureDate, currentDateTime, executeTime
import time

st = time.time()

url = "https://www.liputan6.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"}

html_text = requests.get(
    url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
for data in soup(['style', 'script']):
    data.decompose()
main_news = soup.find('a', class_="ui--a headline--main__title-link")
headlines = soup.find_all(
    'a', class_="ui--a headline--bottom-slider__link")
news = soup.find_all(
    'a', class_="ui--a articles--iridescent-list--text-item__title-link")
news_famous = soup.find_all('h5', class_="article-snippet--numbered__title")


def kerangkaLiputan(sub_soup, link, category):
    # print("link : ", link)
    if (sub_soup.find(
            'h1', class_="read-page--header--title entry-title")):
        title = sub_soup.find(
            'h1', class_="read-page--header--title entry-title").text
    elif(sub_soup.find('h1', class_="read-page--photo-tag--header__title")):
        title = sub_soup.find(
            "h1", class_="read-page--photo-tag--header__title").text
    else:
        title = "Kerangka belum dikenali"

    if (sub_soup.find(
            'time', class_="read-page--header--author__datetime updated")):
        date = sub_soup.find(
            'time', class_="read-page--header--author__datetime updated").text
    elif (sub_soup.find(
            'time', class_="read-page--photo-tag--header__datetime updated")):
        date = sub_soup.find(
            'time', class_="read-page--photo-tag--header__datetime updated").text
    else:
        date = "Kerangka belum dikenali"

    if (sub_soup.find('span', class_="read-page--header--author__name fn")):
        author = sub_soup.find(
            'span', class_="read-page--header--author__name fn").text
    elif (sub_soup.find('div', class_="read-page--photo-tag--header__credits-user")):
        author = sub_soup.find(
            'div', class_="read-page--photo-tag--header__credits-user").text
    else:
        author = "Kerangka belum dikenali"

    if (sub_soup.find_all(
            'div', class_="article-content-body__item-content")):
        contents = sub_soup.find_all(
            'div', class_="article-content-body__item-content")

        arr_content = []

        for data_content in contents:
            if(data_content.find('div', class_="baca-juga-collections")):
                data_content.find(
                    'div', class_="baca-juga-collections").decompose()
            if(data_content.find('div', class_="baca-juga")):
                data_content.find('div', class_="baca-juga").decompose()
            if(data_content.find('strong')):
                get_char = data_content.find('strong').text
                if(get_char[0] == "*"):
                    data_content.find('strong').decompose()
            arr_data = []
            for data in data_content.find_all('p'):
                arr_data.append(data.text)
            merge_content = "".join(arr_data)
            arr_content.append(merge_content)

        content = "".join(arr_content)
    elif (sub_soup.find("div", class_="read-page--photo-tag--header__content")):
        content = sub_soup.find(
            "div", class_="read-page--photo-tag--header__content").text
    else:
        content = "Kerangka belum dikenali"

    listItem = []
    listItem.append(title.strip())
    listItem.append(configureDate(date, 'liputan').strip())
    listItem.append(author.strip())
    listItem.append(link.strip())
    listItem.append(category)
    listItem.append("liputan6")
    listItem.append(content.strip())
    items.append(listItem)


def setUp(new, category):
    if(category == 'popular'):
        link_new = new.a['href']
    else:
        link_new = new['href']
    
    try:
        html_link_new = requests.get(link_new, headers=headers).text
        soup_new = BeautifulSoup(html_link_new, 'lxml')
        kerangkaLiputan(soup_new, link_new, category)
    except:
        print("liputan error")


items = []

link_main = main_news['href']
html_link_main = requests.get(link_main).text
soup_main = BeautifulSoup(html_link_main, 'lxml')
kerangkaLiputan(soup_main, link_main, 'biasa')

for headline in headlines:
    setUp(headline, 'biasa')

for new in news:
    setUp(new, 'biasa')

for new_famous in news_famous:
    setUp(new_famous, 'popular')

listLiputan = pd.DataFrame(items, columns=[
                           'title', 'date', 'author', 'link', 'category', 'website', 'content'])
listLiputan.drop_duplicates(subset="link", keep='last', inplace=True)

et = time.time()
elapsed_time_liputan = et - st
row_liputan = listLiputan.shape[0]
column_liputan = listLiputan.shape[1]

# listLiputan.to_excel(f'data/berita/Liputan({currentDateTime}).xlsx', index=False)
print(listLiputan)

print('Execution time Liputan6.com :', elapsed_time_liputan, 'seconds')
executeTime(elapsed_time_liputan, row_liputan, column_liputan, "Liputan6.com")
