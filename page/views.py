import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the page index.")

def add_stock(request):
    return render(request, 'add_stock.html')

def alike_stock(request):
    return render(request, 'alike_stock.html')

def home(request):
    return render(request, 'home.html')

def live_stock(request):
    return render(request, 'live_stock.html')

def news(request):
    return render(request, 'news.html')

def signup(request):
    return render(request, 'signup.html')

def top5(request):
    return render(request, 'top5.html')