# Generated by Django 3.2.10 on 2021-12-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowest', '0002_auto_20211222_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
