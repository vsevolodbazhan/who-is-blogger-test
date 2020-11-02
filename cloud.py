import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud

NEWS_PAGE_URL = "https://news.google.com/search?q=%20%22Russia%22%20when%3A30d&hl=en-US&gl=US&ceid=US%3Aen"
page = requests.get(NEWS_PAGE_URL).text

soup = BeautifulSoup(page, "html.parser")
headlines = soup.find_all("h3")

words = set()

for headline in headlines:
    for word in headline.get_text().split():
        words.add(word)

wordcloud = WordCloud(max_font_size=40).generate(" ".join(words))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("word_cloud.png", dpi=450)
