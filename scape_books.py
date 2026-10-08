import requests
from bs4 import BeautifulSoup
import time

books = []

for page in range(1,6):
    if page ==1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scaping page{page}...")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")



    for book in soup.select("article.product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one("p.price_color").text.strip().replace("Â£", "£")
        rating = book.select_one("p.star-rating")["class"][1]

        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    time.sleep(1)

import pandas as pd
df=pd.DataFrame(books)
print(df.head())
df.to_csv("books_raw.csv",index="False")
print(f"Saved {len(df)} books to books_raw.csv")