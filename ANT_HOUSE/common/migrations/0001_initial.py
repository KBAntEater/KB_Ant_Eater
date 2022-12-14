# Generated by Django 4.1.2 on 2022-10-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={"db_table": "auth_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_group_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={"db_table": "auth_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={"db_table": "auth_user", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_groups", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_user_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="Dividend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_ticker", models.CharField(max_length=50)),
                ("dividend_yield", models.IntegerField()),
            ],
            options={"db_table": "dividend", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={"db_table": "django_admin_log", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={"db_table": "django_content_type", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={"db_table": "django_migrations", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={"db_table": "django_session", "managed": False,},
        ),
        migrations.CreateModel(
            name="Realtimestock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_time", models.DateField()),
                ("s_now_price", models.IntegerField()),
                ("s_market_cap", models.IntegerField()),
            ],
            options={"db_table": "realtimestock", "managed": False,},
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "s_ticker",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("s_name", models.CharField(max_length=50)),
                ("s_kospi_section", models.CharField(max_length=50)),
            ],
            options={"db_table": "stock", "managed": False,},
        ),
        migrations.CreateModel(
            name="StockDb",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_ticker", models.CharField(max_length=50)),
                ("s_name", models.CharField(max_length=255)),
                ("s_date", models.DateField()),
                ("open", models.IntegerField()),
                ("high", models.IntegerField()),
                ("low", models.IntegerField()),
                ("close", models.IntegerField()),
                ("s_volume", models.IntegerField()),
                ("s_theme", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={"db_table": "stock_db", "managed": False,},
        ),
        migrations.CreateModel(
            name="StockHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_date", models.DateField()),
                ("open", models.IntegerField()),
                ("high", models.IntegerField()),
                ("low", models.IntegerField()),
                ("close", models.IntegerField()),
                ("s_volume", models.IntegerField()),
            ],
            options={"db_table": "stock_history", "managed": False,},
        ),
        migrations.CreateModel(
            name="Theme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_theme", models.CharField(blank=True, max_length=50, null=True)),
                ("s_name", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={"db_table": "theme", "managed": False,},
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("user_pwd", models.CharField(max_length=50)),
                ("user_email", models.CharField(max_length=50)),
            ],
            options={"db_table": "user", "managed": False,},
        ),
    ]
