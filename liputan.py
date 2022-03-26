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


def configureDate(day):
    return day.replace("Jan", "Januari").replace("Feb", "Februari").replace("Mar", "Maret").replace("Apr", "April").replace("Jun", "Juni").replace("Jul", "Juli").replace("Agu", "Agustus").replace("Sep", "Sepptember").replace("Nov", "November").replace("Des", "Desember").replace(',', '')


def rules(sub_soup, link):
    print("link : ", link)
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

    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {configureDate(date).strip()}")
    # print(f"Isi Berita: {content.strip()} ")
    print(" ")


def setUp(new) :
    link_new = new['href']
    html_link_new = requests.get(link_new).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)

link_main = main_news['href']
html_link_main = requests.get(link_main).text
soup_main = BeautifulSoup(html_link_main, 'lxml')
rules(soup_main, link_main)

for headline in headlines:
    setUp(headline)

for new in news:
    setUp(new)

for new_famous in news_famous:
    setUp(news_famous)

