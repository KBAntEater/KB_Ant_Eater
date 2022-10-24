# Generated by Django 4.1.2 on 2022-10-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mystock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'mystock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_date', models.DateField()),
                ('news_title', models.CharField(max_length=255)),
                ('news_sum_1', models.CharField(max_length=255)),
                ('news_sum_2', models.CharField(max_length=255)),
                ('news_sum_3', models.CharField(max_length=255)),
                ('news_src', models.CharField(max_length=255)),
                ('news_rep', models.CharField(max_length=255)),
                ('news_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
    ]
