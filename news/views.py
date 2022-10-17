from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {'myarr':range(8)}
    return render(request, 'news/news_list.html',ctx)