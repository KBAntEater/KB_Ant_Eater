from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    return render(request, 'stock/stock_recommend.html')

def my_stock(request):
    return render(request, 'stock/my_stock.html')


    
def my_stock_search(request):
    return render(request, 'stock/my_stock_search.html')