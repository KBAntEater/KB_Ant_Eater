from django.shortcuts import render
from .models import News
from django.db import connection
import datetime


# Create your views here.
def index(request):
    news_list = News.objects.filter(news_date = datetime.datetime.today().strftime("%Y-%m-%d"))

    ctx = {'myarr':range(8), 'news_list':news_list}
    return render(request, 'news/news_list.html', ctx)