import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movies = []
for title in titles:
   title_text = title.getText()
   movies.append(title_text)
movies.reverse()

for movie in movies:
    print(movie)
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{movie}\n")
