from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    'https://buildwithangga.com/catalog/design-courses').text
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all('div', class_="item-pricing item-mentor item-course")
links = []
for course in courses:
    link = course.a["href"]
    links.append(link)

# links = '\n'.join(links)

# print(f"links: {links}")

for link in links:
    # print(link)
    html_links = requests.get(link).text

    sub_soup = BeautifulSoup(html_links, 'lxml')

    name = sub_soup.find('h1', class_='header-primary').text

    if(sub_soup.find('h2', class_="title") and sub_soup.find('h2', class_="title") != "Standard"):
        price = sub_soup.find('h2', class_='title').text.replace('Rp', '')
    else:
        price = "free"

    print(f"Course Name : {name.strip()}")
    print(f"Price : {price.strip()} ")
    print('')
