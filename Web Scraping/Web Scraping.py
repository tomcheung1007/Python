# Web scraping is the process of collecting raw data/code from the web/internet

# HTML and CSS makes up websites
# HTML - displays information/text
# CSS - provides style to website e.g. color, font, animations
# This is important for data science, business intelligence and investigative reporting.
# which can all benefit enormously from collecting and analyzing data


import requests  # allows you to make HTTP requests to use webpage
import bs4  # allows you to pull data/info/code from the web

# EXAMPLE - grab title
# result = requests.get("https://example.com")
# print(result.text)  # source code as raw string

# soup = bs4.BeautifulSoup(result.text, "lxml")  # source code becomes soup object able to grab info
# print(soup)

# print(soup.select("title"))  # grab title >>> [<title>Example Domain</title>]
# print(soup.select("title")[0].getText())  # >>> Example Domain

# Summary
# 1. import request, bs4
# 2. object = request.get("url")
# 3. soup_object = bs4.object.text, "lxml"
# 4. soup.select

# steps 1,2,3 generally stay the same, step 4 is where it varies

# soup.select('div') >>> All elements with the <div> tag
# soup.select('#some_id') >>> elements containing id='some_id'
# soup.select('.some_class') >>> elements containing class='some_class'
# soup.select('div span') >>> Any elements named <span> within an element named <div>
# soup.select('div >span') >>> Any elements named <span>  directly within <div>, with nothing in between

# EXAMPLE - grab image
# 1. make request and make soup object
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup = bs4.BeautifulSoup(res.text, "lxml")
# 2. soup.select - then inspect webpage for specific class call e.g. class="infobox-image"
# computer = soup.select(".infobox-image")[0]

# 3. identify url for image and make request
# image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")

# 4. save image
# f = open("deep_blue.jpg", "wb")  # name and mode
# f.write(image_link.content)
# f.close()

# Webscraping multiple elements. e.g. across multiple pages
# TASK - get title of every book with 2 star rating - http://books.toscrape.com

# 1. Identify structure of URL as you'll be using multiple pages

page_1 = "http://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
page_2 = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html"
page_3 = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html"
# This tells me that what changes is the number i.e. page-2, page-3. We can use for loop

base_url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html"
# print(base_url.format(3))
# By using a base url, we can use string.formatting to update the page number or could loop a range of numbers


# 2. Inspect the page to identify to code for 2 stars - class="product_pod"


# 3. Check to see if scraped code works
result = requests.get(base_url.format(3))  # 3 = page number
soup = bs4.BeautifulSoup(result.text, "lxml")
products = soup.select(".product_pod")  # class call related to stars. Product is each individual book

example = products[3]  # refers to book at index position 3 >> returns code for product
example_2 = products[2]  # refers to book at index position 3 >> returns empty list


# 4. Get book title - inspect code to identify code for title
print(example.select("a"))  # "a" because when you inspect the code. Title is captured in <a .... </a>
# there are two elements, the book image and book title. We use index [1] for title
print(example.select("a")[1])
print(example.select("a")[1]["title"])


# 5. For loop to go through each page and scrape books with two stars

two_star_titles = []  # Empty list to place books in
for n in range(1, 5):  # range(1, 5) for number of pages
    scrape_url = base_url.format(n)  # for loop through each page/url
    res = requests.get(scrape_url)  # make request for each page/url
    soup = bs4.BeautifulSoup(res.text, "lxml")  # soup object for each page/url
    books = soup.select(".product_pod")  # Specify code to scrape

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:  # if number of books not equal to 0
            book_title = book.select("a")[1]["title"]  # obtain book titles
            two_star_titles.append(book_title)  # add book titles to empty list [two_star_titles]
print(two_star_titles)