from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from newscatcherapi import NewsCatcherApiClient
import random
from .models import Users,topics

API_KEY = 'L07w1nE0SdD5A7CQhCy6UA4VZZgWyTmKMeJuOQfopTU'
newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)

def home(request):
    choice = []
    value = request.COOKIES.get('topics')
    if value is None:
        choice = ['USA','ukraine','hacking','news', 'cnn']
        news_articles = newscatcherapi.get_search(q=choice[random.randint(0,4)], lang="en", page_size=100, page=random.randint(0,5))['articles']
    else:
        choice = value.replace(',', ' OR ')
        news_articles = newscatcherapi.get_search(q=choice, lang="en",page_size=100, page=random.randint(1,3))['articles']
    for i in news_articles:
        print(i)
        i['summary'] = i['summary']
    print(news_articles)
    context = {
        'articles' : news_articles
    }
    return render(request, 'mainsect/index.html', context)

def explore(request):
    if request.method == "POST":
        try:
            news_articles = newscatcherapi.get_search(q=request.POST["terms"], lang="en")['articles']
            print(news_articles)
            for i in news_articles:
                print(i)
                i['summary'] = i['summary']
            print(news_articles)
            print('lol')
            context = {
                'articles' : news_articles
            }
            print('lol')
            return render(request, 'mainsect/explore.html', context)
        except:
            return HttpResponse('Error')
    news_articles = newscatcherapi.get_search(q="news", lang="en")['articles']
    for i in news_articles:
        print(i)
        i['summary'] = i['summary']
    print(news_articles)
    context = {
        'articles' : news_articles
    }
    return render(request, 'mainsect/explore.html', context)

def about(request, question_id):
    return render(request, 'mainsect/about.html')

def pricing(request, question_id):
    return render(request, 'mainsect/pricing.html')

def contact(request, question_id):
    return render(request, 'mainsect/contact.html')

def login(request):
    if request.method == "POST":
        try:
            print(':')
            if Users.objects.filter(username=request.POST["name"]).first().__dict__['password'] == request.POST['password']:
                print(Users.objects.filter(username=request.POST["name"]).first().__dict__['preferences'])
                x = Users.objects.filter(username=request.POST["name"]).first().__dict__['preferences']
                response = redirect('/')
                response.set_cookie('topics', x)
                return response
        except:
            return HttpResponse('Error')
    return render(request, 'mainsect/Login.html')

def signup(request):
    if request.method == "POST":
        Users.objects.create(email=request.POST["email"],username=request.POST["name"],password=request.POST["password"],preferences=request.POST['choice1']+","+request.POST['choice2']+","+request.POST['choice3'])
        return render(request, 'mainsect/Login.html')
    return render(request, 'mainsect/Signup.html')