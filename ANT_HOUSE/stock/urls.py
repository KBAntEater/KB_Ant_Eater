from django.urls import path

from . import views

# URL 네임 스페이스
app_name = 'stock'

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.stock_recommend, name='stock_recommend'),
    path('my_stock/', views.my_stock, name='my_stock'),
    path('my_stock/delete', views.delete),

    # pybo/가 생략된 ''이 사용되는 이유는 config/urls.py에서 이미 pybo/로 시작하는 url이 pybo/urls.py와 매핑되었기 때문
    # config/urls.py ('news/') + pybo/urls.py ('') = 'pybo/'
    # name='' url 별칭
]