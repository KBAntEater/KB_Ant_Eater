from dataclasses import dataclass
from django.shortcuts import render, redirect
from .models import *

from django.db import connection
from django.contrib.auth.models import User
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import plotly.express as px

import pandas as pd
import numpy as np
from pykrx import stock


# Create your views here.
def index(request):
    return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    def get_stock_logo(c_type):
        if c_type == '생활':
            return 'samsung'
        elif c_type == '쇼핑':
            return 'ssg'
        elif c_type == '식비' or c_type == '의료/건강':
            return 'lg'
        elif c_type == '교통/자동차' or c_type == '기타':
            return 'hs'
        elif c_type == '문화/여가':
            return 'sk'

    if request.method == "POST":
        c_type = request.POST.get('c_type')
        c_price = request.POST.get('c_price')
        c_count = request.POST.get('c_count')

        global theme, theme1
        theme = []
        logo = ""

        try:
            cursor = connection.cursor()

            strSql = f"""SELECT DISTINCT s.s_name, t.c_type, d.dividend_yield FROM theme AS t 
                        JOIN stock AS s ON s.s_name = t.s_name
                        JOIN dividend AS d ON d.s_ticker = s.s_ticker
                        WHERE c_type = '{c_type}'
                        ORDER BY d.dividend_yield DESC;"""
            result = cursor.execute(strSql)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()

            for i in range(0,6):
                if i == 0:
                    theme1 = {
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : format(datas[i][2], ','),
                    }

                else:
                    back = (int(c_price) // int(c_count)) // int(datas[i][2])
        
                    if back == 0:
                        back = 1
                    row = {
                        'index' : i+1,
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : format(datas[i][2], ','),
                        'back' : back,
                    }
                    theme.append(row)
            
            c_price = format(int(c_price), ',')
            print(c_price)
        

        except:
            connection.rollback()
            print("Failed")

        ctx = {'logo' : get_stock_logo(c_type), 'c_type':c_type , 'c_price' : c_price, 'theme1' :theme1, 'theme' : theme, "back" : back }

        print(theme)
        print(get_stock_logo(c_type))

    elif request.method == "GET":

        try:
            theme = []
            cursor = connection.cursor()

            strSql = f"""SELECT DISTINCT s.s_name, t.c_type, d.dividend_yield FROM theme AS t 
                        JOIN stock AS s ON s.s_name = t.s_name
                        JOIN dividend AS d ON d.s_ticker = s.s_ticker
                        WHERE c_type = '생활'
                        ORDER BY d.dividend_yield DESC;"""
            result = cursor.execute(strSql)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()

            for i in range(0,6):
                if i == 0:
                    theme1 = {
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : datas[i][2],
                    }
                else:
                    row = {
                        'index' : i+1,
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : datas[i][2],
                    }
                    theme.append(row)

            print(theme)

        except:
            connection.rollback()
            print("Failed")

        ctx = {"logo" : 'samsung', "theme1" : theme1, 'theme' :theme, 'c_price' : format(87420, ','), 'c_type' : "생활", 'back' : (87420 // 20) // 12000}

    return render(request, 'stock/stock_recommend.html', ctx)


def my_stock(request):

    # 주식 추가
    if request.method == "POST":# and request.action=="add":#파라미터추출, 데이터저장
        
        s_name = request.POST.get('s_name',"")
        
        # 추가
        if s_name :
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
        strSql = f"""select a.id, a.username, m.s_ticker, s.s_name, s.s_kospi_section, new.open, new.high, new.low, new.s_volume  
                    from auth_user as a 
                    join mystock as m on a.id = m.user_id 
                    join stock as s on m.s_ticker = s.s_ticker 
                    join stock_new as new on m.s_ticker = new.s_ticker 
                    where a.username = '{request.user.username}'
                    AND new.s_date=(SELECT max(s_date) FROM stock_new);"""
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        for data in datas:
            
            import pykrx, datetime
            from pykrx import stock
            today = datetime.datetime.today().strftime("%Y%m%d")
            df= stock.get_market_ohlcv(today, today, data[2])
            open = df['시가'][today]
            high = df['고가'][today]
            low = df['저가'][today]
            s_price = df['종가'][today]
            s_volume = df['거래량'][today]

            row = {
                'id': data[0],
                'username' : data[1],
                's_ticker'  : data[2],
                's_name' : data[3],
                's_kospi_section' : data[4],
                'open' : open,
                'high' : high,
                'low' : low,
                's_volume' : s_volume,
                's_price' : s_price
            }
            info.append(row)
            


    except:
        connection.rollback()
        print("error")

    stock = Stock.objects.all()
    ctx = {'strSql': strSql,'info': info, 'stock': stock}
    return render(request, 'stock/my_stock.html', ctx)

def delete(request):
    delete = request.POST.get("s_name")
    print('\n\ndelete\n\n = ', delete)

    cursor = connection.cursor()

    strSql = f"SELECT id FROM auth_user WHERE username = '{request.user.username}'"
    result = cursor.execute(strSql)
    user_id = cursor.fetchone()[0]

    strSql = f"SELECT s_ticker FROM stock WHERE s_name = '{delete}'"
    result = cursor.execute(strSql)
    s_ticker = cursor.fetchone()[0]

    # 4 = annie / lhj991202
    # strSql = f"SELECT id, username FROM auth_user WHERE username = '{request.user.username}'; "
    strSql = f"DELETE FROM mystock WHERE (user_id = {user_id}) AND (s_ticker = '{s_ticker}');"
    result = cursor.execute(strSql)

    connection.commit()
    connection.close()

    return render(request, 'stock/delete.html')