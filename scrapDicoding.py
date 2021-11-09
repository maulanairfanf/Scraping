from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.dicoding.com/academies/list').text
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all(
    'div', class_="cta-to-detail")

peoples = soup.find_all('div', class_="d-flex justify-content-between pt-3")
print(peoples)
for people in peoples:
    result = people.find("div", class_="js-enrollment-count")
    print(result)

# print(courses)
# for course in courses:
#     # section1 = course.find("div", class_="cta-to-detail")
#     name = course.find(
#         'p', class_='mb-0 font-weight-bold content-title').text
#     description = course.find('div', class_="mt-2 pb-3 text-gray").text
#     stars = course.find('div', class_="rating").get('data-course-rating')[:4]
#     # user = course.find(
#     #     'div', class_="js-enrollment-count")
#     print(f"Course Name : {name.strip()}")
#     print(f"Description : {description.strip()}")
#     print(f"Star : {stars.strip()}")
#     # print(f"User : {user.strip()}")
#     # print(user)

#     print('')
