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
