from bs4 import BeautifulSoup
import requests
import pandas as pd
from sqlalchemy import false
from help import configureDate, currentDateTime, executeTime
import time

st = time.time()

url = "https://www.tribunnews.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"}
html_text = requests.get(
    url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
for data in soup(['style', 'script']):
    data.decompose()
headlines = soup.find_all('a', class_="ovh tsa2 pos_rel hladvthumb")
news = soup.find_all('a', class_="f20 ln24 fbo txt-oev-2")
news_famous = soup.find_all('a', class_="fbo2 f15 txt-oev-3")
news_stories = soup.find_all('a', class_="fbo2 f14 al txt-oev-3")


def kerangkaTribun(sub_soup, link, category):
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
        date = "Kerangka belum dikenali"

    # author
    if (sub_soup.find('div', id="penulis")):
        author = sub_soup.find('div', id="penulis").a.text
    elif("Penulis" not in sub_soup):
        author = "Author tidak dipublikasikan"
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

    listItem = []
    listItem.append(title.strip())
    listItem.append(configureDate(date, 'tribun').strip())
    listItem.append(author.strip())
    listItem.append(link.strip())
    listItem.append(category)
    listItem.append("tribunnews")
    listItem.append(content.strip())
    items.append(listItem)


def setUp(new, category):
    link_new = new['href']
    html_link_new = requests.get(link_new, headers=headers).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    kerangkaTribun(soup_new, link_new, category)


items = []

for headline in headlines:
    setUp(headline, 'biasa')

for new in news:
    setUp(new, 'biasa')

for new_story in news_stories:
    setUp(new_story, 'biasa')

for new_famous in news_famous:
    setUp(new_famous, 'popular')

listTribun = pd.DataFrame(items, columns=[
                          'title', 'date', 'author', 'link', 'category', 'website', 'content'])
listTribun.drop_duplicates(subset="link", keep='last', inplace=True)

et = time.time()
elapsed_time_tribun = et - st
row_tribun = listTribun.shape[0]
column_tribun = listTribun.shape[1]

# listTribun.to_excel(f'data/berita/Tribun({currentDateTime}).xlsx', index=False)
print(listTribun)

print('Execution time Tribunnews.com :', elapsed_time_tribun, 'seconds')
executeTime(elapsed_time_tribun, row_tribun, column_tribun, "Tribunnews.com")
