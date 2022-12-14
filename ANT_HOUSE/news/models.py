from django.db import models

# Create your models here.
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
