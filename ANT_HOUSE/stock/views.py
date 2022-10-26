from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# def index(request):
#     return render(request, 'stock/live_stock_treemap.html')

def stock_recommend(request):
    def get_stock_logo(c_type):
        if c_type == '생활':
            return 'kyobo'
        elif c_type == '쇼핑' or c_type == '의료/건강':
            return 'lotte'
        elif c_type == '식비' :
            return 'shilla'
        elif c_type == '교통/자동차':
            return 'donga'
        elif c_type == '문화/여가':
            return 'hanhwa'
        elif c_type == '기타':
            return 'hd'
# ['', '', 'BNK금융지주', '', '', '', '롯데하이마트', '', '', '', '화승인더', '', '신라교역', '', '하이트진로홀딩스', '대상', '', '', '동아타이어', '태영건설', '', '', 'DL이앤씨', '', '한화투자증권', 'SK텔레콤', '', 'KT', '', '이노션', '', 'SK텔레콤', '휴비스', '', '&G', 'KT', 'HD현대', '세아베스틸지주', '', 'BNK금융지주', '화성산업', '효성']
#  ['교보증권', 'DGB금융지주', 'BNK금융지주', '효성', '부국증권', '현대차증권', '롯데하이마트', '광주신세계', '현대홈쇼핑', 'GS리테일', '화승인더', 'HDC', '신라교역', '대한제당', '하이트진로홀딩스', '대상', '조흥', '삼양사', '동아타이어', '태영건설', '한국가스공사', '금호석유', 'DL이앤씨', 'POSCO홀딩스', '한화투자증권', 'SK텔레콤', '지투알', 'KT', 'LG유플러스', '이노션', '롯데하이마트', 'SK텔레콤', '휴비스', '한국주철관', 'KT&G', 'KT', 'HD현대', '세아베스틸지주', 'DGB금융지주', 'BNK금융지주', '화성산업', '효성']

    def get_predict(s_name):
        if s_name in ['교보증권', 'BNK금융지주', '효성', '부국증권', "현대차증권", '광주신세계', '현대홈쇼핑', 'HDC', 'GS리테일', '대한제당', '조흥', '삼양사', '한국가스공사', '금호석유', 'POSCO홀딩스', '지투알', 'LG유플러스', '롯데하이마트','한국주철관', 'DGB금융지주', 'KT']:
             return '상승'
        else:
            return '하락'
         

    if request.method == "POST":
        c_type = request.POST.get('c_type')
        c_price = request.POST.get('c_price')
        c_count = request.POST.get('c_count')

        global theme, theme1, back1
        theme1 = {}
        theme = []
        logo = ""
        predict = ''
        back1 = 1

        try:
            cursor = connection.cursor()

            strSql = f"""SELECT DISTINCT s.s_name, t.c_type, d.dividend_yield, d.DIV FROM theme AS t 
                        JOIN stock AS s ON s.s_name = t.s_name
                        JOIN stock_div AS d ON d.s_ticker = s.s_ticker
                        WHERE c_type = '{c_type}'
                        ORDER BY d.DIV DESC;"""
            result = cursor.execute(strSql)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()

            for i in range(0,6):
                predict = get_predict(datas[i][0])

                if i == 0:
                    theme1 = {
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : format(datas[i][2], ','),
                        'div' : datas[i][3],
                        'predict' : predict
                    }
                    back1 = (int(c_price) // int(c_count)) // int(datas[i][2])
                    if back1 == 0:
                        back1 = 1

                    print(theme1)

                else:
                    back = (int(c_price) // int(c_count)) // int(datas[i][2])    

                    if back == 0:
                        back = 1
                    row = {
                        'index' : i+1,
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : format(datas[i][2], ','),
                        'div' : datas[i][3],
                        'back' : back,
                        'predict' : predict
                    }
                    theme.append(row)
            
            c_price = format(int(c_price), ',')
        

        except:
            connection.rollback()
            print("Failed")

        ctx = {'logo' : get_stock_logo(c_type), 'c_type':c_type , 'c_price' : c_price, 'theme1' :theme1, 'theme' : theme, "back1" : back1 }

        print(theme)
        print(get_stock_logo(c_type))

    elif request.method == "GET":
        try:
            theme = []
            predict = ""
            cursor = connection.cursor()

            strSql = f"""SELECT DISTINCT s.s_name, t.c_type, d.dividend_yield, d.DIV FROM theme AS t 
                        JOIN stock AS s ON s.s_name = t.s_name
                        JOIN stock_div AS d ON d.s_ticker = s.s_ticker
                        WHERE c_type = '생활'
                        ORDER BY d.DIV DESC;"""
            result = cursor.execute(strSql)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()

            for i in range(0,6):
                predict = get_predict(datas[i][0])
                
                if i == 0:
                    theme1 = {
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : format(datas[i][2], ','),
                        'div' : datas[i][3],
                        'predict' : predict
                    }
                
                else:
                    if i < 6:
                        back = 2
                    elif i > 0 and i < 5:
                        back = 1
                    row = {
                        'index' : i+1,
                        's_name': datas[i][0],
                        'c_type' : datas[i][1],
                        'dividend_yield'  : datas[i][2],
                        'div' : datas[i][3],
                        'back' : back,
                        'predict' : predict
                    }
                    theme.append(row)

        except:
            connection.rollback()
            print("Failed")

        ctx = {"logo" : 'kyobo', "theme1" : theme1, 'theme' :theme, 'c_price' : format(87420, ','), 'c_type' : "생활", 'back1' : (87420 // 17) // 500}

    return render(request, 'stock/stock_recommend.html', ctx)

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


            strSql = f"SELECT user_id, s_ticker FROM mystock WHERE user_id = {user_id} AND s_ticker = '{s_ticker}'"
            result = cursor.execute(strSql)
            exist = cursor.fetchall()

            if exist == (): # empty
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
        strSql = f"""select a.id, a.username, m.s_ticker, s.s_name, s.s_kospi_section 
                    from auth_user as a 
                    join mystock as m on a.id = m.user_id 
                    join stock as s on m.s_ticker = s.s_ticker 
                    where a.username = '{request.user.username}';"""
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
                'open' : format(int(open), ','),
                'high' : format(int(high), ','),
                'low' : format(int(low), ','),
                's_volume' : format(int(s_volume), ','),
                's_price' : format(int(s_price), ',')
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


    today = int(datetime.datetime.today().strftime("%Y%m%d"))

    cursor = connection.cursor()
    
    sql = "select * from stock"
    cursor.execute(sql)
    stock_info=pd.DataFrame(cursor.fetchall())
    updown=pd.DataFrame()

    # 코스피 등락률 가져오기 
    updown=stock.get_market_price_change_by_ticker(str(today), str(today))

    updown['종목코드']=updown.index

    # 코스피 섹터 가져오기 
    stocks = stock_info.copy()
    # print(stocks.columns())
    sector = stocks[[0, 2]].to_numpy() # s_ticker, sector

    # 코스피 사이즈 가져오기 
    size = stock.get_market_cap(str(today))
    
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

    updown = updown.replace('S-Oil','S_Oil')
    updown = updown.replace('S-Oil우','S_Oil우')

    txt='[{name: KOSPI, children: ['+'\n'
    for 섹터 in updown['섹터'].unique() :
        txt+='    {name: '+섹터+', children: ['+'\n'

        종목 = updown[updown['섹터']==섹터]['종목명']
        등락 = updown[updown['섹터']==섹터]['등락률']      
        시가 = updown[updown['섹터']==섹터]['시가총액'] 

        for 종목명, 등락률, 시가총액 in zip(종목, 등락, 시가):
            txt+='        {name: '+ 종목명 +', size: '+ str(시가총액) +', value: '+ str(등락률) +' },'+'\n'
        txt+='    ]},'+'\n'
    txt+=']'+'\n'+'}]'


    # print(txt)

    # with open("TextFile.txt", "w+") as file :
    #     txt="var KOSPI = 'KOSPI';"+'\n'
    #     for 섹터 in updown['섹터'].unique() :
    #         txt+="var " + 섹터 + " = '" + 섹터 + "';"+'\n'
    #         종목 = updown[updown['섹터']==섹터]['종목명']
    #         등락 = updown[updown['섹터']==섹터]['등락률']      
    #         시가 = updown[updown['섹터']==섹터]['시가총액'] 

    #         for 종목명, 등락률, 시가총액 in zip(종목, 등락, 시가):
    #             txt+="var " + 종목명 + " = '" + 종목명 + "';" +'\n'
    #     file.write(txt)
    # file.close()

             
    # updown.to_excel('KB_Ant_Eater\ANT_HOUSE\stock','updown.xlsx')

    # # Treemap 그리기
    # fig = px.treemap(updown, path=['시장구분','섹터','종목명'], values='시가총액',
    #                 color='등락률',
    #                 hover_data=['등락률','종목코드'],
                    
    #                 range_color=(-0.3,0.3),color_continuous_scale='RdBu')
    # fig.update_traces(textposition='middle center',text = updown['등락률'])
    # fig.update_traces(textfont_color='white',textfont_size=25)

    # fig.update_layout(height=800)
    # fig.show()
    ctx = {'updown':updown, 'txt':txt}#, 'fig': fig}
    return render (request, 'stock/treemap.html', ctx)