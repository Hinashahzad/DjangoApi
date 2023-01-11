# Generated by Django 4.1.5 on 2023-01-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                (
                    "type",
                    models.CharField(
                        choices=[("Eastern", "Eastern"), ("Western", "Western")],
                        max_length=100,
                    ),
                ),
                ("product_added_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
