from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    news_list = News.objects.all()
    ctx = {'myarr':range(8), 'news_list':news_list}
    return render(request, 'news/news_list.html', ctx)