from bs4 import BeautifulSoup
import requests

url = "https://catalog.umkc.edu/course-offerings/graduate/comp-sci/"
# Getting the webpage, creating a Response object.
response = requests.get(url)
text = response.text
soup = BeautifulSoup(text, "html.parser")
print(soup.title.get_text())
# print(text)
title_list = soup.findAll('span', {'class': "title"})
overview_list = soup.findAll('p', {'class': "courseblockdesc"})
for i in range(len(title_list)):
    print("Course title: ", title_list[i].get_text())
    print("Course overView: ", overview_list[i].get_text())
    print('\n')