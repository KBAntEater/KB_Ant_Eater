# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission'),)


class Dividend(models.Model):
    s_ticker = models.CharField(max_length=50)
    dividend_yield = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dividend'


class DjangoAdminLog(models.Model):
    id = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='id', primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mystock(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    s_ticker = models.ForeignKey('Stock', models.DO_NOTHING, db_column='s_ticker')

    class Meta:
        managed = False
        db_table = 'mystock'


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_date = models.DateField()
    news_title = models.CharField(max_length=255)
    news_sum_1 = models.CharField(max_length=255)
    news_sum_2 = models.CharField(max_length=255)
    news_sum_3 = models.CharField(max_length=255)
    news_src = models.CharField(max_length=255)
    news_rep = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'news'


class Realtimestock(models.Model):
    s_ticker = models.ForeignKey('Stock', models.DO_NOTHING, db_column='s_ticker')
    s_time = models.DateField()
    s_now_price = models.IntegerField()
    s_market_cap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'realtimestock'


class Stock(models.Model):
    s_ticker = models.CharField(primary_key=True, max_length=50)
    s_name = models.CharField(max_length=50)
    s_kospi_section = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stock'


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


class Theme(models.Model):
    s_theme = models.CharField(max_length=50, blank=True, null=True)
    s_name = models.CharField(max_length=50, blank=True, null=True)
    c_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theme'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_pwd = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
