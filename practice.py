import requests
import bs4

result = requests.get("https://example.com")

print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

print(soup.select("title"))
print(soup.select("title")[0].getText())
