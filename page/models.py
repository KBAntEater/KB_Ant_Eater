from django.db import models

# Create your models here 

class ant_info(models.Model): # 개미 정보
    # 개인 id. pk
    ant_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30)   
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # mydata에서 추출한 소비 top5
    shop_1 = models.CharField(max_length=30)
    shop_2 = models.CharField(max_length=30)
    shop_3 = models.CharField(max_length=30)
    shop_4 = models.CharField(max_length=30)
    shop_5 = models.CharField(max_length=30)

class ant_stock(models.Model): # 개미-주식 관계
    ant_id = models.CharField(max_length=100)   
    stock_name = models.CharField(max_length=100)   

class stock_info(models.Model):
    stock_name = models.CharField(max_length=100)
    price = models.IntegerField()
    prev_price = models.IntegerField()
    up = models.BooleanField()
    # 그래프 정보를 어떻게 넣을까?
    # 주식 데이터는 얼마나 자주 업데이트할까?