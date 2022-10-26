# Generated by Django 4.1.2 on 2022-10-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_ticker', models.CharField(max_length=50)),
                ('s_name', models.CharField(max_length=255)),
                ('s_date', models.DateField()),
                ('open', models.IntegerField()),
                ('high', models.IntegerField()),
                ('low', models.IntegerField()),
                ('close', models.IntegerField()),
                ('s_volume', models.IntegerField()),
            ],
            options={
                'db_table': 'stock_db',
                'managed': False,
            },
        ),
    ]