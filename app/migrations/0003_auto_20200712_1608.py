# Generated by Django 3.0.7 on 2020-07-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200712_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexp',
            name='enddate',
            field=models.DateField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='startdate',
            field=models.DateField(max_length=55, null=True),
        ),
    ]