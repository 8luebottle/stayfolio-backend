# Generated by Django 2.2.4 on 2019-09-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0018_auto_20190921_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazines',
            name='identifier_kr',
            field=models.CharField(max_length=100),
        ),
    ]