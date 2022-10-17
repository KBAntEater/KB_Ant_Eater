from django.db import models

# Create your models here.
class News(models.Model):
    news_url = models.CharField(primary_key=True, max_length=255)
    news_date = models.DateField(blank=True, null=True)
    news_title = models.CharField(max_length=255)
    news_sum_1 = models.CharField(max_length=255)
    news_sum_2 = models.CharField(max_length=255)
    news_sum_3 = models.CharField(max_length=255)
    news_src = models.CharField(max_length=255)
    news_rep = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'news'
