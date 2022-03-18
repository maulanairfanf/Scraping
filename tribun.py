from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.tribunnews.com/"
# webbrowser.open(url)
html_text = requests.get(
    url).text
soup = BeautifulSoup(html_text, 'lxml')
headlines = soup.find_all('a', class_="ovh tsa2 pos_rel hladvthumb")
news = soup.find_all('a', class_="f20 ln24 fbo txt-oev-2")
news_famous = soup.find_all('a', class_="fbo2 f15 txt-oev-3")
news_stories = soup.find_all('a', class_="fbo2 f14 al txt-oev-3")
print(soup)


def rules(sub_soup, link):
    title = sub_soup.find('h1', class_="f50 black2 f400 crimson").text
    date = sub_soup.find('time').text

    if (sub_soup.find('div', id="penulis")):
        author = sub_soup.find('div', id="penulis").a.text
    else:
        author = "Tidak terdapat author"
    print(f"Link Berita : {link.strip()}")
    print(f"Judul Berita : {title.strip()}")
    print(f"Author : {author.strip()}")
    print(f"Date : {date.strip()}")
    print(" ")


for headline in headlines:
    link_headline = headline['href']
    html_link_headline = requests.get(link_headline).text
    soup_headline = BeautifulSoup(html_link_headline, 'lxml')
    rules(soup_headline, link_headline)

for new in news:
    link_new = new['href']
    html_link_new = requests.get(link_new).text
    soup_new = BeautifulSoup(html_link_new, 'lxml')
    rules(soup_new, link_new)

for new_famous in news_famous:
    link_new_famous = new_famous['href']
    html_link_new_famous = requests.get(link_new_famous).text
    soup_new_famous = BeautifulSoup(html_link_new_famous, 'lxml')
    rules(soup_new_famous, link_new_famous)

for new_story in news_stories:
    link_new_story = new_story['href']
    html_link_new_story = requests.get(link_new_story).text
    soup_new_story = BeautifulSoup(html_link_new_story, 'lxml')
    rules(soup_new_story, link_new_story)
