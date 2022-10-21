from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    return render(request, 'stock/stock_recommend.html')

from django.db import connection
from django.contrib.auth.models import User

def my_stock(request):

    # 주식 추가
    if request.method == "POST":# and request.action=="add":#파라미터추출, 데이터저장
        s_name = request.POST['s_name']
        print('s_name = '+ s_name)
        cursor = connection.cursor()

        strSql = f"SELECT id FROM auth_user WHERE username = '{request.user.username}'"
        result = cursor.execute(strSql)
        user_id = cursor.fetchone()[0]

        strSql = f"SELECT s_ticker FROM stock WHERE s_name = '{s_name}'"
        result = cursor.execute(strSql)
        s_ticker = cursor.fetchone()[0]

        # 4 = annie / lhj991202
        # strSql = f"SELECT id, username FROM auth_user WHERE username = '{request.user.username}'; "
        strSql = f"INSERT INTO mystock (user_id, s_ticker) VALUES ({user_id}, '{s_ticker}')"
        result = cursor.execute(strSql)

        connection.commit()
        connection.close()

    # 내 주식 테이블 로드
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
        print("error")

    # # 삭제
    # if request.method == "POST" and request.action=="delete":#파라미터추출, 데이터저장
    #     delete = request.POST['delete']
    #     print('\n\ndelete\n\n = ', delete)
    #     cursor = connection.cursor()

    #     strSql = f"""DELETE FROM mystock 
    #                 JOIN stock ON mystock.s_ticker = stock.s_ticker
    #                 WHERE user_id = '{request.user.username}' 
    #                 AND stock.s_name = '{delete}';"""
    #     result = cursor.execute(strSql)
        
    #     connection.commit()
    #     connection.close()

    stock = Stock.objects.all()
    ctx = {'strSql': strSql,'info': info, 'stock': stock}
    return render(request, 'stock/my_stock.html', ctx)