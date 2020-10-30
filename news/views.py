from django.shortcuts import redirect, render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def scrape(request):
    kp_req = requests.get("https://kathmandupost.com/")
    kp_soup = BeautifulSoup(kp_req.content, 'html.parser')
    kp_news = kp_soup.find_all('article', class_="article-image")
    kp_news = kp_news[0: -30]

    headline = []
    link = []
    detail =[]
    author = []

    for post in kp_news:
        headline.append(post.find('a').text)
        detail.append(post.find('p').text)
        author.append(post.find('span').text)
        link.append("https://kathmandupost.com/" + post.find('a')['href'])

    return render(request, 'news/index.html', {'news': zip(headline, detail, author, link)})