from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.dicoding.com/academies/list').text
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all(
    'div', class_="cta-to-detail")
for course in courses:

    name = course.find(
        'p', class_='mb-0 font-weight-bold content-title').text
    description = course.find('div', class_="mt-2 pb-3 text-gray").text
    stars = course.find('div', class_="rating").get('data-course-rating')[:4]

    print(f"Course Name : {name.strip()}")
    print(f"Description : {description.strip()}")
    print(f"Star : {stars.strip()}")

    print('')
