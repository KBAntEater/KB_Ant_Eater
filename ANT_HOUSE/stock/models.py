from django.db import models
from common import *
# Create your models here.
class Stock(models.Model):
    s_ticker = models.CharField(primary_key=True, max_length=50)
    s_name = models.CharField(max_length=50)
    s_kospi_section = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stock'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Mystock(models.Model):
    s_ticker = models.ForeignKey('Stock', models.DO_NOTHING, db_column='s_ticker')
    user_id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'mystock'

class StockDb(models.Model):
    s_ticker = models.CharField(max_length=50)
    s_name = models.CharField(max_length=255)
    s_date = models.DateField()
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()
    s_volume = models.IntegerField()
    kospi = models.FloatField(blank=True, null=True)
    kospi200 = models.FloatField(blank=True, null=True)
    kospi100 = models.FloatField(blank=True, null=True)
    kospi50 = models.FloatField(blank=True, null=True)
    ixic = models.FloatField(db_column='IXIC', blank=True, null=True)  # Field name made lowercase.
    snp500 = models.FloatField(db_column='SnP500', blank=True, null=True)  # Field name made lowercase.
    hsi = models.FloatField(db_column='HSI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_db'

class Theme(models.Model):
    s_theme = models.CharField(max_length=50, blank=True, null=True)
    s_name = models.CharField(max_length=50, blank=True, null=True)
    c_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theme'

class StockDiv(models.Model):
    s_ticker = models.CharField(max_length=255, blank=True, null=True)
    div = models.CharField(db_column='DIV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dividend_yield = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_div'

class StockNew(models.Model):
    s_ticker = models.CharField(max_length=50)
    s_name = models.CharField(max_length=255)
    s_date = models.DateField()
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()
    s_volume = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_new'


class StockPred(models.Model):
    s_date = models.DateTimeField(blank=True, null=True)
    s_ticker = models.IntegerField(blank=True, null=True)
    s_name = models.CharField(max_length=50, blank=True, null=True)
    predict = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_pred'
