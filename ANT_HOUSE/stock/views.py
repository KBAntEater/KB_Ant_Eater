from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# def index(request):
#     return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    return render(request, 'stock/stock_recommend.html')

from django.db import connection
from django.contrib.auth.models import User

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
            updown= stock.get_market_ohlcv(today, today, data[2])
            open = updown['시가'][today]
            high = updown['고가'][today]
            low = updown['저가'][today]
            s_price = updown['종가'][today]
            s_volume = updown['거래량'][today]

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

def index(request):

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly
    from plotly import express as px
    from pykrx import stock
    import datetime
    from django.db import connection


    today = datetime.datetime.today().strftime("%Y%m%d")

    cursor = connection.cursor()
    
    sql = "select * from stock"
    cursor.execute(sql)
    stock_info=pd.DataFrame(cursor.fetchall())
    updown=pd.DataFrame()

    # 코스피 등락률 가져오기 
    updown=stock.get_market_price_change_by_ticker(today, today)
    updown['종목코드']=updown.index

    # 코스피 섹터 가져오기 
    stocks = stock_info.copy()
    # print(stocks.columns())
    sector = stocks[[0, 2]].to_numpy() # s_ticker, sector

    # 코스피 사이즈 가져오기 
    size = stock.get_market_cap(today)
    
    # ticker를 안에 넣어주기 
    size['s_ticker']= size.index
    size = size[['s_ticker','시가총액']].to_numpy()


    # 등락률과 섹터 합치는 함수 
    def updown_sector(code):
        for i in range(len(sector)):
            if code == sector[i][0]:
                return sector[i][1]
        return 'No'

    # 등락률과 사이즈 합치는 함수 
    def updown_size(code):
        for i in range(len(size)):
            if code == size[i][0]:
                return size[i][1]
        return 'No'

    #합치기 
    updown['섹터'] = updown['종목코드'].map(updown_sector)
    updown['시가총액'] = updown['종목코드'].map(updown_size)

    # updown=updown.drop(['시가','종가','변동폭','거래량','거래대금'],axis='columns')

    updown['시장구분']='KOSPI'

    updown.loc[updown['섹터'].isna(),'섹터']='우선주'


    # Treemap 그리기
    fig = px.treemap(updown, path=['시장구분','섹터','종목명'], values='시가총액',
                    color='등락률',
                    hover_data=['등락률','종목코드'],
                    
                    range_color=(-0.3,0.3),color_continuous_scale='RdBu')
    fig.update_traces(textposition='middle center',text = updown['등락률'])
    fig.update_traces(textfont_color='white',textfont_size=25)

    fig.update_layout(height=800)
    fig.show()
    ctx = {'updown':updown, 'fig': fig}
    return render (request, 'stock/treemap.html')