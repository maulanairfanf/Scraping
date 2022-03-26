from bs4 import BeautifulSoup
import requests
# import webbrowser

url = "https://www.tribunnews.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
html_text = requests.get(
    url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all('a', class_="ovh tsa2 pos_rel hladvthumb")
news = soup.find_all('a', class_="f20 ln24 fbo txt-oev-2")
news_famous = soup.find_all('a', class_="fbo2 f15 txt-oev-3")
news_stories = soup.find_all('a', class_="fbo2 f14 al txt-oev-3")


def configureDate(day):
    return day.split(', ')[-1]


def rules(sub_soup, link):
    # print("link : ", link)

    # title
    if (sub_soup.find('h1', class_="f50 black2 f400 crimson")):
        title = sub_soup.find('h1', class_="f50 black2 f400 crimson").text
    elif (sub_soup.find('h1', class_="crimson")):
        title = sub_soup.find('h1', class_="crimson").text
    else:
        title = 'Kerangka belum dikenali'

    # time
    if(sub_soup.find('time')):
        date = sub_soup.find('time').text
    else:
        author = "Kerangka belum dikenali"

    # author
    if (sub_soup.find('div', id="penulis")):
        author = sub_soup.find('div', id="penulis").a.text
    else:
        author = "Kerangka belum dikenali"

    # content
    if(sub_soup.find('div', class_="side-article txt-article multi-fontsize")):
        content = sub_soup.find(
            'div', class_="side-article txt-article multi-fontsize")
        if(content.find('p', class_="baca")):
            reads = content.find_all('p', class_="baca")
            for read in reads:
                read.decompose()

        if(content.find('div', class_="_popIn_recommend_art_title")):
            recommends = content.find_all(
                'div', class_="_popIn_recommend_art_title")
            for recommend in recommends:
                recommend.decompose()

        arr_content = []
        for data_content in content.find_all("p"):
            arr_content.append(data_content.text)
        content = "".join(arr_content)

    else:
        content = "Kerangka belum dikenali"

    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {configureDate(date).strip()}")
    print(f"Isi Berita : {content.strip()}")
    print("")


def setUp(new):
    link_new = new['href']
    html_link_new = requests.get(link_new, headers=headers).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)


for headline in headlines:
    setUp(headline)

for new in news:
    setUp(new)

for new_famous in news_famous:
    setUp(new_famous)

for new_story in news_stories:
    setUp(new_story)
