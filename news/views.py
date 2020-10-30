from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup



def scrape(request):
    kp_req = requests.get("https://kathmandupost.com/")
    kp_soup = BeautifulSoup(kp_req.content, 'html.parser')
    kp_news = kp_soup.find_all('article', class_="article-image")

    headline = []
    link = []
    detail =[]
    for post in kp_news:
        headline.append(post.find('h3 a'))
        detail.append(post.find('p'))
        link.append(post.find('a')['href'])

    return render(request, 'news/index.html', {'news': zip(headline, detail, link)})