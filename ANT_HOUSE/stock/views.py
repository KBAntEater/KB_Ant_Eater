from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    return render(request, 'stock/stock_recommend.html')

from django.db import connection
from django.contrib.auth.models import User

def my_stock(request):
    global info
    info = []
    try:
        cursor = connection.cursor()
        # 4 = annie / lhj991202
        # strSql = f"SELECT id, username FROM auth_user WHERE username = '{request.user.username}'; "
        strSql = f"""select a.id, a.username, m.s_ticker, s.s_name, s.s_kospi_section, db.open, db.high, db.low, db.s_volume  
                    from auth_user as a 
                    join mystock as m on a.id = m.user_id 
                    join stock as s on m.s_ticker = s.s_ticker 
                    join stock_db as db on m.s_ticker = db.s_ticker 
                    where a.username = '{request.user.username}'
                    AND db.s_date=(SELECT max(s_date) FROM stock_db);"""
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()
        
        for data in datas:
            row = {
                'id': data[0],
                'username' : data[1],
                's_ticker'  : data[2],
                's_name' : data[3],
                's_kospi_section' : data[4],
                'open' : data[5],
                'high' : data[6],
                'low' : data[7],
                's_volume' : data[8]
            }
            info.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    stock = Stock.objects.all()
    ctx = {'strSql': strSql,'info': info, 'stock': stock}
    return render(request, 'stock/my_stock.html', ctx)


# def search(request):
#     stock = Stock.objects.all()
#     ctx = {'stock': stock}
#     return render(request, 'stock/my_stock.html', ctx)

from django.http import JsonResponse
def get(request):
    try:
        word = request.GET.get('word', '')
        results=[]

        s_name = StockDb.objects.filter(s_name__icontains = word).exists()
        
        if s_name:
            stocks = StockDb.objects.filter(s_name__icontains = word)
            for stock in stocks:
                results.append({
                    'word' : StockDb.s_name
                })
        
        return JsonResponse({'results': results}, status=201)
    
    except Exception as error:
        return JsonResponse({'message': error}, status=400)

# # stock_price 실시간
# import urllib.request, re

# def fetch(daumticker):
#     #print("daumticker",daumticker)
#     url="http://finance.daum.net/item/main.daum?code="
#     txt=urllib.request.urlopen(url+daumticker).read().decode()
#     k=re.search('class="curPrice(.*?)">(.*?)<',txt)
#     if k:
#         price=k.group(60)
#     else:
#         price = "Nothing found for: " + daumticker + " price"
#     return price

# def combine(ticker):
#     price = fetch(ticker)   
#     output=[ticker, price]
#     return output