import requests
from bs4 import BeautifulSoup
from dados import url


def Noticia ():
    
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html')

    #find the news
    news = soup.find('div', attrs={'class': 'feed-post-body'})

    #find the title
    title = news.find('a', attrs={'class':'feed-post-link'})

