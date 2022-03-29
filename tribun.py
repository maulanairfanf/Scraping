from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import json

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


def rules(sub_soup, link, category):
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
    if (sub_soup.find('div', id=["penulis", "editor"])):
        author = sub_soup.find('div', id=["penulis", "editor"]).a.text
    # elif (sub_soup.find('div', id="editor")):
    #     author = sub_soup.findn('div', id="editor").a.text
    else:
        author = "Kerangka belum dikenali / Author tidak dipublikasikan"

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
        
    if(category == "popular") :
        listTribun.append({'title' : title.strip(),'author ' : author.strip(), 'date' : configureDate(date).strip(), 'category' : 'popular','link' : link, 'content' : content,'website' : 'tribun.com'}) 
    else:
        listTribun.append({'title' : title.strip(),'author ' : author.strip(), 'date' : configureDate(date).strip(), 'category' : 'biasa','link' : link, 'content' : content,'website' : 'tribun.com'}) 


def setUp(new,category):
    link_new = new['href']
    html_link_new = requests.get(link_new, headers=headers).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new,category)

listTribun = []


for headline in headlines:
    setUp(headline,'biasa')

for new in news:
    setUp(new,'biasa')

for new_famous in news_famous:
    setUp(new_famous,'popular')

for new_story in news_stories:
    setUp(new_story,'biasa')

print(json.dumps(listTribun))

# items = {'Author' : list_author ,'Judul Berita' : list_title, 'Date' : list_date, "Link" : list_link, "Content" : list_content}
# df = pd.DataFrame(items)
# df.to_csv("tribun.csv")