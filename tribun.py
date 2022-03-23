from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.tribunnews.com/"
# webbrowser.open(url)
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
    if (sub_soup.find('h1', class_="f50 black2 f400 crimson")):
        title = sub_soup.find('h1', class_="f50 black2 f400 crimson").text
    elif (sub_soup.find('h1', class_="crimson")):
        title = sub_soup.find('h1', class_="crimson").text
    else:
        print('kerangka website berbeda')

    if(sub_soup.find('time')):
        date = sub_soup.find('time').text
    else:
        author = "kerangka website berbeda"

    if (sub_soup.find('div', id="penulis")):
        author = sub_soup.find('div', id="penulis").a.text
    else:
        author = "kerangka website berbeda"
    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {configureDate(date).strip()}")
    print(" ")


for headline in headlines:
    link_headline = headline['href']
    html_link_headline = requests.get(link_headline, headers=headers).text
    soup_headline = BeautifulSoup(html_link_headline, 'lxml')
    rules(soup_headline, link_headline)

for new in news:
    link_new = new['href']
    html_link_new = requests.get(link_new, headers=headers).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)

for new_famous in news_famous:
    link_new_famous = new_famous['href']
    html_link_new_famous = requests.get(link_new_famous, headers=headers).text
    soup_new_famous = BeautifulSoup(html_link_new_famous, 'lxml')
    rules(soup_new_famous, link_new_famous)

for new_story in news_stories:
    link_new_story = new_story['href']
    html_link_new_story = requests.get(link_new_story, headers=headers).text
    soup_new_story = BeautifulSoup(html_link_new_story, 'lxml')
    rules(soup_new_story, link_new_story)
